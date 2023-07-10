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
            #riavvio()
        elif (scelta == 2):
            print()
            output = subprocess.run("bcdedit /set hypervisorlaunchtype auto", capture_output=True, text=True) # Disattivazione Hyper-V
            print(output.stdout)
            #riavvio()
        elif (scelta == 3):
            output = subprocess.run("bcdedit /enum {current}", capture_output=True, text=True) # Stato attuale
            #print(output.stdout)

            if "hypervisorlaunchtype    Auto" in output.stdout:
                print()
                #print("hypervisorlaunchtype    Auto")
                #print("-------------------")
                print("Hyper-V attivo")
                print()
            elif "hypervisorlaunchtype    Off" in output.stdout:
                print()
                #print("hypervisorlaunchtype    Off")
                #print("-------------------")
                print("Hyper-V disattivato")
                print()
            else:
                print()
                print("Errore nell'output. Output completo:")
                print(output.stdout)

        elif (scelta == 4):
            exit()
        else:
            print()
            print("Scelta non valida")
            print()

#def riavvio():
#    print("Per rendere effettive le modifiche bisogna riavviare il sistema. Riavviare adesso? [S/n]")
#    scelta = input()
#    if (scelta == "n"):
#        print()
#        return
#    else:
#        subprocess.run("shutdown /r /t 30")
#        print("Riavvio programmato tra 30 secondi")
#        print("Utilizzare 'shutdown /a' per annullare")
#        print()

if __name__ == "__main__":
    main()