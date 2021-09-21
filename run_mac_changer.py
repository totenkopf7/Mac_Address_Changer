#!/usr/bin/env python

import subprocess

subprocess.call("clear")

Logo = """

      __  __               ____ _                                   ____            _           _
     |  \/  | __ _  ___   / ___| |__   __ _ _ __   __ _  ___ _ __  |  _ \ _ __ ___ (_) ___  ___| |_
     | |\/| |/ _` |/ __| | |   | '_ \ / _` | '_ \ / _` |/ _ \ '__| | |_) | '__/ _ \| |/ _ \/ __| __|
     | |  | | (_| | (__  | |___| | | | (_| | | | | (_| |  __/ |    |  __/| | | (_) | |  __/ (__| |_
     |_|  |_|\__,_|\___|  \____|_| |_|\__,_|_| |_|\__, |\___|_|    |_|   |_|  \___// |\___|\___|\__|
                                                  |___/                          |__/


    """

print(Logo)
print("Project created by: TotenKopf")
print("----------------------------------------------------------------------------------------")

interface = input("[-] Type the interface that you want to change: ")
if not interface:
    print("[-] Please specify the interface!")

else:

    subprocess.call(["ifconfig", interface, "down"])
    print("[+] Setting the interface ...")
    print("[+] Interface has been chosen.")

    print("-----------------------------------------------------------------------")

    new_mac = input("[-] Type the mac desired Mac Address: ")
    if not new_mac:
        print("[-] please specify the new Mac Address!")

    else:

        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
        print("[+] Changing the Mac Address...")
        print("[+] Mac Address has been changed successfully!")
        print(f"New Mac_address is: {new_mac}")
