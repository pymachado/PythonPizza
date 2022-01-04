import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/<apikey Infura>'))

addressContract = '0x1aEaa601545D852b956494E2714B6AbE36A1dE34'
with open("./PythonPizza.json") as file:
    abiContract = json.load(file)

contract = w3.eth.contract(address= addressContract, abi=abiContract)

value = contract.functions.gretting().call()

print(value)