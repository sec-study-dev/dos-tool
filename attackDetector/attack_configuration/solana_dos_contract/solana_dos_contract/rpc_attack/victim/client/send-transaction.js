import { Connection, LAMPORTS_PER_SOL, Keypair} from '@solana/web3.js';
import web3 from  '@solana/web3.js';
import BufferLayout from '@solana/buffer-layout';
import { readFileSync } from 'fs';
import internal from 'stream';

//get config
const config = JSON.parse(readFileSync('./config.json', 'utf8'));
const url = config.normalUrl;
const programId = config.victimId;
// console.log(programId);
const interval = parseInt(config.interval);
const sentCount = parseInt(config.sentCount);

const connection = new Connection(url,'confirmed');
const account = Keypair.generate();

await connection.requestAirdrop(account.publicKey, 50 * LAMPORTS_PER_SOL);
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

const transaction = new web3.Transaction();
transaction.add(new web3.TransactionInstruction({
  keys: [],
  programId: new web3.PublicKey(programId),
  data: data,
  }),
);

//send transaction

var sendConunt = 0;
const address = account.publicKey.toString();
var send = setInterval(async function(){
  //send simulate transaction
  const txHash = await connection.sendTransaction(transaction,[account]);
  sendConunt += 1;
  // console.log("number of account \"",address,"\" transactions sent out:",sendConunt);
  if(sendConunt == sentCount) clearInterval(send);
}, interval);
