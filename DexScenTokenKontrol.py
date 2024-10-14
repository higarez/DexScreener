import requests, random, sys, re, time, argparse, json, os, asyncio
from web3 import Web3
from uniswap import Uniswap
from datetime import datetime
from eth_utils import to_checksum_address
from telegram import Bot

aktifsaat=3

sleepy=3
etherscanapikey=["VYCN5DQBDYBWNFMA4XXQM39PEKFGFNQU8G",
        "J857UTDF442WIIKWB596B385FG8AP43X9T",
        "DGSRHIBUXP4K57XZ8MCS6UHU2GAMR3V8QT",
        "1BPAP8D8V1DB4FWJRPEGTIZYP28P3WSWWC",
        "CBFB54G76VADPBS42QZA96SCJ12G1P6C57",
        "G484I2T8B299VXGC7XRVX6J3R53Z6GQY8G",
        "MR6Y5S8W6VSJ9Q9W5BZ9ZFGXGSTEAHT1TW",
        "FURRITC6V79JH61YIYDUFUAQBRTSVXWSAR",
        "KBI7X28JA4QPS2C4PP4FBG7IZTVDSZDBUS",
        "RQDA2UX6TDJY37WTMR78Z4U6RQPPP52M6Y",
        "WF3JWZG96DZVXNSHPNXJ2PHKIQVD3T1ICE",
        "VPDNU67J5YE45ZA2W6HYM3T6GR5XPCUM5S",
        "XDT4ATTB2GSVKHHJ73C8Y5CP2ZYQYUH35K",
        "S1WB9XCV26RXYHWCTFBG65CQZITRE5IU8G",
        "MSH48AMI1H4XQB6U4JDUKZUREIHH41UF3F",
        "GV8TWFSKBCQ7RECT3WZ4H361PR4MBWZFCZ",
        "GV4ZEAYA53VEW2FQU2Z2M1G3D4624TRZXV",
        "DMHI5SPPQ5PYDW6T9XXBRK14BSCN78PHAQ",
        "T78UI1MIJ952WWQEX9A1JDPXWF1GIVGBCD",
        "5AHE7VASQZGJUDA388I6TF6RRFTPQV325C",
        "6Q81B2THN7ZQD2VST933WXUQ2RZGN69D2S",
        "II2XMRJNZ3V17CADJBHZ8Z2Y4YQTJFDC36",
        "YAUFU36BCT5WPI7J9GJENS6N46QYJ938EZ",
        "RITYRDHN2MGAZDV7ZR9SSZNQ5K2NWA58BU",
        "UIZR44ZN1A84HMQE3FT4TT2V6MW4D53QGE",
        "VE3D1VU14XIPK7RK9W5S4CR9RDKM84ADNI",
        "ZAEB9XTWWENEKXVN37RHKYU7TKEGU8KCRI",
        "JRDHM2Z8B542FFWFE755Q394MJCWS6RIUQ",
        "5PDC5C6R6YCIEFYTAV979IADBT3M6WYHS4",
        "N4RY1V9B37S4IYUZ97J2WUU9CNRN5JT55Z"]


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
     
hours, minutes, seconds = map(int, (datetime.today().isoformat()[11:19]).split(':'))
baslangictarihi= hours * 3600 + minutes * 60 + seconds

def get_abi(address):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
            response = requests.get(f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={address}&apikey={random.choice(etherscanapikey)}", headers=headers)
            response = response.json()    
            sourcecode = response['result'][0]["SourceCode"]
            abi = response['result'][0]["ABI"]
            if sourcecode=="":
                #print("Token Kontratı onaylanmamış!")
                time.sleep(1)
            del sourcecode, headers ,response
            return abi
        except Exception as e:
                print(f" -(GetAbi)- Bir Hata oluştu :\n{e}\n")
                continue
                
def get_honeypot_is(token_add):
    try:
        response = requests.get(f"https://api.honeypot.is/v2/IsHoneypot?address={token_address}")
        response = response.json()    
        try:                
            unkrisk = response['simulationSuccess']
            #print(unkrisk)
            if unkrisk == False:
                time.sleep(sleepy)
                response="0"
                del unkrisk
                return response
        except:            
            pass                 
        try:
            code = response['code']
            if code == 404:                    
                time.sleep(sleepy)
                response="0"
                return response
        except:
            return response
        return response
        
    except requests.exceptions.RequestException as e:
        data="0"
        return data

async def send_message(sonucmetin):
    bot = Bot(token="7267134571:AAGdsu-PMVG7q_QRHWpKDzi-wql46YBeBEc")
    await bot.send_message(chat_id='@dex_tarayici', text=sonucmetin)
    
async def send_elite_msg(finalmetin):
    #telegramTOKEN = "7267134571:AAGdsu-PMVG7q_QRHWpKDzi-wql46YBeBEc" advo gem bot 
    #telegramTOKEN = "7849230972:AAHjBYSHEjQYkU0SLLdq8dLLxsatleGeXNs" Voice Sniper Bot
    bot = Bot(token="7849230972:AAHjBYSHEjQYkU0SLLdq8dLLxsatleGeXNs")
    await bot.send_message(chat_id='@AdvoGemAlpha', text=finalmetin)
    
def creator_scan(token_address,sonucmetin):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
            response = requests.get(f"https://api.etherscan.io/api?module=contract&action=getcontractcreation&contractaddresses={token_address}&apikey={random.choice(etherscanapikey)}", headers=headers)
            response = response.json()    
            contractCreator = response['result'][0]["contractCreator"]      
            del response
            response = requests.get(f"https://api.etherscan.io/api?module=account&action=balance&address={contractCreator}&tag=latest&apikey={random.choice(etherscanapikey)}", headers=headers)
            response = response.json() 
            balance = response['result']
            del  response, headers
            #print(float(balance))
            #holderslink=f"https://etherscan.io/token/generic-tokenholders2?m=dark&a={token_address}&s=1000000000000000000&p=1"
            balance=float(balance)/10**18
            #print(balance)
            if balance<3.0:
                break
            else:
                finalmetin=sonucmetin+f"\n--Other Analyzer: https://etherscan.io/token/{token_address}#cards\nContrat Creator: {contractCreator}\nCreator Balance: {balance} ETH\nAll Holders: https://etherscan.io/token/generic-tokenholders2?m=dark&a={token_address}&s=1000000000000000000&p=1"
                asyncio.run(send_elite_msg(finalmetin))
            break
        except Exception as e:
            print(f"-(Creator_Scan)- Bir Hata oluştu :\n{e}\n")
            continue

def getdexinfo(token_address):
    try:
        while True:
            hours, minutes, seconds = map(int, (datetime.today().isoformat()[11:19]).split(':'))
            simdikizaman= hours * 3600 + minutes * 60 + seconds
            if simdikizaman-baslangictarihi>3600*aktifsaat:
                    exit()
                    del simdikizaman
                    break
            try:                
                response = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{token_address}")
                response = response.json() 
                priceNative = response['pairs'][0]['priceNative']
                priceUsd = response['pairs'][0]['priceUsd']
                marketCap = response['pairs'][0]['marketCap']
                websites = response['pairs'][0]['info']['websites']
                finalmetin=f"\nPrice USD: {priceUsd}"+f"\nMarket Cap: {marketCap}"
            
                for item in websites:
                    finalmetin=finalmetin+f"\nWeb Sites: {item['url']}"
                socials = response['pairs'][0]['info']['socials']
                for item in socials:
                    finalmetin=finalmetin+f"\nSocial: {item['url']}"

                del priceNative, priceUsd,marketCap,websites,socials,response
                return finalmetin
                break
            except Exception as e:
                time.sleep(sleepy)
                continue
                
    except Exception as e:
        print(f" -(GetDexInfo)- Bir Hata oluştu :\n{e}\n")
        
def get_ownerinfo(token_address):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
            response = requests.get(f"https://etherscan.io/readcontract?a={token_address}", headers=headers)
            response=response.text
            index = response.find('href="/address/')
            response=response[index+15:]
            index = response.find('" target="_parent">')
            response=response[:index]
            del headers, index
            return response
        except Exception as e:
            print(f" -(Get_OwnerInfo)- Bir Hata oluştu :\n{e}\n")
            continue
    
def getcontractinfo(token_add):
    while True:  
        web3 = Web3(Web3.HTTPProvider(random.choice(URLS)))        
        if not web3.is_connected():            
            continue
        else:         
            hours, minutes, seconds = map(int, (datetime.today().isoformat()[11:19]).split(':'))
            simdikizaman= hours * 3600 + minutes * 60 + seconds
            if simdikizaman-baslangictarihi>3600*aktifsaat:
                    exit()
                    del simdikizaman
                    break
            try:
                uniswap_router = web3.eth.contract(address="0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f", abi=get_abi("0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"))                
                weth_address = Web3.to_checksum_address("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
                pair_address = uniswap_router.functions.getPair(token_add, weth_address).call()
                if pair_address == '0x0000000000000000000000000000000000000000':
                    time.sleep(sleepy)
                    continue
                elif pair_address=="":
                    time.sleep(sleepy)
                    continue
                else:
                    del weth_address, uniswap_router
                    return pair_address
                    break
            except Exception as e:
                    print(f"-(GetContractInfo)- Bir Hata oluştu :\n{e}\n")
                    time.sleep(sleepy)
                    continue

def check_token(token_address,pair_address,finalmetin):
    counter=0
    while True:
        try:
            hours, minutes, seconds = map(int, (datetime.today().isoformat()[11:19]).split(':'))
            simdikizaman= hours * 3600 + minutes * 60 + seconds
            if simdikizaman-baslangictarihi>3600*aktifsaat:
                exit()
                del simdikizaman
                break
            if counter >200:
                time.sleep(sleepy)
                #exit()
                break
            counter+=1
            color=True
            data=get_honeypot_is(token_address)
            if data=="0":
                time.sleep(sleepy)
                continue
            
            sonucmetin=f"https://dexscreener.com/ethereum/{pair_address}\n"
            token_name = data['token']['name']
            token_symbol = data['token']['symbol']
            is_honeypot = data['honeypotResult']['isHoneypot']
            risk = data['summary']['risk']
            risk_level = data['summary']['riskLevel']
            buyTax = data['simulationResult']['buyTax']
            sellTax = data['simulationResult']['sellTax']
            transferTax = data['simulationResult']['transferTax']
            liquidity = str(data['pair']['liquidity'])
            index = liquidity.find('.')
            liquidity=float(liquidity[:index])
            
            #if liquidity<100:
                #color="red"
                #print(f"XXXXXXXXXX Not Enoght Liqudity XXXXXXXXXX")
                #sonucmetin=sonucmetin+"XXXXXXXXXX Not Enoght Liqudity XXXXXXXXXX\n"
                
            try:
                holders = data['holderAnalysis']['holders']
            except:
                holders=0
                #print(f"XXXXXXXXXX Not Enoght Holder XXXXXXXXXX")
                #sonucmetin=sonucmetin+f"XXXXXXXXXX Not Enoght Holder XXXXXXXXXX\n"
            if risk_level>1:
                color=False
                #print(f"XXXXXXXXXX {risk_level} Risk Level XXXXXXXXXX")
                sonucmetin=sonucmetin+f"XXXXXXXXXXXXXX {risk_level} Risk Level XXXXXXXXXXXXXX\n"
            if buyTax>10:
                color=False
                #print(f"XXXXXXXXXX Buy Tax {buyTax} XXXXXXXXXX")
                sonucmetin=sonucmetin+f"XXXXXXXXXXXXXX Buy Tax {buyTax} XXXXXXXXXXXXXX\n"
            if sellTax>10:
                color=False
                #print(f"XXXXXXXXXX Sell Tax {sellTax} XXXXXXXXXX")
                sonucmetin=sonucmetin+f"XXXXXXXXXXXXXX Sell Tax {sellTax} XXXXXXXXXXXXXX\n"
            if transferTax>10:
                color=False
                #print(f"XXXXXXXXXX Tranfer Tax {transferTax} XXXXXXXXXX")
                sonucmetin=sonucmetin+f"XXXXXXXXXXXXXX Tranfer Tax {transferTax} XXXXXXXXXXXXXX\n"
            #sonucmetin=sonucmetin+f"https://dexscreener.com/ethereum/{pair_address}\n"
            contrat_owner = get_ownerinfo(token_address)
            try:
                if contrat_owner.find('000000')<0:
                    sonucmetin=sonucmetin+f"\nXXXXXXXXXXXXXXX OWNER NOT RENOUNCED ! XXXXXXXXXXXXXXX\n\n"
                    color=False
            except:
                pass
            sonucmetin=sonucmetin+f"Token Name: {token_name}_-_{token_symbol}\n"+f"Token Address: {token_address}\n"+f"Pair Address: {pair_address}\n"+f"--Is Honeypot: {is_honeypot} --Risk: {risk}\n"+f"--Risk Level: {risk_level} --Holders: {holders}\n"+f"---BuyTax: -- %{buyTax} --\n"+f"---SellTax: -- %{sellTax} --\n"+f"---TransferTax: -- %{transferTax} --"+f"\nContrat Owner: {contrat_owner}\nLiquidity: {liquidity}"   

            if color:
                sonucmetin=sonucmetin+finalmetin+"\n----- ALL Liability is YOURS (DYOR!) -----"
                #asyncio.run(send_message(sonucmetin))
                warning=False
            else:
                sonucmetin=sonucmetin+f"\n\nXXXXXXXXXXXXXXX HONEY POT RİSK XXXXXXXXXXXXXXX\n"                
                sonucmetin=sonucmetin+finalmetin+"\n----- ALL Liability is YOURS (DYOR!) -----"
                warning=True
            try:
                with open("DexScan_.txt", "a") as f:
                    f.write(f"{datetime.today().isoformat()};{sonucmetin}\n")
            except Exception as e:
                    print(e)
            
            del contrat_owner, color, holders, liquidity, index, transferTax, sellTax, buyTax, risk_level, risk, token_name, token_symbol, token_address, pair_address, is_honeypot
            #exit()
            return sonucmetin, warning
            break
        except Exception as e:
            print(f" -(Check_Token)- Bir Hata oluştu :\n{e}\n")
            pass
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if a token is a honeypot")
    parser.add_argument("--add", type=str, required=True, help="The token address to check")
    args = parser.parse_args()
    
    token_address = args.add
    firststart=True
    try:
        while True:
            web3 = Web3(Web3.HTTPProvider(random.choice(URLS)))       
            if not web3.is_connected():
                #print("Web3 Bağlantı Hatası")
                time.sleep(sleepy)
                continue
            else:
                token_address = Web3.to_checksum_address(token_address)
                if firststart==True:
                    pair_address=getcontractinfo(token_address)
                    firststart=False
                    print("First Start, Take Control!")
                #telegramTOKEN = "7849230972:AAHjBYSHEjQYkU0SLLdq8dLLxsatleGeXNs" Voice Sniper Bot
                #telegramTOKEN = "7267134571:AAGdsu-PMVG7q_QRHWpKDzi-wql46YBeBEc"   
                finalmetin = getdexinfo(token_address)
                sonucmetin, warning = check_token(token_address,pair_address,finalmetin)   
                if warning:
                    creator_scan(token_address, sonucmetin)
                    break
                else:
                    creator_scan(token_address, sonucmetin)
                    time.sleep(15)
                    asyncio.run(send_message(sonucmetin))
                break
    except Exception as e:
            print(f"Failed to connect!\n{e}")
