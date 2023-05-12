import subprocess
import time




def find_up_ins(blockchain):
	if blockchain == 'ethereum':
		geth_process = subprocess.Popen(f'./{blockchain}/sync.sh', shell=True)
		time.sleep(10)
		subprocess.run(['pkill', 'geth'])

def construct_contract(blockchain, v1_pre, v2_pre, v3_pre, v4_pre, datapath):
	args = ["./contractBuilder/contractConstruction", blockchain, v1_pre, v2_pre, v3_pre, v4_pre, datapath]
	subprocess.call(args)



#if __name__ == "__main__":
#	find_up_ins("ethereum")

