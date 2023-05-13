import os
import time

def build_chain(blockchain):
	if blockchain == "eos":
		cwd = os.getcwd()
		install_path = os.path.join(cwd, "attackDetector", "attack_configuration", "eos_script", "install_eosio.sh")
		os.chdir(os.path.dirname(install_path))

		try:
			os.system("./install_eosio.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./import_wallet.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./genesis_start.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./deploy_contract.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./after_deploy.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./allocate_bp.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./transfer_bp.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./return_pri.sh")
		except Exception as e:
			print("An error occurred: ", e)

def attack(blockchain):
	if blockchain == "eos":
		# 1. SCP resource drain
		# cpu drain attack
		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "attackDetector", "attack_configuration", "eos_dos_contract", "cpu_drain_attack", "cpu_victim")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./cpu_victim/bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./create_account.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./deploy_victim.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./attack_all.sh")
		except Exception as e:
			print("An error occurred: ", e)

		# ram drain attack
		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "attackDetector", "attack_configuration", "eos_dos_contract", "ram_drain_attack", "ram_victim")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./ram_victim/bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./create_account.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./deploy_victim.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./attack_all.sh")
		except Exception as e:
			print("An error occurred: ", e)

def end(blockchain):
	if blockchain == "eos":
		cwd = os.getcwd()
		stop_path = os.path.join(cwd, "attackDetector", "attack_configuration", "eos_script", "stop_all.sh")
		os.chdir(os.path.dirname(stop_path))

		try:
			os.system("./stop_all.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./uninstall_eosio.sh")
		except Exception as e:
			print("An error occurred: ", e)

def simulate(blockchain):
	build_chain(blockchain)
	attack(blockchain)
	end(blockchain)
