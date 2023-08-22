import subprocess
from pyuac import main_requires_admin

tempo_riavvio = "30"
riavvio_req = True

riavvio_programmato = False

@main_requires_admin
def main():
    global riavvio_programmato
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
            riavvio()
        elif (scelta == "2"):
            output = subprocess.run("bcdedit /set hypervisorlaunchtype auto", capture_output=True, text=True) # Disattivazione Hyper-V
            output_pulito = output.stdout.replace("\n", "")
            print("="*40)
            print(output_pulito)
            stato()
            riavvio()
        elif (scelta == "3"):
            print("="*40)
            stato()
        elif (scelta == "4"):
            exit()
        elif (scelta == "5"):
            print("="*40)
            if riavvio_programmato == True:
                subprocess.run("shutdown /a")
                print("Riavvio annullato")
                riavvio_programmato = False
            else:
                print("Il riavvio non è stato pianificato")
            print("="*40)
        else:
            print("Scelta non valida")
            print("="*40)
        comandi()

def comandi():
    print("1 - Disattiva Hyper-V")
    print("2 - Attiva Hyper-V")
    print("3 - Stato attuale")
    print("4 - Chiusura")
    global riavvio_programmato
    if riavvio_programmato == True:
        print("5 - Annulla riavvio")

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

def riavvio():
    global riavvio_req
    if riavvio_req == True:
        global tempo_riavvio
        global riavvio_programmato
        print("Per rendere effettive le modifiche bisogna riavviare il sistema. Riavviare adesso? [S/N]")
        while(True):
            scelta = input()
            if (scelta == "n" or scelta == "N"):
                break
            elif (scelta == "s" or scelta == "S"):
                riavvio_programmato = True
                subprocess.run("shutdown /r /t " + tempo_riavvio)
                print("Riavvio programmato tra " + tempo_riavvio + " secondi")
                break
            else:
                print("Sono accettati solo S e N")
        print("="*40)
    else:
        return

if __name__ == "__main__":
    main()