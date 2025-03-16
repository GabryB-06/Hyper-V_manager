# Hyper-V manager

- ## Python
    Tool per la gestione dello stato di attivazione di Microsoft Hyper-V \
    Script utile come workaround per i vari problemi di compatibilità tra Hyper-V e VirtualBox/VMware

    ### Installazione dipendenze

    `pip install -r requirements.txt`

    ### Configurazione

    Eventualmente configurare nel file `config.json` i parametri `riavvio_req` e `tempo_riavvio` \

  - `riavvio_req` imposta se eseguire il riavvio

    > valori: `true`/`false`

  - `tempo_riavvio` imposta il tempo dopo cui eseguire il riavvio

    > valori: tempo in secondi


- ## Powershell
  
  1. Eseguire Powershell come amministratore
  2. Spostati nella cartella dove si trova il file <b>Manager.ps1</b>
  3. Esegui il comando `Set-ExecutionPolicy Unrestricted -Scope Process`
  4. Premere "s" (Sì)
  5. Esegui il comando `.\Manager.ps1`
 
    - In alternativa è possibile fare click destro e selezionare "Esegui con powershell" dopodichè fornire i privilegi amministratore
