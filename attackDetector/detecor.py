import os
import time
import socket
import re
import uuid

def replace_ip(folder):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		ip_address = s.getsockname()[0]
	finally:
		s.close()
	#ip_address = socket.gethostbyname(socket.gethostname())
	

	folder_path = os.path.join("..", folder)

	for root, dirs, files in os.walk(folder_path):
		for file_name in files:
			if file_name.endswith(('.ini', '.sh')):
				file_path = os.path.join(root, file_name)

				with open(file_path, "r") as f:
					content = f.read()

				content = re.sub(r'192\.168\.\d{1,3}\.\d{1,3}', ip_address, content)

				with open(file_path, "w") as f:
					f.write(content)

def build_chain(blockchain):
	if blockchain == "eos":
		cwd = os.getcwd()
		install_path = os.path.join(cwd, "attackDetector", "attack_configuration", "eos_script", "install_eosio.sh")
		os.chdir(os.path.dirname(install_path))

		replace_ip("eos_script")

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

		time.sleep(5)

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

		time.sleep(5)

		try:
			os.system("./transfer_bp.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./return_pri.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

	if blockchain == "telos":
		cwd = os.getcwd()
		install_path = os.path.join(cwd, "attackDetector", "attack_configuration", "eos_script", "install_eosio.sh")
		os.chdir(os.path.dirname(install_path))

		replace_ip("eos_script")

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

		time.sleep(5)

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

		time.sleep(5)

		try:
			os.system("./transfer_bp.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./return_pri.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

	if blockchain == "wax":
		cwd = os.getcwd()
		install_path = os.path.join(cwd, "attackDetector", "attack_configuration", "eos_script", "install_eosio.sh")
		os.chdir(os.path.dirname(install_path))

		replace_ip("eos_script")

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

		time.sleep(5)

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

		time.sleep(5)

		try:
			os.system("./transfer_bp.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./return_pri.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

	if blockchain == "bos":
		cwd = os.getcwd()
		install_path = os.path.join(cwd, "attackDetector", "attack_configuration", "eos_script", "install_eosio.sh")
		os.chdir(os.path.dirname(install_path))

		replace_ip("eos_script")

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

		time.sleep(5)

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

		time.sleep(5)

		try:
			os.system("./transfer_bp.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./return_pri.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

	if blockchain == "solana":
		cwd = os.getcwd()
		install_path = os.path.join(cwd, "attackDetector", "attack_configuration", "solana_script", "victim_node", "install_system.sh")
		os.chdir(os.path.dirname(install_path))

		replace_ip("../solana_script")

		try:
			os.system("./install_system.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./start.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./second.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)


def attack(blockchain):
	if blockchain == "eos":
		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "eos_dos_contract", "cpu_drain_attack")
		os.chdir(os.path.dirname(cpu_path))
		replace_ip("eos_dos_contract")
		# 1. SCP resource drain
		# cpu drain attack
		cwd = os.getcwd()
		print("***", cwd)
		cpu_path = os.path.join(cwd, "..", "eos_dos_contract", "cpu_drain_attack", "cpu_victim", "bianyi.sh")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "..")
		os.chdir(os.path.dirname(cpu_path))

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
		cpu_path = os.path.join(cwd, "..", "ram_drain_attack", "ram_victim", "bianyi.sh")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "..")
		os.chdir(os.path.dirname(cpu_path))

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

	if blockchain == "telos":
		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "eos_dos_contract", "cpu_drain_attack")
		os.chdir(os.path.dirname(cpu_path))
		replace_ip("eos_dos_contract")
		# 1. SCP resource drain
		# cpu drain attack
		cwd = os.getcwd()
		print("***", cwd)
		cpu_path = os.path.join(cwd, "..", "eos_dos_contract", "cpu_drain_attack", "cpu_victim", "bianyi.sh")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "..")
		os.chdir(os.path.dirname(cpu_path))

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
		cpu_path = os.path.join(cwd, "..", "ram_drain_attack", "ram_victim", "bianyi.sh")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "..")
		os.chdir(os.path.dirname(cpu_path))

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

	if blockchain == "wax":
		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "eos_dos_contract", "cpu_drain_attack")
		os.chdir(os.path.dirname(cpu_path))
		replace_ip("eos_dos_contract")
		# 1. SCP resource drain
		# cpu drain attack
		cwd = os.getcwd()
		print("***", cwd)
		cpu_path = os.path.join(cwd, "..", "eos_dos_contract", "cpu_drain_attack", "cpu_victim", "bianyi.sh")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "..")
		os.chdir(os.path.dirname(cpu_path))

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
		cpu_path = os.path.join(cwd, "..", "ram_drain_attack", "ram_victim", "bianyi.sh")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "..")
		os.chdir(os.path.dirname(cpu_path))

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

	if blockchain == "bos":
		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "eos_dos_contract", "cpu_drain_attack")
		os.chdir(os.path.dirname(cpu_path))
		replace_ip("eos_dos_contract")
		# 1. SCP resource drain
		# cpu drain attack
		cwd = os.getcwd()
		print("***", cwd)
		cpu_path = os.path.join(cwd, "..", "eos_dos_contract", "cpu_drain_attack", "cpu_victim", "bianyi.sh")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "..")
		os.chdir(os.path.dirname(cpu_path))

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
		cpu_path = os.path.join(cwd, "..", "ram_drain_attack", "ram_victim", "bianyi.sh")
		os.chdir(os.path.dirname(cpu_path))

		try:
			os.system("./bianyi.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		cwd = os.getcwd()
		cpu_path = os.path.join(cwd, "..", "..")
		os.chdir(os.path.dirname(cpu_path))

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
		stop_path = os.path.join(cwd, "..", "..", "eos_script", "stop_all.sh")
		os.chdir(os.path.dirname(stop_path))

		try:
			os.system("./stop_all.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./unistall_eosio.sh")
		except Exception as e:
			print("An error occurred: ", e)

	if blockchain == "telos":
		cwd = os.getcwd()
		stop_path = os.path.join(cwd, "..", "..", "eos_script", "stop_all.sh")
		os.chdir(os.path.dirname(stop_path))

		try:
			os.system("./stop_all.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./unistall_eosio.sh")
		except Exception as e:
			print("An error occurred: ", e)

	if blockchain == "was":
		cwd = os.getcwd()
		stop_path = os.path.join(cwd, "..", "..", "eos_script", "stop_all.sh")
		os.chdir(os.path.dirname(stop_path))

		try:
			os.system("./stop_all.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./unistall_eosio.sh")
		except Exception as e:
			print("An error occurred: ", e)

	if blockchain == "bos":
		cwd = os.getcwd()
		stop_path = os.path.join(cwd, "..", "..", "eos_script", "stop_all.sh")
		os.chdir(os.path.dirname(stop_path))

		try:
			os.system("./stop_all.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(1)

		try:
			os.system("./unistall_eosio.sh")
		except Exception as e:
			print("An error occurred: ", e)

	if blockchain == "solana":
		cwd = os.getcwd()
		att_path = os.path.join(cwd, "..", "attack_node", "rpc_attack", "src", "build.sh")
		os.chdir(os.path.dirname(att_path))

		try:
			os.system("./build.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		cwd = os.getcwd()
		att_path = os.path.join(cwd, "..", "client", "install_system.sh")
		os.chdir(os.path.dirname(att_path))

		try:
			os.system("./install_system.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./deoloy.sh")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./attack.sh 30 1400")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./attack.sh 50 1400")
		except Exception as e:
			print("An error occurred: ", e)

		time.sleep(5)

		try:
			os.system("./attack.sh 100 1400")
		except Exception as e:
			print("An error occurred: ", e)

def simulate(blockchain):
	build_chain(blockchain)
	attack(blockchain)
	end(blockchain)
