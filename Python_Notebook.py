import os
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

Name = input("Hello there, what name would you like to be called? ")
#   os.system("cls") # unhash for windows OS
os.system("clear")
# Allowing user to make a name.
while True:     #Loop back to this point (Beginning).
    #Options.
    print("\033[1;39;40m " + "-Ports-"),
    print("-Network-"),
    print("-LAN-"),
    print("-WLAN-"),
    #input: pick option.         #Character name.
    operation = input("Hello " + Name + ", Select an option to continue ")
    if operation == "Ports":    #If they type "Ports" it'll show Notes.
        #   os.system("cls") # unhash for windows OS
        os.system("clear")
        print("\nHi, " + Name + ", Here are the ports and what they are:\n")
        print("Port Definition: A computer port is a connection point or interface between a computer and an external or internal device.\n"
        "Internal ports may connect such devices as hard drives and CD ROM or DVD drives\n"
        "external ports may connect modems, printers, mice and other devices.\n")
        print("You can use Ports to find vulnerabilities to further exploit or to build reconnaissance.\n ")
        print("- Port: 23   / TCP is telnet")
        print("- Port: 21   / TCP is FTP (sftp for secure)")
        print("- Port: 445  / TCP is SMB operate (SMB: Server Message Block)")
        print("- port: 80   / HTTP is (Hypertext Transfer Protocol)")
        print("- port: 3389 / TCP  It is typically used for Windows Remote Desktop Protocol (RDP)")

    elif operation == "Network":    #If they type "Network" it'll show notes.
        #   os.system("cls") # unhash for windows OS
        os.system("clear")
        print("\nNetwork Definition: A group or system of interconnected people or things.")
        print("\nNetwork Topologies:\n There are 8 different Net Topologies (Listed Below)")
       
        Topology = """ 
        Point-To-Point
        Bus Topology 
        Star Topology
        Ring Topology
        Mesh Topology
        Tree Topology
        Daisy Chain
        Hybrid Topology"""
        print(Topology) #Makes words ontop of eachother
#      "!=" will not let it execute if not typed exactly like "Ports"
    if operation != "Ports" and operation != "Network" and operation != "LAN" and operation != "WLAN":
        print("\nNo No.... Pick one of the options please. they're case sensitive. (^_^)")
        #"No No" shows if they type anything other than options given

    check = input("\nDo you want to go to the main menu?\n y or n: ")
    if check.lower() == "y":
        #   os.system("cls") # unhash for windows OS
        os.system("clear") 
        continue   # from "check = input" down to "continue" allows loop back to "While true"
    print("Bye.")
    break 
            # "Break" stops the loop back from repeating itself