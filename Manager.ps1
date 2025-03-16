# Script PowerShell per gestire Hyper-V, Windows Hypervisor Platform e Virtual Machine Platform
# Chiede automaticamente i privilegi di amministratore se non sono attivi e mantiene il menu aperto

# 🔹 Controlla se lo script è in esecuzione come amministratore
$adminCheck = [System.Security.Principal.WindowsPrincipal] [System.Security.Principal.WindowsIdentity]::GetCurrent()
$adminRole = [System.Security.Principal.WindowsBuiltInRole]::Administrator

if (-not $adminCheck.IsInRole($adminRole)) {
    Write-Host "Richiesta di privilegi amministrativi..." -ForegroundColor Yellow
    Start-Process powershell.exe -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

function Controllo-Stato {
    Write-Host "`nStato di Hyper-V e servizi correlati:`n"

    # Controllo stato Hyper-V nel boot manager
    $hyperv_boot = (bcdedit | Select-String "hypervisorlaunchtype") -join "`n"
    if ($hyperv_boot -match "Auto") {
        Write-Host "Hyper-V attivo nel boot manager"
    } elseif ($hyperv_boot -match "Off") {
        Write-Host "Hyper-V disattivato nel boot manager"
    } else {
        Write-Host "Errore nel controllo di Hyper-V nel boot manager"
    }

    # Controllo stato delle feature di Windows
    $features = @("Microsoft-Hyper-V-Hypervisor", "HypervisorPlatform", "VirtualMachinePlatform")
    foreach ($feature in $features) {
        $status = DISM /Online /Get-FeatureInfo /FeatureName:$feature | Out-String
        if ($status -match "Stato : Attivata") {
            Write-Host "$feature è attivo"
        } elseif ($status -match "Stato : Disattivata") {
            Write-Host "$feature è disattivato"
        } else {
            Write-Host "Errore nel controllo di $feature"
        }
    }
}

function Attiva-HyperV {
    Write-Host "`nAttivazione di Hyper-V e servizi correlati..."
    bcdedit /set hypervisorlaunchtype auto
    DISM /Online /Enable-Feature /FeatureName:Microsoft-Hyper-V-Hypervisor /All /NoRestart
    DISM /Online /Enable-Feature /FeatureName:HypervisorPlatform /All /NoRestart
    DISM /Online /Enable-Feature /FeatureName:VirtualMachinePlatform /All /NoRestart
    Write-Host "Hyper-V e servizi attivati. Riavvia il PC per applicare le modifiche."
}

function Disattiva-HyperV {
    Write-Host "`nDisattivazione di Hyper-V e servizi correlati..."
    bcdedit /set hypervisorlaunchtype off
    DISM /Online /Disable-Feature /FeatureName:Microsoft-Hyper-V-Hypervisor /NoRestart
    DISM /Online /Disable-Feature /FeatureName:HypervisorPlatform /NoRestart
    DISM /Online /Disable-Feature /FeatureName:VirtualMachinePlatform /NoRestart
    Write-Host "Hyper-V e servizi disattivati. Riavvia il PC per applicare le modifiche."
}

# 🔹 Mantieni il menu aperto dopo ogni operazione
while ($true) {
    Write-Host "`nGestione Hyper-V"
    Write-Host "1 - Controllare lo stato di Hyper-V"
    Write-Host "2 - Attivare Hyper-V"
    Write-Host "3 - Disattivare Hyper-V"
    Write-Host "4 - Uscire"

    $scelta = Read-Host "Inserisci un'opzione (1-4)"

    switch ($scelta) {
        "1" { Controllo-Stato }
        "2" { Attiva-HyperV }
        "3" { Disattiva-HyperV }
        "4" { exit }
        default { Write-Host "Scelta non valida. Riprova." }
    }
}
