# TODO: troncare l'output di "bcdedit /enum {current}" lasciando solo la stringa "hypervisorlaunchtype" (ultima stringa) con valori "auto" e "off"

import subprocess
from pyuac import main_requires_admin

@main_requires_admin
def main():
    while(True):
        print("1 - Disattiva Hyper-V")
        print("2 - Attiva Hyper-V")
        print("3 - Stato attuale")
        print("4 - Chiusura")
        scelta = int(input())
        if (scelta == 1):
            print()
            output = subprocess.run("bcdedit /set hypervisorlaunchtype off", capture_output=True, text=True) # Attivazione Hyper-V
            print(output.stdout)
        elif (scelta == 2):
            print()
            output = subprocess.run("bcdedit /set hypervisorlaunchtype auto", capture_output=True, text=True) # Disattivazione Hyper-V
            print(output.stdout)
        elif (scelta == 3):
            output = subprocess.run("bcdedit /enum {current}", capture_output=True, text=True) # Stato attuale
            print(output.stdout)
        elif (scelta == 4):
            exit()
        else:
            print()
            print("Scelta non valida")
            print()

if __name__ == "__main__":
    main()