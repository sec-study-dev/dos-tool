# dos-tool


## Requirements
## Requirements

### Required Packages

* **python**3
* **Oracle JDK**1.8
* **rust**
* **nodejs**
* **npm**
* **jq**
* **paramiko**
* **cryptography**36.0.2

Run the following script to install the required packages.

```
sudo apt update
sudo apt install nodejs npm
sudo apt install jq
pip install --upgrade pip
pip install paramiko
pip install cryptography==36.0.2
```

## Running Our Tool

* In order to use the info collector normally, please first fill in your OpenAI API Key in the fourth line of dos-tool/infoCollect/chatgpt.py

* Go to the dos-tool folder and use this command: . /DoSDetector.py

* Enter the type of blockchain you want to detect. The synchronization process will take 48 hours as it is necessary to synchronize a sufficient number of blocks to get accurate information when detecting under priced weaknesses in ethereum, tron, rsk, klaytn.

