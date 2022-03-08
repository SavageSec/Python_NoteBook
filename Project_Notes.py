Name = input("Hello there, what name would you like to be called? ")
# Name = input()
while True:

    print("-Ports-"),
    print("-Network-"),
    print("-LAN-"),
    print("-WLAN-"),

    operation = input("Hello " + Name + ", Select an option to continue ")
    if operation == "Ports":
        print("\nHi " + Name + ", Here are the ports and what they are:\n"
                               "\nyou can use Ports to find vulnerabilities "
                               "to further exploit or to build reconnaissance.\n ")
        print("- Port: 23   / TCP is telnet")
        print("- Port: 21   / TCP is FTP (sftp for secure)")
        print("- Port: 445  / TCP is SMB operate (SMB: Server Message Block)")
        print("- port: 80   / HTTP is (Hypertext Transfer Protocol)")
        print("- port: 3389 / TCP  It is typically used for Windows Remote Desktop Protocol (RDP)")

    elif operation == "Network":
        print("")

    if operation != "Ports" and operation != "Network":
        print("\nNo No.... Pick one of the options please. they're case sensitive. (^_^)")

    check = input("\nDo you want to go to the main menu?\n y or n: ")
    if check == "y":
        continue
    print("Bye.")
    break
