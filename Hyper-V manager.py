import subprocess
from pyuac import main_requires_admin
import json
import time
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

try:
    with open(__location__+'/config.json', 'r') as config_file:
        config_data = json.load(config_file)
except FileNotFoundError:
    print("Configuration file does not exist.")
    time.sleep(5)
    exit()
except json.JSONDecodeError:
    print("Error parsing JSON file.")
    time.sleep(5)
    exit()

time_before_reboot = str(config_data["time_before_reboot"])
reboot_requested = config_data["reboot_requested"]

planned_reboot = False

@main_requires_admin
def main():
    global planned_reboot
    commands()
    print("="*40)
    status()
    while(True):
        choice = input()
        if (choice == "1"):
            output = subprocess.run("bcdedit /set hypervisorlaunchtype off", capture_output=True, text=True) # Enable Hyper-V
            cleaned_output = output.stdout.replace("\n", "")
            print("="*40)
            print(cleaned_output)
            status()
            schedule_restart()
        elif (choice == "2"):
            output = subprocess.run("bcdedit /set hypervisorlaunchtype auto", capture_output=True, text=True) # Disable Hyper-V
            cleaned_output = output.stdout.replace("\n", "")
            print("="*40)
            print(cleaned_output)
            status()
            schedule_restart()
        elif (choice == "3"):
            print("="*40)
            status()
        elif (choice == "4"):
            exit()
        elif (choice == "5"):
            print("="*40)
            if planned_reboot == True:
                subprocess.run("shutdown /a")
                print("Restart cancelled")
                planned_reboot = False
            else:
                print("No restart is scheduled")
            print("="*40)
        else:
            print("Invalid choice")
            print("="*40)
        commands()

def commands():
    print("1 - Disable Hyper-V")
    print("2 - Enable Hyper-V")
    print("3 - Current status")
    print("4 - Exit")
    global planned_reboot
    if planned_reboot == True:
        print("5 - Cancel restart")

def status():
    output = subprocess.run("bcdedit /enum {current}", capture_output=True, text=True) # Current status
    if "hypervisorlaunchtype    Auto" in output.stdout:
        print("Current status: Hyper-V is enabled")
    elif "hypervisorlaunchtype    Off" in output.stdout:
        print("Current status: Hyper-V is disabled")
    else:
        print("Error in output. Full output:")
        print(output.stdout)
    print("="*40)

def schedule_restart():
    global reboot_requested
    if reboot_requested == True:
        global time_before_reboot
        global planned_reboot
        print("Changes require a system reboot to take effect. Reboot now? [Y/N]")
        while(True):
            choice = input()
            if (choice.lower() == "n"):
                break
            elif (choice.lower() == "y"):
                planned_reboot = True
                subprocess.run("shutdown /r /t " + time_before_reboot)
                print("Reboot scheduled in " + time_before_reboot + " seconds")
                break
            else:
                print("Only Y and N are accepted")
        print("="*40)
    else:
        return

if __name__ == "__main__":
    main()
