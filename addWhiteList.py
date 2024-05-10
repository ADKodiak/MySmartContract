from web3 import Web3
import os
from dotenv import load_dotenv
import json

# Chargement des variables d'environnement
load_dotenv()

# Récupération des valeurs du fichier .env
private_key = os.getenv('PRIVATE_KEY')
infura_project_id = os.getenv('INFURA_PROJECT_ID')

# Configuration de la connexion au réseau testnet Sepolia
infura_url = f'https://sepolia.infura.io/v3/{infura_project_id}'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Vérification de la connexion
print("Connected:", web3.is_connected())

# Adresse du contrat MyNFT que vous avez déployé
contract_address = '0x8e7bfbfA4f1d141c86E2d07e363CA5d03F15eC67'
from_address = '0x7AFeF4AdB8fa7f480df6f5468eA97d09729BF745'
adress_to = '0x5107c056db49a64b2FfCf0A2c3A0dd843FBb0794'

# Assurez-vous de donner le chemin correct au fichier TokenABI.json
with open('TokenABI.json', 'r') as file:
    abi = json.load(file)


# Créer une instance du contrat
contract = web3.eth.contract(address=contract_address, abi=abi)



#amount_to_send = 100 * (10 ** 18)



# Préparation des données de la transaction pour appeler `mint`
nonce = web3.eth.get_transaction_count(from_address)
tx = contract.functions.addToWhitelist(adress_to).build_transaction({
    'chainId': 11155111,  # Changer selon le réseau
    'gas': 1000000,
    'gasPrice': web3.to_wei('240', 'gwei'),
    'nonce': nonce,
})

# Signature de la transaction
signed_txn = web3.eth.account.sign_transaction(tx, private_key)

# Envoi de la transaction signée
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("Transaction hash:", tx_hash.hex())

# Attente de la confirmation de la transaction
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction receipt:", tx_receipt)
