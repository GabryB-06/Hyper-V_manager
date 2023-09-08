# Hyper-V manager

Tool per la gestione dello stato di attivazione di Microsoft Hyper-V \
Script utile come workaround per i vari problemi di compatibilità tra Hyper-V e VirtualBox/VMware

## Installazione dipendenze

`pip install -r requirements.txt`

## Configurazione

Eventualmente configurare nel file `config.json` i parametri `riavvio_req` e `tempo_riavvio` \
`riavvio_req` imposta se eseguire il riavvio

- valori: `true`/`false`

`tempo_riavvio` imposta il tempo dopo cui eseguire il riavvio

- valori: tempo in secondi
