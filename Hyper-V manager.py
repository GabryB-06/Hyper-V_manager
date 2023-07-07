#import os
import subprocess
#import win32com.shell.shell as shell
from pyuac import main_requires_admin


#def exec(commands):
    #shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)

@main_requires_admin
def main():
    #print("Do stuff here that requires being run as an admin.")
    # The window will disappear as soon as the program exits!
    #input("Press enter to close the window. >")
    while(True):
        print("1 - Disattiva Hyper-V")
        print("2 - Attiva Hyper-V")
        print("3 - Stato attuale")
        print("4 - Chiusura")
        scelta = int(input())
        if (scelta == 1):
            print()
            #print("output prima scelta")
            #exec('bcdedit /set hypervisorlaunchtype off')
            #shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
            output = subprocess.run("bcdedit /set hypervisorlaunchtype off", capture_output=True, text=True)
            print(output.stdout)
            #output = subprocess.run(['runas', '/user:Administrator', "bcdedit /set hypervisorlaunchtype off"], capture_output=True, text=True)
            #print(output)
            #os.system("bcdedit /set hypervisorlaunchtype off")
            print()
        elif (scelta == 2):
            print()
            #print("output seconda scelta")
            output = subprocess.run("bcdedit /set hypervisorlaunchtype auto", capture_output=True, text=True)
            print(output.stdout)
            #exec('bcdedit /set hypervisorlaunchtype on')
            #os.system("bcdedit /set hypervisorlaunchtype auto")
            print()
        elif (scelta == 3):
            print()
            #print("output terza scelta")
            output = subprocess.run("bcdedit /enum {current}", capture_output=True, text=True)
            print(output.stdout)
            #exec('bcdedit /enum {current}')
            #os.system("bcdedit /enum {current}")
            print()
        elif (scelta == 4):
            exit()
        else:
            print()
            print("Scelta non valida")
            print()

if __name__ == "__main__":
    main()