from vyper import compile_code
from web3 import Web3

def main():
    print("Read in the vyper code and deploy it!")
    with open("buy_me_a_coffee.vy", "r") as favorites_file:
        favorites_code = favorites_file.read()
        compliation_details = compile_code(favorites_code, output_formats=["bytecode"])
        print("Compilation Details:", compliation_details)

    
    w3 = Web3(Web3.HTTPProvider('https://virtual.sepolia.eu.rpc.tenderly.co/69be85b3-80c7-48df-8a41-8053bb3cbb4f'))
    favorites_contract = w3.eth.contract(bytecode=compliation_details["bytecode"])
    print(favorites_contract)

if __name__ == "__main__":
    main()