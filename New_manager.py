import subprocess
from pyuac import main_requires_admin

@main_requires_admin
def main():
    while True:
        print("\nGestione Hyper-V")
        print("1 - Controllare lo stato di Hyper-V")
        print("2 - Attivare Hyper-V")
        print("3 - Disattivare Hyper-V")
        print("4 - Esci")
        scelta = input("Inserisci un'opzione (1-4): ")

        if scelta == "1":
            controllo_stato()
        elif scelta == "2":
            attiva_hyperv()
        elif scelta == "3":
            disattiva_hyperv()
        elif scelta == "4":
            break
        else:
            print("Scelta non valida.")

def esegui_comando(comando):
    """ Esegue un comando PowerShell e restituisce l'output, gestendo errori di esecuzione """
    risultato = subprocess.run(["powershell", "-Command", comando], capture_output=True, text=True, encoding="utf-8")

    if risultato.returncode != 0:
        print(f"Errore nell'esecuzione di '{comando}': {risultato.stderr}")
        return ""

    output = risultato.stdout.strip()
    if not output:
        print(f"Attenzione: il comando '{comando}' non ha restituito output.")
        return ""

    return output

def controllo_stato():
    print("\nStato di Hyper-V e servizi correlati:\n")

    # Controllo stato Hyper-V nel boot manager
    hyperv_boot = esegui_comando("bcdedit | findstr /i 'hypervisorlaunchtype'")
    if "Auto" in hyperv_boot:
        print("Hyper-V attivo nel boot manager")
    elif "Off" in hyperv_boot:
        print("Hyper-V disattivato nel boot manager")
    else:
        print("Errore nel controllo di Hyper-V nel boot manager")

    # Controllo stato delle feature
    features = ["Microsoft-Hyper-V-Hypervisor", "HypervisorPlatform", "VirtualMachinePlatform"]
    for feature in features:
        status = esegui_comando(f"DISM /Online /Get-FeatureInfo /FeatureName:{feature}")
        if "Stato : Attivata" in status:
            print(f"{feature} è attivo")
        elif "Stato : Disattivata" in status:
            print(f"{feature} è disattivato")
        else:
            print(f"Errore nel controllo di {feature}")

def attiva_hyperv():
    print("\nAttivazione di Hyper-V e servizi correlati...")
    esegui_comando("bcdedit /set hypervisorlaunchtype auto")
    esegui_comando("DISM /Online /Enable-Feature /FeatureName:Microsoft-Hyper-V-Hypervisor /All /NoRestart")
    esegui_comando("DISM /Online /Enable-Feature /FeatureName:HypervisorPlatform /All /NoRestart")
    esegui_comando("DISM /Online /Enable-Feature /FeatureName:VirtualMachinePlatform /All /NoRestart")
    print("Hyper-V attivato. Riavvia il PC per applicare le modifiche.")

def disattiva_hyperv():
    print("\nDisattivazione di Hyper-V e servizi correlati...")
    esegui_comando("bcdedit /set hypervisorlaunchtype off")
    esegui_comando("DISM /Online /Disable-Feature /FeatureName:Microsoft-Hyper-V-Hypervisor /NoRestart")
    esegui_comando("DISM /Online /Disable-Feature /FeatureName:HypervisorPlatform /NoRestart")
    esegui_comando("DISM /Online /Disable-Feature /FeatureName:VirtualMachinePlatform /NoRestart")
    print("Hyper-V disattivato. Riavvia il PC per applicare le modifiche.")

if __name__ == "__main__":
    main()
