from dotenv import load_dotenv
import os
from web3 import Web3

# 1. Load environment variables (our keys) from the .env file
load_dotenv()

private_key = os.getenv("TESTNET_PRIVATE_KEY")
address = os.getenv("TESTNET_PUBLIC_ADDRESS")

# Check if keys were loaded successfully
if not address or not private_key:
    print("ERROR: No keys found. Please run 'wallet_generator.py' first to create your wallet.")
    exit()


print(f"Loaded Wallet Address: {address}")

# 2. Connect to the Blockchain (Sepolia Testnet)
# We use an RPC node to talk to the blockchain. This acts as a gateway.
# The default setting uses a public node (which may be slower).
# (Optional) To use a private provider (Alchemy/Infura), set SEPOLIA_RPC_URL in your .env file.

rpc_url = os.getenv("SEPOLIA_RPC_URL", "https://ethereum-sepolia-rpc.publicnode.com")

w3 = Web3(Web3.HTTPProvider(rpc_url))

# 3. Verify Connection
if w3.is_connected(): 
    print("SUCCESS: Connected to Sepolia Testnet")
    
    # 4. Check Balance
    balance = w3.eth.get_balance(address)
    print(f"Current Balance: {w3.from_wei(balance, 'ether')} SepoliaETH")

    # 5. Fund Wallet Instructions
    if balance == 0:
        print("\n--- NEED FUNDS? ---")
        print("To get free testnet ETH, visit: https://cloud.google.com/application/web3/faucet/ethereum/sepolia")
        print("-------------------")
else:
    print("Failed to connect to the network. Check your internet connection.")
