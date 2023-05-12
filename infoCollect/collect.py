import re
from infoCollect.chatgpt import chat_gpt

blockchain = "EOS" # default is EOS
command_dict = {}
prerequisites_dict = {
        "v_scp": "",
        "v_free": "",
        "v_under": "",
        "v_rpc": "",
    }


class BaseCommand(object):
    """
    base class
    """

    def __init__(self, command_example="", command=""):
        self.command = command
        self.command_example = command_example
        self.prompt = f"List contract deployment command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        print("BaseCommand extract_command!")

    def get_command_arg(self):
        """
        get command parameters
        """
        print("BaseCommand get_command_arg!")

    def make_command(self):
        """
        construct command
        """
        print("BaseCommand make_command!")

    def set_command_example(self):
        """
        g  et command example
        """
        command_example = chat_gpt(self.prompt)
        # command_example = input(self.prompt)
        self.command_example = command_example

    def show_command(self):
        """
        展示命令
        """
        print("Command is : ", self.command)

    def process(self):
        """
        整个流程
        """
        try:
            self.set_command_example()
            self.extract_command()
            # self.get_command_arg()
            # self.make_command()
            # self.show_command()
        except Exception as e:
            print("Multiple rounds of QA")
            self.process()


class Deploy(BaseCommand):
    """
    1.部署命令
    """

    def __init__(self, ip="", accountname="", contractpath="", accountpermission=""):
        """
        initialization class
        """
        self.ip_arg = "-u http://<host>:<port>"
        self.accountname_arg = "<accountname>"
        self.contractpath_arg = "<contractpath>"
        self.accountpermission_arg = "-p <account_name>@active"

        self.ip = ip
        self.accountname = accountname
        self.contractpath = contractpath
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "set contract"
        self.prompt = f"List contract deployment command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]
        accountname_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[1].strip().split()[0]
        contractpath_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[1].strip().split()[1]
        accountpermission_arg = " ".join(
            command_str.split("cleos")[1].strip().split(self.key_parameter)[1].strip().split()[2:]
        )
        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(accountname_arg) == 0:
            self.accountname_arg = accountname_arg
        if not len(contractpath_arg) == 0:
            self.contractpath_arg = contractpath_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """
        self.ip = input("Please input ip, for example {} : ".format(self.ip_arg))
        self.accountname = input("Please input accountname, for example {} : ".format(self.accountname_arg))
        self.contractpath = input("Please input contractpath, for example {} : ".format(self.contractpath_arg))
        self.accountpermission = input(
            "Please input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter
        if not len(self.accountname) == 0:
            command = command + " " + self.accountname
        if not len(self.contractpath) == 0:
            command = command + " " + self.contractpath
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission
        self.command = command


class Call_contract(BaseCommand):
    """
    2.调用合约
    """

    def __init__(self, ip="", contractname="", actionname="", parameters="", accountpermission=""):
        """
        initialization class
        """
        self.ip_arg = "-u http://<host>:<port>"
        self.contractname_arg = "<contractname>"
        self.actionname_arg = "<actionname>"
        self.parameters_arg = "'<parameters>'"
        self.accountpermission_arg = "-p <account>@<permission>"

        self.ip = ip
        self.contractname = contractname
        self.actionname = actionname
        self.parameters = parameters
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "push action"
        self.prompt = f"List contract call command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]
        data = re.findall("\<(.*?)\>", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)
        contractname_arg = "<" + data[0] + ">"
        actionname_arg = "<" + data[1] + ">"
        data = re.findall("'(.*?)'", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)

        parameters_arg = "'" + data[0] + "'"
        accountpermission_arg = command_str.split(parameters_arg)[-1].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(contractname_arg) == 0:
            self.contractname_arg = contractname_arg
        if not len(actionname_arg) == 0:
            self.actionname_arg = actionname_arg
        if not len(parameters_arg) == 0:
            self.parameters_arg = parameters_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Please input ip, for example {} :".format(self.ip_arg))
        self.contractname = input("Please input contractname, for example {} :".format(self.contractname_arg))
        self.actionname = input("Please input actionname, for example {} :".format(self.actionname_arg))
        self.parameters = input("Please input parameters, for example {} :".format(self.parameters_arg))
        self.accountpermission = input(
            "Please input accountpermission, for example {} :".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter
        if not len(self.contractname) == 0:
            command = command + " " + self.contractname
        if not len(self.actionname) == 0:
            command = command + " " + self.actionname
        if not len(self.parameters) == 0:
            command = command + " " + self.parameters
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission

        self.command = command


class Systemaccount(BaseCommand):
    """
    3.创建系统账户
    """

    def __init__(
        self,
        ip="",
        creatorname="",
        newaccountname="",
        owner_public_key="",
        active_public_key="",
        net="",
        cpu="",
        ram="",
    ):
        """
        initialization class
        """
        self.ip_arg = "-u http://<host>:<port>"
        self.creatorname_arg = "creator_account>"
        self.newaccountname_arg = "<new_account_name>"
        self.owner_public_key_arg = "<owner_public_key>"
        self.active_public_key_arg = "<active_public_key>"
        self.net_arg = "0.1 EOS"
        self.cpu_arg = "0.1 EOS"
        self.ram_arg = "8"

        self.ip = ip
        self.creatorname = creatorname
        self.newaccountname = newaccountname
        self.owner_public_key = owner_public_key
        self.active_public_key = active_public_key
        self.net = net
        self.cpu = cpu
        self.ram = ram

        self.command = ""
        self.command_example = ""
        self.key_parameter = "system newaccount"
        self.prompt = f"List creating a system account command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example

        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]

        data = re.findall("\<(.*?)\>", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)
        creatorname_arg = "<" + data[0] + ">"
        newaccountname_arg = "<" + data[1] + ">"
        owner_public_key_arg = "<" + data[2] + ">"
        active_public_key_arg = "<" + data[3] + ">"

        net_arg = re.findall(".*--stake-net(.*)--stake-cpu.*", command_str)[0].strip()
        cpu_arg = re.findall(".*--stake-cpu(.*)--buy-ram-kbytes.*", command_str)[0].strip()
        ram_arg = re.findall("(?<=--buy-ram-kbytes).*$", command_str)[0].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(creatorname_arg) == 0:
            self.creatorname_arg = creatorname_arg
        if not len(newaccountname_arg) == 0:
            self.newaccountname_arg = newaccountname_arg
        if not len(owner_public_key_arg) == 0:
            self.owner_public_key_arg = owner_public_key_arg
        if not len(active_public_key_arg) == 0:
            self.active_public_key_arg = active_public_key_arg
        if not len(net_arg) == 0:
            self.net_arg = net_arg
        if not len(cpu_arg) == 0:
            self.cpu_arg = cpu_arg
        if not len(ram_arg) == 0:
            self.ram_arg = ram_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Please input ip,for example {} : ".format(self.ip_arg))
        self.creatorname = input("Please input creatorname,for example {} : ".format(self.creatorname_arg))
        self.newaccountname = input("Please input newaccountname,for example {} : ".format(self.newaccountname_arg))
        self.owner_public_key = input(
            "Please input owner_public_key,for example {} : ".format(self.owner_public_key_arg)
        )
        self.active_public_key = input(
            "Please input active_public_key,for example {} : ".format(self.active_public_key_arg)
        )
        self.net = input("Please input net,for example {} : ".format(self.net_arg))
        self.cpu = input("Please input cpu,for example {} : ".format(self.cpu_arg))
        self.ram = input("Please input ram,for example {} : ".format(self.ram_arg))

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter

        if not len(self.creatorname) == 0:
            command = command + " " + self.creatorname
        if not len(self.newaccountname) == 0:
            command = command + " " + self.newaccountname
        if not len(self.owner_public_key) == 0:
            command = command + " " + self.owner_public_key
        if not len(self.active_public_key) == 0:
            command = command + " " + self.active_public_key
        if not len(self.net) == 0:
            command = command + " " + self.net
        if not len(self.cpu) == 0:
            command = command + " " + self.cpu
        if not len(self.ram) == 0:
            command = command + " " + self.ram

        self.command = command


class Open(BaseCommand):
    """
    4.打开钱包
    """

    def __init__(self):
        self.command = ""
        self.command_example = ""

        self.prompt = f"List open wallet command of {blockchain} blockchain client : "

    def make_command(self):
        """
        construct command
        """

        self.command = self.command_example

    def process(self):
        """
        整个流程
        """
        self.set_command_example()
        self.make_command()
        # self.show_command()


class Unlock(BaseCommand):
    """
    5.解锁钱包
    """

    def __init__(self):
        self.command = ""
        self.command_example = ""

        self.prompt = f"List unlock wallet command of {blockchain} blockchain client : "

    def make_command(self):
        """
        construct command
        """

        self.command = self.command_example

    def process(self):
        """
        整个流程
        """
        self.set_command_example()
        self.make_command()
        # self.show_command()


class Transfer(BaseCommand):
    """
    6.转账代币
    """

    def __init__(self, ip="", parameters="", accountpermission=""):
        """
        initialization class
        """

        self.ip_arg = "-u http://<host>:<port>"
        self.parameters_arg = """'["fromaccount","toaccount","quantity","memo"]'"""
        self.accountpermission_arg = "-p <account_name>@active"

        self.ip = ip
        self.parameters = parameters
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""

        self.key_parameter = "push action token transfer"
        self.prompt = f"List push action token transfer command of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]

        data = re.findall("'(.*?)'", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)
        parameters_arg = "'" + data[0] + "'"
        accountpermission_arg = command_str.split(parameters_arg)[-1].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(parameters_arg) == 0:
            self.parameters_arg = parameters_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Plaease input ip, for example {} : ".format(self.ip_arg))
        self.parameters = input("Plaease input parameters, for example {} : ".format(self.parameters_arg))
        self.accountpermission = input(
            "Plaease input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter
        if not len(self.parameters) == 0:
            command = command + " " + self.parameters
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission
        self.command = command


class Delegate(BaseCommand):
    """
    7.抵押（缺）
    """

    def __init__(self, ip="", _from="", to="", net="", cpu="", accountpermission=""):
        """
        initialization class
        """

        self.ip_arg = "-u http://<host>:<port>"
        self._from_arg = ""
        self.to_arg = ""
        self.net_arg = ""
        self.cpu_arg = ""
        self.accountpermission_arg = ""

        self.ip = ip
        self._from = _from
        self.to = to
        self.net = net
        self.cpu = cpu
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "system delegatebw"
        self.prompt = f"List delegatebw command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]

        data = re.findall("\<(.*?)\>", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)

        _from_arg = "<" + data[0] + ">"
        to_arg = "<" + data[1] + ">"
        net_arg = "<" + data[2] + ">"
        cpu_arg = "<" + data[3] + ">"
        accountpermission_arg = command_str.split(cpu_arg)[-1].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(_from_arg) == 0:
            self._from_arg = _from_arg
        if not len(to_arg) == 0:
            self.to_arg = to_arg
        if not len(net_arg) == 0:
            self.net_arg = net_arg
        if not len(cpu_arg) == 0:
            self.cpu_arg = cpu_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Plaease input ip, for example {} : ".format(self.ip_arg))
        self._from = input("Plaease input _from, for example {} : ".format(self._from_arg))
        self.to = input("Plaease input to, for example {} : ".format(self.to_arg))
        self.net = input("Plaease input net, for example {} : ".format(self.net_arg))
        self.cpu = input("Plaease input cpu, for example {} : ".format(self.cpu_arg))
        self.accountpermission = input(
            "Plaease input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter
        if not len(self._from) == 0:
            command = command + " " + self._from
        if not len(self.to) == 0:
            command = command + " " + self.to
        if not len(self.net) == 0:
            command = command + " " + self.net
        if not len(self.cpu) == 0:
            command = command + " " + self.cpu
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission

        self.command = command


class Buyram(BaseCommand):
    """
    8.购买RAM
    """

    def __init__(self, ip="", accountname="", receiver="", amount="", accountpermission=""):
        """
        initialization class
        """

        self.ip_arg = "-u http://<host>:<port>"
        self.accountname_arg = ""
        self.receiver_arg = ""
        self.amount_arg = ""
        self.accountpermission_arg = ""

        self.ip = ip
        self.accountname = accountname
        self.receiver = receiver
        self.amount = amount
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "system buyram"
        self.prompt = f"List buyram command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]

        data = re.findall("\<(.*?)\>", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)

        accountname_arg = "<" + data[0] + ">"
        receiver_arg = "<" + data[1] + ">"
        amount_arg = "<" + data[2] + ">"
        accountpermission_arg = command_str.split(amount_arg)[-1].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(accountname_arg) == 0:
            self.accountname = accountname_arg
        if not len(receiver_arg) == 0:
            self.receiver_arg = receiver_arg
        if not len(amount_arg) == 0:
            self.amount_arg = amount_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Plaease input ip, for example {} : ".format(self.ip_arg))
        self.accountname = input("Plaease input accountname, for example {} : ".format(self.accountname_arg))
        self.receiver = input("Plaease input receiver, for example {} : ".format(self.receiver_arg))
        self.amount = input("Plaease input amount, for example {} : ".format(self.amount_arg))
        self.accountpermission = input(
            "Plaease input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter

        if not len(self.accountname) == 0:
            command = command + " " + self.accountname
        if not len(self.receiver) == 0:
            command = command + " " + self.receiver
        if not len(self.amount) == 0:
            command = command + " " + self.amount
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission

        self.command = command


class Accountinfo(BaseCommand):
    """
    9.获取账户信息
    """

    def __init__(self, ip="", account="", accountpermission=""):
        """
        initialization class
        """

        self.ip_arg = "-u http://<host>:<port>"
        self.account_arg = ""
        self.accountpermission_arg = ""

        self.ip = ip
        self.account = account
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "get account"
        self.prompt = f"List getting account information command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]
        data = re.findall("\<(.*?)\>", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)
        account_arg = "<" + data[0] + ">"
        accountpermission_arg = command_str.split(account_arg)[-1].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(account_arg) == 0:
            self.account_arg = account_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Plaease input ip, for example {} : ".format(self.ip_arg))
        self.account = input("Plaease input account, for example {} : ".format(self.account_arg))
        self.accountpermission = input(
            "Plaease input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter

        if not len(self.account) == 0:
            command = command + " " + self.account
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission

        self.command = command


class Create(BaseCommand):
    """
    10.创建账户
    """

    def __init__(
        self, ip="", creator="", new_account="", owner_public_key="", active_public_key="", accountpermission=""
    ):
        """
        initialization class
        """

        self.ip_arg = "-u http://<host>:<port>"
        self.creator_arg = ""
        self.new_account_arg = ""
        self.owner_public_key_arg = ""
        self.active_public_key_arg = ""
        self.accountpermission_arg = ""

        self.ip = ip
        self.creator = creator
        self.new_account = new_account
        self.owner_public_key = owner_public_key
        self.active_public_key = active_public_key
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "create account"
        self.prompt = f"List creating a account command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]
        data = re.findall("\<(.*?)\>", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)

        creator_arg = "<" + data[0] + ">"
        new_account_arg = "<" + data[1] + ">"
        owner_public_key_arg = "<" + data[2] + ">"
        active_public_key_arg = "<" + data[3] + ">"

        accountpermission_arg = command_str.split(active_public_key_arg)[-1].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(creator_arg) == 0:
            self.creator_arg = creator_arg
        if not len(new_account_arg) == 0:
            self.new_account_arg = new_account_arg
        if not len(owner_public_key_arg) == 0:
            self.owner_public_key_arg = owner_public_key_arg
        if not len(active_public_key_arg) == 0:
            self.active_public_key_arg = active_public_key_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Plaease input ip, for example {} : ".format(self.ip_arg))
        self.creator = input("Plaease input creator, for example {} : ".format(self.creator_arg))
        self.new_account = input("Plaease input new_account_, for example {} : ".format(self.new_account_arg))
        self.owner_public_key = input(
            "Plaease input owner_public_key, for example {} : ".format(self.owner_public_key_arg)
        )
        self.active_public_key = input(
            "Plaease input active_public_key, for example {} : ".format(self.active_public_key_arg)
        )
        self.accountpermission = input(
            "Plaease input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter
        if not len(self.creator) == 0:
            command = command + " " + self.creator
        if not len(self.new_account) == 0:
            command = command + " " + self.new_account
        if not len(self.owner_public_key) == 0:
            command = command + " " + self.owner_public_key
        if not len(self.active_public_key) == 0:
            command = command + " " + self.active_public_key
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission

        self.command = command


class Token(BaseCommand):
    """
    11.创建代币
    """

    def __init__(self, ip="", parameters="", accountpermission=""):
        """
        initialization class
        """

        self.ip_arg = "-u http://<host>:<port>"
        self.parameters_arg = ""
        self.accountpermission_arg = ""

        self.ip = ip
        self.parameters = parameters
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "push action eosio.token create"
        self.prompt = f"List creating a eosio.token action command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]
        data = re.findall("'(.*?)'", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)
        parameters_arg = "'" + data[0] + "'"
        accountpermission_arg = command_str.split(parameters_arg)[-1].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(parameters_arg) == 0:
            self.parameters_arg = parameters_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Plaease input ip, for example {} : ".format(self.ip_arg))
        self.parameters = input("Plaease input creator, for example {} : ".format(self.parameters_arg))
        self.accountpermission = input(
            "Plaease input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter
        if not len(self.parameters) == 0:
            command = command + " " + self.parameters
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission

        self.command = command


class Issue(BaseCommand):
    """
    12.发行代币
    """

    def __init__(self, ip="", parameters="", accountpermission=""):
        """
        initialization class
        """

        self.ip_arg = "-u http://<host>:<port>"
        self.parameters_arg = ""
        self.accountpermission_arg = ""

        self.ip = ip
        self.parameters = parameters
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "push action eosio issue"
        self.prompt = f"List issue a token action command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]
        data = re.findall("'(.*?)'", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)
        parameters_arg = "'" + data[0] + "'"
        accountpermission_arg = command_str.split(parameters_arg)[-1].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(parameters_arg) == 0:
            self.parameters_arg = parameters_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Plaease input ip, for example {} : ".format(self.ip_arg))
        self.parameters = input("Plaease input creator, for example {} : ".format(self.parameters_arg))
        self.accountpermission = input(
            "Plaease input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter
        if not len(self.parameters) == 0:
            command = command + " " + self.parameters
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission

        self.command = command


class Schedule(BaseCommand):
    """
    13.获取时间表
    """

    def __init__(self, ip="", accountpermission=""):
        """
        initialization class
        """

        self.ip_arg = "-u http://<host>:<port>"
        self.parameters_arg = ""
        self.accountpermission_arg = ""

        self.ip = ip
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "get schedule"
        self.prompt = f"List get info about the current schedule command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]
        data = re.findall("'(.*?)'", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)
        if data:
            accountpermission_arg = re.findall("(?<=" + self.key_parameter + ").*$", data)[0].strip()
        else:
            accountpermission_arg = ""
        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Plaease input ip, for example {} : ".format(self.ip_arg))
        self.accountpermission = input(
            "Plaease input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission

        self.command = command


class Wallet(BaseCommand):
    """
    14.查询钱包的密钥对
    """

    def __init__(self, ip="", wallet="", accountpermission=""):
        """
        initialization class
        """

        self.ip_arg = "-u http://<host>:<port>"
        self.wallet_arg = ""
        self.accountpermission_arg = ""

        self.ip = ip
        self.wallet = wallet
        self.accountpermission = accountpermission

        self.command = ""
        self.command_example = ""
        self.key_parameter = "wallet private_keys"
        self.prompt = f"List querying the public key and private key pair of a single wallet command example of {blockchain} blockchain client : "

    def extract_command(self):
        """
        extract command template
        """
        command_str = self.command_example
        ip_arg = command_str.split("cleos")[1].strip().split(self.key_parameter)[0]
        data = re.findall("\<(.*?)\>", command_str.split(self.key_parameter)[1].strip(), re.I | re.M)
        wallet_arg = "-n <" + data[0] + ">"
        accountpermission_arg = command_str.split(wallet_arg)[-1].strip()

        if not len(ip_arg) == 0:
            self.ip_arg = ip_arg
        if not len(wallet_arg) == 0:
            self.wallet_arg = wallet_arg
        if not len(accountpermission_arg) == 0:
            self.accountpermission_arg = accountpermission_arg

    def get_command_arg(self):
        """
        get command parameters
        """

        self.ip = input("Plaease input ip, for example {} : ".format(self.ip_arg))
        self.wallet = input("Plaease input wallet, for example {} : ".format(self.wallet_arg))
        self.accountpermission = input(
            "Plaease input accountpermission, for example {} : ".format(self.accountpermission_arg)
        )

    def make_command(self):
        """
        construct command
        """

        command = "cleos"
        if not len(self.ip) == 0:
            command = command + " " + self.ip
        command = command + " " + self.key_parameter
        if not len(self.wallet) == 0:
            command = command + " " + self.wallet
        if not len(self.accountpermission) == 0:
            command = command + " " + self.accountpermission

        self.command = command


class Replay(BaseCommand):
    """
    15.重放区块链
    """

    def __init__(self):
        self.command = ""
        self.command_example = ""

        self.prompt = f"List nodeos hard replay blockchain command example of {blockchain} blockchain client : "

    def make_command(self):
        """
        construct command
        """

        self.command = "nodeos --hard-replay-blockchain"

    def process(self):
        """
        整个流程
        """
        self.set_command_example()
        self.make_command()
        # self.show_command()

def collect_pre():
    print("Collecting Prerequisite Information...")

    scp_pre = chat_gpt(f"Does the {blockchain} blockchain have delayed operation? Answer yes or no.")
    free_pre = chat_gpt(f"Does the {blockchain} blockchain have free resources? Answer yes or no.")
    under_pre = chat_gpt(f"Does the {blockchain} blockchain define prices for VM commands? Answer yes or no.")
    rpc_pre = chat_gpt(f"Does the {blockchain} blockchain have an RPC interface for local execution of contracts only? Answer yes or no.")

    prerequisites_dict = {
        "v_scp": scp_pre,
        "v_free": free_pre,
        "v_under": under_pre,
        "v_rpc": rpc_pre,
    }


def run(blockchain):

    print("Collecting Command Information...")

    deploy_instance = Deploy()
    deploy_instance.process()
    call_instance = Call_contract()
    call_instance.process()
    systemaccount_instance = Systemaccount()
    systemaccount_instance.process()
    open_instance = Open()
    open_instance.process()
    unlock_instance = Unlock()
    unlock_instance.process()
    transfer_instance = Transfer()
    transfer_instance.process()
    delegate_instance = Delegate()
    delegate_instance.process()
    buy_instance = Buyram()
    buy_instance.process()
    accountinfo_instance = Accountinfo()
    accountinfo_instance.process()
    create_instance = Create()
    create_instance.process()
    token_instance = Token()
    token_instance.process()
    issue_instance = Issue()
    issue_instance.process()
    schedule_instance = Schedule()
    schedule_instance.process()
    wallet_instance = Wallet()
    wallet_instance.process()
    replay_instance = Replay()
    replay_instance.process()

    command_dict = {
        "deploy": deploy_instance,
        "call": call_instance,
        "systemaccount": systemaccount_instance,
        "open": open_instance,
        "unlock": unlock_instance,
        "transfer": transfer_instance,
        "delegate": delegate_instance,
        "buy": buy_instance,
        "accountinfo": accountinfo_instance,
        "create": create_instance,
        "token": token_instance,
        "issue": issue_instance,
        "schedule": schedule_instance,
        "wallet": wallet_instance,
        "replay": replay_instance,
    }

    collect_pre()
    
    print("All information has been collected")




# if __name__ == "__main__":
#     run()
