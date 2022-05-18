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
    print(Fore.GREEN+ "-Ports-"),
    print(Fore.GREEN+ "-Network-"),
    print(Fore.GREEN+ "-LAN-"),
    print(Fore.GREEN+ "-WLAN-"),
    #input: pick option.         #Character name.
    operation = input("Hello " + Name + ", Select an option to continue ")
    if operation == "Ports":    #If they type "Ports" it'll show Notes.
        #   os.system("cls") # unhash for windows OS
        os.system("clear")
        print("\nHi, " + Name + ", Here are the ports and what they are:\n")
        print("Port Definition: A computer port is a connection point or interface between a computer and an external or internal device.\n"
        "Internal ports may connect such devices as hard drives and CD ROM or DVD drives\n"
        "external ports may connect modems, printers, mice and other devices.\n")
        print(Fore.RED + "You can use Ports to find vulnerabilities to further exploit or to build reconnaissance.\n ")
        print("- Port: 22      / SSH is Secure Shell enables two computers to communicate ")
        print("- Port: 23      / TCP is telnet")
        print("- Port: 25      / SMTP is Simple Mail Transfer Protocol, E-mail routing")
        print("- Port: 21/21   / TCP is FTP (sftp for secure)")
        print("- Port: 21/21   / ")
        print("- Port: 53      / DNS is Domain Name System")
        print("- Port: 69      / TFTP is Trivial File Transfer Protocol. less secure and does not require authentication ")
        print("- Port: 445     / TCP is SMB operate (SMB: Server Message Block)")
        print("- port: 443     / HTTPS IS (Hypertext Transfer Protocol Secure)")
        print("- port: 80      / HTTP is (Hypertext Transfer Protocol)")
        print("- port: 3389    / TCP  It is typically used for Windows Remote Desktop Protocol (RDP)")
        print("- port: ")

    elif operation == "Network":    #If they type "Network" it'll show notes.
        #   os.system("cls") # unhash for windows OS
        os.system("clear")
        print(Fore.RED + "\nNetwork Definition: A group or system of interconnected people or things.")
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