import subprocess
from infoCollect.collect import run
from infoCollect.collect import prerequisites_dict
from contractBuilder.builder import find_up_ins
from contractBuilder.builder import construct_contract
from attackDetector.detecor import simulate

def model_validation(blockchain):
	args = ["./DoSVER", blockchain]
	subprocess.call(args)

if __name__ == "__main__":

	print("*" * 50)
	blockchain = input("Please input blockchain type (eos, ethereum, rsk, wax, solana, telos, klaytn, tron, bos): ")

	model_validation(blockchain)
	run(blockchain)
	find_up_ins(blockchain, prerequisites_dict["v_under"])
	construct_contract(blockchain, prerequisites_dict["v_scp"], prerequisites_dict["v_free"], prerequisites_dict["v_under"], prerequisites_dict["v_rpc"], "None")
	simulate(blockchain)