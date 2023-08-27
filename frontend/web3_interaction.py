from web3 import Web3

ganache_url = "YOUR_RPC_URL"; 

# connect to your local ganache rpc 
w3 = Web3(Web3.HTTPProvider(ganache_url)); 

if w3.isConnected():
    print("Connected to your local Ethereum network")
else:
    print("Failed to connect")

# retrieve accounts adress from ganache
account_addr1 = "YourFirstAccountAddress"
account_addr2 = "YourSecondAccountAddress"

private_key = "YourPrivateKey"

# get the nonce for the account
nonce = w3.eth.getTransactionCount(account_addr1)

# buil a transaction 
tx = {
    'nonce': nonce,
    'to': account_addr2,
    'value': w3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei')
}

# sign a transaction
signed_tx = w3.eth.account.signTransaction(tx, private_key)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print("Transaction sent with this hash: ", tx_hash.hex())