import paramiko
import time

# Target router configuration
router_ip = "192.1.1.1"  # Update to your router's IP if different
port = 22
username = "root"
fake_passwords = ["wrongpass1", "wrongpass2", "wrongpass3", "wrongpass4", "wrongpass5","wrongpass6", "wrongpass7", "wrongpass8", "wrongpass9", "wrongpass10"]

print(f"[*] Starting simulated SSH brute-force attack against {router_ip}...")

for i, pwd in enumerate(fake_passwords, start=1):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        print(f"[-] Attempt {i}: Trying password '{pwd}'...")
        client.connect(router_ip, port=port, username=username, password=pwd, timeout=3)
    except paramiko.AuthenticationException:
        print(f"[+] Attempt {i}: Authentication failed (Expected).")
    except Exception as e:
        print(f"[!] Attempt {i}: Connection error or dropped ({e})")
    finally:
        client.close()
        
    time.sleep(1)

print("[*] Simulation complete. Check your Wazuh logs for triggered alerts!")
