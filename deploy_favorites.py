from vyper import compile_code
from web3 import Web3

def main():
    print("Read in the vyper code and deploy it!")
    with open("buy_me_a_coffee.vy", "r") as favorites_file:
        favorites_code = favorites_file.read()
        compliation_details = compile_code(favorites_code, output_formats=["bytecode", "abi"])
        # print("Compilation Details:", compliation_details)

    
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    favorites_contract = w3.eth.contract(bytecode=compliation_details["bytecode"], abi=compliation_details["abi"])
    # print(favorites_contract)

    print("Building the transaction to deploy the contract...")
    transaction = favorites_contract.constructor().build_transaction()

if __name__ == "__main__":
    main()