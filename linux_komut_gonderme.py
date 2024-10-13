import paramiko
import argparse
from datetime import datetime
import time
servers = [
    {'ip': '2.59.117.127', 'username': 'root', 'password': 'salata'},
    {'ip': '2.59.117.134', 'username': 'root', 'password': 'salata'},
    {'ip': '2.59.117.147', 'username': 'root', 'password': 'salata'},
    {'ip': '2.59.117.154', 'username': 'root', 'password': 'salata'},
    {'ip': '2.59.117.163', 'username': 'root', 'password': 'salata'},
]

def get_free_memory(ip, username, password):
    try:
        # SSH bağlantısını kur
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password)
        
        # `free -h` komutunu çalıştır
        stdin, stdout, stderr = client.exec_command('free -h')
        output = stdout.read().decode()
        
        client.close()
        
        # Boş RAM değerini ayrıştır
        for line in output.splitlines():
            if 'Mem:' in line:
                parts = line.split()
                free_memory = parts[3]  # Free alan
                return free_memory
        
    except Exception as e:
        print(f"{ip} üzerinde hata oluştu: {e}")
        
    return None
    
 
def run_remote_command(hostname, username, password, token_address):    
        try:
            # SSH istemcisi oluştur
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #commands = f"cd DexScreener && python3 DexScenTokenKontrol.py --add={token_address}"

            # Sunucuya bağlan
            client.connect(hostname, username=username, password=password)
            
            # Komutu çalıştır
            #stdin, stdout, stderr = client.exec_command(commands)
            stdin, stdout, stderr = client.exec_command(f"cd DexScreener && python3 DexScenTokenKontrol.py --add={token_address}")
            client.close()
            #exit()
            # Çıktıyı oku
            print(stdout.read().decode())
            print(stderr.read().decode())
            break
        except Exception as e:
            print(f"Hata: {e}")
            continue
        
        
def main(token_address):
    max_free_memory = 0
    target_server = None
    while True:
        try:
            # Her sunucu için boş RAM miktarını kontrol et
            for server in servers:
                free_memory = get_free_memory(server['ip'], server['username'], server['password'])
                print(f"{server['ip']} için boş RAM: {free_memory}")
                
                # Boş RAM'i karşılaştır
                if free_memory and free_memory.endswith('Gi'):  # Eğer GiB ise
                    free_value = float(free_memory[:-2])  # Son iki karakteri çıkar
                    if free_value > max_free_memory:
                        max_free_memory = free_value
                        target_server = server

            # En yüksek boş RAM'e sahip sunucuya komut gönder
            if target_server:
                print(f"En yüksek boş RAM'e sahip sunucu: {target_server['ip']} ({max_free_memory} GiB)")
                try:
                    with open("ServerCall.txt", "a") as f:
                        f.write(f"{target_server['ip']};({max_free_memory} GB);{(datetime.today().isoformat())[:-5]};{token_address}\n")
                        f.close()
                except Exception as e:
                        print(e)
                run_remote_command(target_server['ip'], target_server['username'], target_server['password'], token_address)
                break
                exit()
        except:
            time.sleep(5)
            pass
       

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if a token is a honeypot")
    parser.add_argument("--add", type=str, required=True, help="The token address to check")

    args = parser.parse_args()
    token_address = args.add
    main(token_address)
    #for hostname in hostnames:
    #    run_remote_command(hostname, username, password, token_address)
