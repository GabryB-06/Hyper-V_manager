# Hyper-V Manager

Tool for managing the activation status of Microsoft Hyper-V \
Useful script as a workaround for various compatibility issues between Hyper-V and VirtualBox/VMware

## Install Dependencies

`pip install -r requirements.txt`

## Configuration

Optionally configure the `riavvio_req` and `tempo_riavvio` parameters in the `config.json` file

- `riavvio_req` sets whether to perform a reboot

> values: `true`/`false`

- `tempo_riavvio` sets the time after which to perform the reboot

> values: time in seconds
