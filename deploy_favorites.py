from vyper import compile_code

def main():
    print("Read in the vyper code and deploy it!")
    with open("buy_me_a_coffee.vy", "r") as favorites_file:
        favorites_code = favorites_file.read()
        compliation_details = compile_code(favorites_code, output_formats=["bytecode"])
        print("Compilation Details:", compliation_details)

if __name__ == "__main__":
    main()