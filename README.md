# FIN 5120: Blockchain Lab!!!

Welcome to the blockchain lab for FIN 5120. This project contains Python scripts for the class.

## Project Overview

*   **`wallet_generator.py`**: Generates a new Ethereum Public Address and Private Key. It saves these securely to a `.env` file.
*   **`testnet_wallet.py`**: Connects to the blockchain, checks if your keys are loaded, and displays your current balance of SepoliaETH.

## Prerequisites

*   Python 3.x installed on your machine.

## Installation

1.  **Download the code**: Clone this repository or download the ZIP file.
2.  **Open Terminal**: Navigate to the project folder in your command prompt or terminal.
3.  **Install Libraries**: Run the following command to install `web3` and `python-dotenv`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage Guide

### 1. Create your Wallet
Run the generator script once:
```bash
python wallet_generator.py
```
*   **Output**: You will see your new Public Address.
*   **Security**: Your Private Key is saved to a hidden `.env` file. Do not share this file.

### 2. Check Connection & Balance
Run the wallet script:
```bash
python testnet_wallet.py
```
*   If successful, it will print "Connected to Sepolia Testnet".
*   If you have 0 ETH, it will provide a link to a Faucet to get free test funds.

## Troubleshooting
*   **"No keys found"**: Make sure you ran `wallet_generator.py` first.
*   **Connection Failed**: Ensure you have an internet connection. Public nodes can sometimes be busy; try again in a minute.
