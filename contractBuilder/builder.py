import subprocess
import time
import os
import shutil




def find_up_ins(blockchain, v_under):
	current_path = os.getcwd()
	sync_path = os.path.join(current_path, "contractBuilder", "ethereum")
	os.chdir(os.path.dirname(sync_path))
	
	if blockchain == 'ethereum':
		geth_process = subprocess.Popen(f'./{blockchain}/sync.sh', shell=True)
		time.sleep(172800)
		subprocess.run(['pkill', 'geth'])
	elif blockchain == 'tron':
		tron_process = subprocess.Popen(f'./{blockchain}/sync.sh', shell=True)
		time.sleep(10)
		log_process = subprocess.Popen('tail -999f ./logs/tron.log', shell=True)
		time.sleep(172800)
		os.system("./tron/stop.sh")
		shutil.rmtree("logs")
		shutil.rmtree("output-directory")
	elif blockchain == 'klaytn':
		geth_process = subprocess.Popen(f'./{blockchain}/sync.sh', shell=True)
		time.sleep(172800)
		subprocess.run(['pkill', 'geth'])
	elif blockchain == 'rsk':
		tron_process = subprocess.Popen(f'./{blockchain}/sync.sh', shell=True)
		time.sleep(10)
		log_process = subprocess.Popen('tail -999f ./logs/rsk.log', shell=True)
		time.sleep(172800)
		shutil.rmtree("logs")
		shutil.rmtree("database")
	else:
		print("No prerequisite for under priced")

	recover_path = os.path.join(current_path, "dos_tool")
	os.chdir(os.path.dirname(recover_path))

def construct_contract(blockchain, v1_pre, v2_pre, v3_pre, v4_pre, datapath):
	args = ["./contractBuilder/contractConstruction", blockchain, v1_pre, v2_pre, v3_pre, v4_pre, datapath]
	subprocess.call(args)



#if __name__ == "__main__":
#	find_up_ins("ethereum")

