# dos-tool


## Requirements
## Requirements

### Required Packages

* **python**3
* **jq**
* **paramiko**
* **cryptography**36.0.2

Run the following script to install the required packages.

```
pip install --upgrade pip
pip install paramiko
pip install cryptography==36.0.2
```

For the blockchain to be tested, you need to configure its required environment according to the official requirements

## Running Our Tool

* Go to the dos-tool folder and use this command: . /DoSDetector.py

* Enter the type of blockchain you want to detect. The synchronization process will take 48 hours as it is necessary to synchronize a sufficient number of blocks to get accurate information when detecting under priced weaknesses in ethereum, tron, rsk, klaytn.

