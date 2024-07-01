# Hyper-V Manager

Tool for managing the activation status of Microsoft Hyper-V \
Useful script as a workaround for various compatibility issues between Hyper-V and VirtualBox/VMware

## Install Dependencies

`pip install -r requirements.txt`

## Configuration

Optionally configure the `reboot_requested` and `time_before_reboot` parameters in the `config.json` file

- `reboot_requested` sets whether to perform a reboot

> values: `true`/`false`

- `time_before_reboot` sets the time after which to perform the reboot

> values: time in seconds
