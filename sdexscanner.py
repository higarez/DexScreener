import os, random, time, subprocess, requests,  json, sys
from web3 import Web3
from datetime import datetime

sleepy=1
hidden=True


URLS = ["https://mainnet.infura.io/v3/fa90fd8d679a401f8fd45a271760b987",
        "https://mainnet.infura.io/v3/e0a910e5638f4d3a8dde924c940759c5",
        "https://mainnet.infura.io/v3/db2185997ccb47f59843d70db0a0651b",
        "https://mainnet.infura.io/v3/d85b64720fff420e892de868beea517c",
        "https://mainnet.infura.io/v3/fa6549b722ab4179a85b3c15bd486981",
        "https://mainnet.infura.io/v3/c86528f78e8047c19a3b14e27e3487af",
        "https://mainnet.infura.io/v3/fc37bb47f9494d5987f29b9ea5e14ea1",
        "https://mainnet.infura.io/v3/afa4f1b01e7e4689ac4f4f5e14035e3c",
        "https://mainnet.infura.io/v3/3acaf332276e4e5383d16825a6a6461c",
        "https://mainnet.infura.io/v3/8e3339a19af949d0b46f5ddedeaf30d9",
        "https://mainnet.infura.io/v3/7ac51dddd5514743bc4d06cef5dc8ea1",
        "https://mainnet.infura.io/v3/83b16940bbed499f999d10cd75905d9e",
        "https://mainnet.infura.io/v3/fb569ddaa2fb4f58a785c51ea8c1aa85",
        "https://mainnet.infura.io/v3/c8dcaef55f494059bcade1119cfe1e03",
        "https://mainnet.infura.io/v3/bdcf7660ddfb46e8af306b7dd45eb8d5",
        "https://mainnet.infura.io/v3/8f627b13f2b54a66ba961112cfddfbd9",
        "https://mainnet.infura.io/v3/dd0cc53898a04967ad6615e199d5fc54",
        "https://mainnet.infura.io/v3/c9cc4dc3c7fd4fc3b17e2b82c18f5fad",
        "https://mainnet.infura.io/v3/73e68311fc5341e596bb7038a6ca8644",
        "https://mainnet.infura.io/v3/3043c095fa214da1bad47a48aade8415",
        "https://mainnet.infura.io/v3/afeb0067527540d189b7389a4b773268",
        "https://mainnet.infura.io/v3/2e151b5f3e4e4b058749c379d038cb7b",
        "https://mainnet.infura.io/v3/b96b2eb3d0cc4568a29e90d7f0eaee11",
        "https://mainnet.infura.io/v3/cf3e8f7e71654d26832f4ba880f6a375",
        "https://mainnet.infura.io/v3/b899d8e68180450eaa2d5d0ead9d0685",
        "https://mainnet.infura.io/v3/9e1c0320bbae4f6495063644d056c4d3",
        "https://mainnet.infura.io/v3/0fea7f6094d44373afffd693085dbc09", 
		"https://mainnet.infura.io/v3/576da22a662042ef8abe2e8eadaa0ce2",
        "https://mainnet.infura.io/v3/c42d1f0560f94dc3b39bba946f0799db",
        "https://mainnet.infura.io/v3/a99308cc194f47d6905e7155a295ec6d",
        "https://mainnet.infura.io/v3/91e050c9fdc34a10b399685f44ce0389",
        "https://mainnet.infura.io/v3/f5fa7e3f5c324276821edf453514a867",
        "https://mainnet.infura.io/v3/49b08d04ca7f456abd17b01881a82aa3",
        "https://mainnet.infura.io/v3/4a50e650e74648feb7021bea7d8331ba",
        "https://mainnet.infura.io/v3/858dbac3dab24f72a0f6896358a73d1f",
        "https://mainnet.infura.io/v3/cb13203cac6b4341834042063415d35c",
        "https://mainnet.infura.io/v3/53b57dba96fc4228bdbed7655d6d1cb3",
        "https://mainnet.infura.io/v3/b87aae3d6e3449b599cae4766438308d",
        "https://mainnet.infura.io/v3/bb47ba781e8148ad9bda0e90739660ad",
        "https://mainnet.infura.io/v3/04e3390ab8ef4850870749c7b5ba7ce4",
        "https://mainnet.infura.io/v3/eb2de220edbf4afda9648e1ca59dfea7",
        "https://mainnet.infura.io/v3/3a7e16b725bc42b1bfcff8ce65d59e60",
        "https://mainnet.infura.io/v3/27adcd828ea544e99608b7209ea46089",
        "https://mainnet.infura.io/v3/fd496bf2ccfa44fbafb40c26b6767591",
        "https://mainnet.infura.io/v3/ea3ed7364c88475aa32d886b4d4a77c1",
        "https://mainnet.infura.io/v3/e1eaa9cb999c4a398a1f0432f6e30207",
        "https://mainnet.infura.io/v3/60e71345bdc44d439f9e43a56f3fe60c",
        "https://mainnet.infura.io/v3/6fa0b87a6c9f414d838f2b1e06b3246b",
        "https://mainnet.infura.io/v3/e6fe125682cb4b86883771f98057b768",	
        "https://mainnet.infura.io/v3/e52948cc71c74d8797097a7509e10373",	
        "https://eth-mainnet.g.alchemy.com/v2/drcd7mTcR3dbXG9yTXnFJQQWyjpjGzrl",
        "https://eth-mainnet.g.alchemy.com/v2/6TG7sh8FplvOPvLE3QYG_9DjvhIeqEiN",
        "https://eth-mainnet.g.alchemy.com/v2/mndHizJp12hQM3jyDxc-kN133WdNqOBM",
        "https://eth-mainnet.g.alchemy.com/v2/5Ur4mLJ0_n5JGEvOYbIRcLCdGPAAW6oq",
        "https://eth-mainnet.g.alchemy.com/v2/h_uqgT30jDgXz8SbbxGRRNjqNKkp1JUb",
        "https://eth-mainnet.g.alchemy.com/v2/ttVre8nxMeJqtCWfACyJTsqRGzTPjrg_",
        "https://eth-mainnet.g.alchemy.com/v2/P-JbSaH0IXU8ByHqZ3NTqFMoQuGwZSuc"]


def add_token_and_call_checker(contract_address):
        try:
            with open("Subprocess.txt", "a") as f:
                f.write(f"{datetime.today().isoformat()};{contract_address}\n")
                f.close()
        except:
            try:
                with open("SubprocessAlt_.txt", "a") as f:
                    f.write(f"{datetime.today().isoformat()};{contract_address}\n")
                    f.close()
            except Exception as e:
                print(e)
        
        if hidden:
            
            subprocess.Popen(
                [sys.executable, 'linux_komut_gonderme.py', f'--add={contract_address}'],
                stdout=subprocess.DEVNULL,  # Standart çıktıyı sessize al
                stderr=subprocess.DEVNULL,  # Hata çıktısını sessize al
            )
        else:
            os.system(f'start cmd /k "python linux_komut_gonderme.py --add={contract_address}"')

def monitor_blocks():
    while True:
        try:
            web3 = Web3(Web3.HTTPProvider(random.choice(URLS)))        
            if not web3.is_connected():
                connection=False        
                continue
            else:            
                break
        except Exception as e:
            print(f"Failed to connect to Ethereum network.\n{e}")
            pass
    try:
        lastbl = web3.eth.block_number
        print(f"{datetime.today().isoformat()}  Starting block: {lastbl}")
        while True:
            try:
                block = web3.eth.get_block('latest', full_transactions=True)
                if lastbl==block['number']:
                    time.sleep(2.1)
                    continue
                else:
                    print(f"{datetime.today().isoformat()}  Processing block {block['number']}...")
                    lastbl=block['number']
                
                for tx in block.transactions:
                    if tx['to'] is None:  # Contract creation transaction (no 'to' address)
                        #contract_address = get_contract_address_from_tx(web3,tx['hash'])
                        contract_address = web3.eth.get_transaction_receipt(tx['hash']).contractAddress
                        #receipt
                        if contract_address:
                            os.system('cls')
                            print(f"{datetime.today().isoformat()}  New contract deployed at: {contract_address}")
                            #check_token(contract_address)
                            # Optional: Check if it's a token contract via Etherscan API
                            try:
                                with open(f"Subprocess.txt", "r") as file:
                                    # Her satırı alıp noktalı virgül ile ayırıyoruz
                                    lines = [line.strip().split(";") for line in file]
                                with open(f"SubprocessAlt_.txt", "r") as file:
                                    # Her satırı alıp noktalı virgül ile ayırıyoruz
                                    lines = [line.strip().split(";") for line in file]
                                for line in lines:
                                    #print(line[2])
                                    if contract_address==line[1]:
                                        #print("TOKEN ZATEN ALINMIŞ.")
                                        continue
                            except Exception as e:
                                    print(e)
                            add_token_and_call_checker(contract_address)

                time.sleep(10)
            except Exception as e:
                print(e)
                break
    except:
        pass
if __name__ == "__main__":
    try:
        while True:
            monitor_blocks()
    except KeyboardInterrupt:
        print(f"{datetime.today().isoformat()}  \nDöngü sonlandırıldı.")
