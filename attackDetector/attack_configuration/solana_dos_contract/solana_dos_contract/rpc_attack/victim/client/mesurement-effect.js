import { Connection, LAMPORTS_PER_SOL, Keypair} from '@solana/web3.js';
import web3 from  '@solana/web3.js';
import { readFileSync,writeFileSync,appendFileSync} from 'fs';

//get config
const config = JSON.parse(readFileSync('./config.json', 'utf8'));
const normalUrl = config.normalUrl;
const syncUrl = config.syncUrl;
const mesureInternal = parseInt(config.mesureInternal);
const mesureCount = parseInt(config.mesureCount);
const programId = config.helloWorldId;

//get connection
const normalConnection = new Connection(normalUrl,'confirmed');
const syncConnection = new Connection(syncUrl,'confirmed');

//get shell parameter

const args = process.argv.splice(2);
const attackerNumber = args.at(0);
const payload = args.at(1);

//set a account

const account = Keypair.generate();

await syncConnection.requestAirdrop(account.publicKey, 10 * LAMPORTS_PER_SOL);
while(true){
  await new Promise((resolve) => setTimeout(resolve, 100));
  if (await syncConnection.getBalance(account.publicKey)) break;
}

//set hello world transaction

const transaction = new web3.Transaction();
transaction.add(new web3.TransactionInstruction({
    keys: [],
    programId:programId,
  }),
);

//write file start
const fileName = "result"+attackerNumber + "_" + payload;
writeFileSync(fileName,"result of  " + attackerNumber + " attacker and " + payload + " payload \n");
appendFileSync(fileName,"time(min)           dapp excute time(ms)     sync slowdown(%) \n");

const startHeight = await normalConnection.getBlockHeight();

//mesure effect

var mesuredCount = 0;

var mesureSend = setInterval(async function(){

  const txHash = await syncConnection.sendTransaction(transaction,[account]);
  const beforeTime = performance.now();
  while(true){
    const txResult = await syncConnection.getParsedTransaction(txHash);
    if(txResult != null){
      break;
    }
  }
  const afterTime = performance.now();
  const timeDiff =  (afterTime - beforeTime).toFixed(2);
  const syncHeight = (await syncConnection.getBlockHeight()) - startHeight;
  const normalHeight =  (await normalConnection.getBlockHeight()) - startHeight;
  const slowDown = ((1 - (syncHeight / normalHeight))* 100).toFixed(2);
  mesuredCount += 1;
  console.log(mesuredCount.toString() +" : { normalHeight : " + normalHeight + " , sync height : " + syncHeight + ", slowDown : " + slowDown + " }");
  appendFileSync(fileName,mesuredCount.toString() +"    " + timeDiff + "    " + slowDown + "\n");
  if(mesuredCount == mesureCount) clearInterval(mesureSend);
}, mesureInternal);

