import os
import time

def build_chain(blockchain):
	if blockchain == "eos":
		cwd = os.getcwd()
		install_path = os.path.join(cwd, "attackDetector", "attack_configuration", "eos_script", "install_eosio.sh")
		os.chdir(os.path.dirname(install_path))
		os.system("./install_eosio.sh")

		time.sleep(1)
		os.system("./import_wallet.sh")

		time.sleep(1)
		os.system("./genesis_start.sh")

		time.sleep(1)
		os.system("./deploy_contract.sh")

		time.sleep(1)
		os.system("./after_deploy.sh")

		time.sleep(1)
		os.system("./allocate_bp.sh")

		time.sleep(1)
		os.system("./transfer_bp.sh")

		time.sleep(1)
		os.system("./return_pri.sh")

def simulate(blockchain):
	build_chain(blockchain)
