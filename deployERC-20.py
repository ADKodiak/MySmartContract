from solcx import install_solc

# Vérifie si solc version 0.8.0 est installé, sinon l'installe
solc_version = '0.8.1'
install_solc(solc_version)



from web3 import Web3
from solcx import compile_standard
import json
from dotenv import load_dotenv
import os

# Ajout de l'importation nécessaire pour le middleware
from web3.middleware import geth_poa_middleware


load_dotenv()

# Charger et compiler le contrat
with open("votedToken.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {"votedToken.sol": {"content": contract_source_code}},
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
            }
        }
    },
},
solc_version='0.8.1',
allow_paths="." 
)

with open("compiled_contract.json", "w") as file:
    json.dump(compiled_sol, file)

# Obtenir bytecode et ABI
bytecode = compiled_sol['contracts']['votedToken.sol']['MyToken']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['votedToken.sol']['MyToken']['abi']
print(abi)
# Sauvegardez l'ABI dans un fichier JSON
with open('TokenABI.json', 'w') as abi_file:
    json.dump(abi, abi_file)
# Connexion à Sepolia
w3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{os.getenv('INFURA_PROJECT_ID')}"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Créer le contrat en blockchain
account = w3.eth.account.from_key(os.getenv('PRIVATE_KEY'))
MyContract = w3.eth.contract(abi=abi, bytecode=bytecode)


initialSupply = 100 * (10 ** 18)

# Créer le contrat en blockchain
transaction = MyContract.constructor(initialSupply).build_transaction({
    'from': account.address,  # Utilisez account.address ici
    'nonce': w3.eth.get_transaction_count(account.address),
    'gas': 2500000,  # J'ai ajusté la valeur du gaz, 1 est très probablement insuffisant
    'gasPrice': w3.to_wei('50', 'gwei')
})
# Signer la transaction
signed = account.sign_transaction(transaction)

# Envoyer la transaction signée
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Contract deployed at address: {tx_receipt.contractAddress}")
