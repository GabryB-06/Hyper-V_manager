import subprocess
from pyuac import main_requires_admin

@main_requires_admin
def main():
    comandi()
    print("="*40)
    stato()
    while(True):
        scelta = input()
        if (scelta == "1"):
            output = subprocess.run("bcdedit /set hypervisorlaunchtype off", capture_output=True, text=True) # Attivazione Hyper-V
            output_pulito = output.stdout.replace("\n", "")
            print("="*40)
            print(output_pulito)
            stato()
            #riavvio()
        elif (scelta == "2"):
            output = subprocess.run("bcdedit /set hypervisorlaunchtype auto", capture_output=True, text=True) # Disattivazione Hyper-V
            output_pulito = output.stdout.replace("\n", "")
            print("="*40)
            print(output_pulito)
            stato()
            #riavvio()
        elif (scelta == "3"):
            print("="*40)
            stato()
        elif(scelta == "4"):
            print("="*40)
            comandi()
            print("="*40)
        elif (scelta == "5"):
            exit()
        else:
            print("Scelta non valida")

def comandi():
    print("1 - Disattiva Hyper-V")
    print("2 - Attiva Hyper-V")
    print("3 - Stato attuale")
    print("4 - Elenco comandi")
    print("5 - Chiusura")

def stato():
    output = subprocess.run("bcdedit /enum {current}", capture_output=True, text=True) # Stato attuale
    if "hypervisorlaunchtype    Auto" in output.stdout:
        print("Stato attuale: Hyper-V attivo")
    elif "hypervisorlaunchtype    Off" in output.stdout:
        print("Stato attuale: Hyper-V disattivato")
    else:
        print("Errore nell'output. Output completo:")
        print(output.stdout)
    print("="*40)
                
#def riavvio():
#    print("Per rendere effettive le modifiche bisogna riavviare il sistema. Riavviare adesso? [S/n]")
#    scelta = input()
#    if (scelta == "n"):
#        #print()
#        return
#    else:
#        subprocess.run("shutdown /r /t 30")
#        print("Riavvio programmato tra 30 secondi")
#        print("Utilizzare 'shutdown /a' per annullare")
#        #print()

if __name__ == "__main__":
    main()