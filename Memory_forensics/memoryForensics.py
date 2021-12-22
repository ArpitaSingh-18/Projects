import os
memoryImageLocation = "C:\\Users\\Arpita.S.K.Singh_18\\Desktop\\Mini\\memdump.mem"
currentDirectory = os.getcwd()
command = "python " + currentDirectory + "\\volatility3\\vol.py -f " + memoryImageLocation



def collectDump():
    """
    This will open the FTK Imager application, take memory dump
    """
    os.startfile("C:\\Program Files\\AccessData\\FTK Imager\\FTK Imager.exe")


def downloadVolatility():
    os.system('cmd /c git clone https://github.com/volatilityfoundation/volatility3.git')
    os.system('cmd /c "pip3 install -r "' + currentDirectory + '"\\volatility3\\requirements.txt"')


def processList(memoryImageLocation):
    print("Listing all processes that were being executed at the time of memory dump and saving them into an excel file:- ")
    os.system('cmd /c ' + command + ' windows.pslist > ' + currentDirectory + '\\processList.xls')
    os.system('cmd /c ' + command + ' windows.pslist')


def processListTree(memoryImageLocation):
    print("Listing all processes with parent-child relation and dumping it into an excel file :- ")
    os.system('cmd /c ' + command + ' windows.pstree > ' + currentDirectory + '\\processListTree.xls')
    os.system('cmd /c ' + command + ' windows.pstree')

def hiddenprocess(memoryImageLocation):
    print("Listing all the hidden and inactive process at the time of memory dump and saving it :- ")
    os.system('cmd /c ' + command + ' windows.psscan > ' + currentDirectory + '\\psScan.xls')
    os.system('cmd /c ' + command + ' windows.psscan')

def cmdline(memoryImageLocation):
    print("Listing all the commands that were being executed on command line and saving it into an excel file :- ")
    os.system('cmd /c ' + command + ' windows.cmdline > ' + currentDirectory + '\\commandLine.xls')
    os.system('cmd /c ' + command + ' windows.cmdline')


def dumpingProcess(memoryImageLocation):
    # Do this step if the dump is of this device and you think this process is malicious
    pid = input("Enter pid of the process to be dumped: - ")
    os.system('cmd /c ' + command + ' windows.pslist --pid ' + pid + ' --dump')


def networkConnections(memoryImageLocation):
    print("Listing al the Network Connections :- ")
    os.system('cmd /c ' + command + ' windows.netscan > ' + currentDirectory + '\\networkConnections.xls')
    os.system('cmd /c ' + command + ' windows.netscan')


def sids(memoryImageLocation):
    print("Listing all the security identifiers for checking privileges :- ")
    os.system('cmd /c ' + command + ' windows.getsids > ' + currentDirectory + '\\privilages.xls')
    os.system('cmd /c ' + command + ' windows.getsids')


def fileobjects(memoryImageLocation):
    print("Listing and saving File Scan :- ")
    os.system('cmd /c ' + command + ' windows.filescan > ' + currentDirectory + '\\fileScan.xls')
    os.system('cmd /c ' + command + ' windows.filescan')



if __name__ == "__main__":
    #collectDump()
    #downloadVolatility()

    while True:
        choice = int(input("\n---------------------------------------------------------------------------\n"
                           "\nSelect an option: - \n 1. Display and save process list"
                           "\n 2. Display and save process tree"
                           "\n 3. Display and save command line used "
                           "\n 4. Dump a process "
                           "\n 5. Display and list network connections"
                           "\n 6. Display and save security identifiers for checking privileges"
                           "\n 7. Display and save file objects present"
                           "\n 8. Display and save hidden and inactive processes"
                           "\n 9. Enter -1 for termination\n"
                           "\n---------------------------------------------------------------------------\n"
                           "\nYour choice :- "))
        if (choice == 1):
            processList(memoryImageLocation)
        elif (choice == 2):
            processListTree(memoryImageLocation)
        elif (choice == 3):
            cmdline(memoryImageLocation)
        elif (choice == 4):
            dumpingProcess(memoryImageLocation)
        elif (choice == 5):
            networkConnections(memoryImageLocation)
        elif (choice == 6):
            sids(memoryImageLocation)
        elif (choice == 7):
            fileobjects(memoryImageLocation)
        elif (choice == 8):
            hiddenprocess(memoryImageLocation)
        else:
            break
