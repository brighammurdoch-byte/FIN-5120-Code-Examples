# Create and Store your very own Ethereum Testnet Wallet!
# This program creates your new Ethereum wallet and prints out the public address and private key.
# (Never share your private key!) 
""" Note: Run this program once. The program takes your public address and private key and stores 
them in the ".env" file. If you run this program again, it will make you new private keys
and replace the old keys in the .env file. If you loose your keys (particularly your 
private key) you will be unable to access any funds on or transactions done with your 
wallet (you can always make a new wallet but keep this in mind). """

from eth_account import Account
import secrets

# Main is what runs when you hit the play button or otherwise run this file. Inside this "main()" funciton we have
# the "generate_wallet()" function, wich is the function that will actualy generate the wallet.
def main():
    wallet = generate_wallet()
    print(f"Your new Ethereum Testnet Wallet: {wallet[0]}")
    print(f"Private Key (keep it secret!): {wallet[1]}")
    
#Generate wallet
def generate_wallet():

    # Generate private key: this is the part of the function that will generate the private key.
    priv = secrets.token_hex(32)
    private_key = "0x" + priv

    # Create account
    acct = Account.from_key(private_key)

    # Save to .env file
    with open(".env", "w") as f:
        f.write(f"TESTNET_PUBLIC_ADDRESS={acct.address}\n")
        f.write(f"TESTNET_PRIVATE_KEY={private_key}\n")

    return (acct.address, private_key)

main()