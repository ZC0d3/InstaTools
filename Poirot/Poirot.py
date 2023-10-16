"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92

Poirot is a Python script used to extract information from Instagram accounts.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print(f"[!] Error ! Poirot requires Python version 3.X ! ")
        sleep(2)
        print(f"""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print(f"[*] Please install Python 3 and then use Poirot ✅")
        sleep(2)
        print(f"[+] Exiting...")
        sleep(1)
        quit()
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ['sys', 'time', 'rich', 'platform', 'os', 'requests', 'json', 'prettytable', 'colorama']
    with console.status('[bold dark_orange]Loading module...') as status:
        for mod in mods:
            sleep(0.8)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]okay')
    import platform
    import json
    import requests
    import os
    from os import system
    from colorama import init, Fore
except ImportError or ModuleNotFoundError:
    print(f"[!] WARNING: Not all packages used in Poirot have been installed !")
    sleep(2)
    print(f"[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print(f"[!] Root user not detected !")
            sleep(2)
            print(f"[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print(f"[!] Error ! Cannot install the required modules !")
                sleep(1)
                print(f"[=] Error message ==> {ex}")
                sleep(2)
                print(f"[1] Uninstall Poirot")
                print(f"[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2:
                    print(f"[!] Invalid number !")
                    sleep(1)
                    print(f"[+] Acceptable numbers: [1/2]")
                    sleep(2)
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))
                        return None
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(fpath('InstaTools'))
                    print(f"[✓] Files and dependencies uninstalled successfully !")
                else:
                    print(f"[+] Exiting...")
                    sleep(1)
                    print(f"[+] See you next time 👋")
                    quit()
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW

sleep(0.8)
console.clear()
console.log("[bold green][✓] Successfully loaded modules ![/]")
sleep(1)

def checkUser(username:str) -> bool:
    return username in ['' , ' '] or len(username) > 30

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    fp = True if not fpath(f) == None else False
    fsize = 0 if fp else os.stat(fpath(f)).st_size
    print(f"{YELLOW}[+] Author: {conf['author']}")
    print(f"{YELLOW}[+] Contributors : {conf['contributors']}")
    print(f"{YELLOW}[+] Github: @{conf['author']}")
    print(f"{YELLOW}[+] Leetcode: @{conf['author']}")
    print(f"{YELLOW}[+] PyPI: @{conf['author']}")
    print(f"{YELLOW}[+] License: {conf['lice']}")
    print(f"{YELLOW}[+] Natural language: {conf['lang']}")
    print(f"{YELLOW}[+] Programming language(s) used: {conf['language']}")
    print(f"{YELLOW}[+] Number of lines: {conf['lines']}")
    print(f"{YELLOW}[+] Script's name: {conf['name']}")
    print(f"{YELLOW}[+] API(s) used: {conf['api']}")
    print(f"{YELLOW}[+] Latest update: {conf['update']}")
    print(f"{YELLOW}[+] File size: {fsize} bytes")
    print(f"{YELLOW}[+] File path: {fpath(f)}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Stars: {conf['stars']}")
    print(f"{YELLOW}[+] Forks: {conf['forks']}")
    print(f"{YELLOW}[+] Open issues: {conf['issues']}")
    print(f"{YELLOW}[+] Closed issues: {conf['clissues']}")
    print(f"{YELLOW}[+] Open pull requests: {conf['prs']}")
    print(f"{YELLOW}[+] Closed pull requests: {conf['clprs']}")
    print(f"{YELLOW}[+] Discussions: {conf['discs']}")

console = Console()
table = Table(show_footer=False)
centered = Align.center(table)

def banner() -> str:
    console.print("""[bold yellow]
               _               _   
              (_)             | |  
 _ __    ___   _  _ __   ___  | |_ 
| '_ \  / _ \ | || '__| / _ \ | __|
| |_) || (_) || || |   | (_) || |_ 
| .__/  \___/ |_||_|    \___/  \__|
| |
|_|
""")

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f'{GREEN}[✓] Files and dependencies uninstalled successfully !'

ANS = ['yes', 'no']

TABLE = [
    [
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://new92.github.io/[/]"
    ],
    [
        "[b white]Github[/]: [i light_green]@new92[/]",
        "[green]https://github.com/new92[/]"
    ],
    [
        "[b white]Leetcode[/]: [i light_green]@new92[/]",
        "[green]https://leetcode.com/new92[/]"
    ],
    [
        "[b white]PyPI[/]: [i light_green]@new92[/]",
        "[green]https://pypi.org/user/new92[/]"
    ]
]

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

def fetch(username: str):
    request = requests.get(f'https://www.instagram.com/{username}/?__a=1&__d=dis')
    js = request.json()
    if request.status_code == 200:
        return {
            'bio': js['graphql']['user']['biography'],
            'links': [js['graphql']['user']['bio_links'][i]['url'] for i in range(len(js['graphql']['user']['bio_links']))],
            'fb': js['graphql']['user']['fb_profile_biolink'],
            'users': [js['graphql']['user']['biography_with_entities']['entities'][i]['user']['username'] for i in range(len(js['graphql']['user']['biography_with_entities']['entities'])) if js['graphql']['user']['biography_with_entities']['entities'][i]['user'] != None],
            'hashtags': [js['graphql']['user']['biography_with_entities']['entities'][i]['hashtag']['name'] for i in range(len(js['graphql']['user']['biography_with_entities']['entities'])) if js['graphql']['user']['biography_with_entities']['entities'][i]['hashtag'] != None],
            'followers': js['graphql']['user']['edge_followed_by']['count'],
            'followings': js['graphql']['user']['edge_follow']['count'],
            'fbid': js['graphql']['user']['fbid'],
            'name': js['graphql']['user']['full_name'],
            'id': js['graphql']['user']['id'],
            'hide': js['graphql']['user']['hide_like_and_view_counts'],
            'business': js['graphql']['user']['is_business_account'],
            'professional': js['graphql']['user']['is_professional_account'],
            'supervision': js['graphql']['user']['is_supervision_enabled'],
            'join': js['graphql']['user']['is_joined_recently'],
            'email': js['graphql']['user']['business_email'],
            'tel': js['graphql']['user']['business_phone_number'],
            'private': js['graphql']['user']['is_private'],
            'verified': js['graphql']['user']['is_verified'],
            'pic': js['graphql']['user']['profile_pic_url_hd']
        }
    else:
        return js['message']
    
def main():
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] Poirot is a python script for extracting info from a user's Instagram account.[/]")
    print("\n")
    console.print("[bold yellow][1] Initiate Poirot[/]")
    console.print("[bold yellow][2] Show Poirot's info[/]")
    console.print("[bold yellow][3] Clear log[/]")
    console.print("[bold yellow][4] Uninstall Poirot[/]")
    console.print("[bold yellow][5] Exit[/]")
    print("\n")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 5:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1-5]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        sleep(1)
        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
        sleep(1)
        keep=str(input(f"{YELLOW}[?] Keep log ? "))
        while keep.lower() not in ANS or keep in ['', ' ']:
            if keep in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [yes/no]")
            sleep(1)
            keep=str(input(f"{YELLOW}[?] Keep log ? "))
        keep = True if keep.lower() == ANS[0] else False
        sleep(1.2)
        clear()
        username=str(input(f"{YELLOW}[>] Please enter the target username: "))
        while checkUser(username):
            if username in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid length !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable length: 30 or less characters")
            sleep(1)
            username=str(input(f"{YELLOW}[>] Please enter again the target username: "))
        while valUser(username):
            print(f"{RED}[!] User not found !")
            sleep(1)
            print(f"{YELLOW}[1] Try with another username")
            print(f"{YELLOW}[2] Return to menu")
            print(f"{YELLOW}[3] Exit")
            opt=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1-3]")
                sleep(2)
                opt=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input(f"{YELLOW}[>] Please enter the target username: "))
                while checkUser(username):
                    if username in ['', ' ']:
                        print(f"{RED}[!] This field can't be blank !")
                    else:
                        print(f"{RED}[!] Invalid length !")
                        sleep(1)
                        print(f"{GREEN}[+] Acceptable length: 30 or less characters")
                    sleep(1)
                    username=str(input(f"{YELLOW}[>] Please enter again the target username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print(f"{RED}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] See you next time 👋")
                sleep(2)
                quit()
        username = username.lower().strip()
        sleep(1.2)
        name = 'poirotLog.txt'
        print(f"{GREEN}[+] Username -> OK")
        sleep(1.3)
        print(f"{GREEN}[+] Extracting info...")
        sleep(1.3)
        dict = fetch(username)
        if type(dict) != str:
            sleep(1.3)
            print(f"{GREEN}[✓] Success !")
            sleep(1.1)
            print("\n")
            print(f"{GREEN}---------------" + '-' * len(username))
            print(f"{GREEN}[>] Username | {username}")
            print(f"{GREEN}[>] Name | {dict['name']}")
            print(f"{GREEN}[>] Bio | {dict['bio']}")
            print(f"{GREEN}[>] Followers | {dict['followers']}")
            print(f"{GREEN}[>] Followings | {dict['followings']}")
            print(f"{GREEN}[>] Email | {dict['email']}")
            print(f"{GREEN}[>] Tel | {dict['tel']}")
            print(f"{GREEN}[>] Profile pic | {dict['pic']}")
            print(f"{GREEN}[>] ID | {dict['id']}")
            print(f"{GREEN}[>] External links | {dict['links']}")
            print(f"{GREEN}[>] Users in bio | {dict['users']}")
            print(f"{GREEN}[>] Hashtags in bio | {dict['hashtags']}")
            print(f"{GREEN}[>] fb | {dict['fb']}")
            print(f"{GREEN}[>] fb ID | {dict['fbid']}")
            print(f"{GREEN}[>] Joined recently | {dict['join']}")
            print(f"{GREEN}[>] Private | {dict['private']}")
            print(f"{GREEN}[>] Verified | {dict['verified']}")
            print(f"{GREEN}[>] Business | {dict['business']}")
            print(f"{GREEN}[>] Professional | {dict['professional']}")
            print(f"{GREEN}[>] Supervised | {dict['supervision']}")
            print(f"{GREEN}[>] Hide likes & views | {dict['hide']}")
            print(f"{GREEN}-------------------------" + '-' * len(str(dict['hide'])))
            sleep(3)
            if keep:
                with open(name, 'w', encoding='utf8') as f:
                    f.write('---------------' + '-' * len(username))
                    f.write(dict)
                    f.write("\n-------------------------" + '-' * len(str(dict['hide'])))
                    print("\n")
                    print(f"{YELLOW}[✓] Successfully saved log !")
                    sleep(1)
                    print(f"{YELLOW}[↪] File name: {name}")
                    print(f"{YELLOW}[↪] Location: {fpath(name)}")
                    print(f"{YELLOW}[↪] File size: {os.stat(fpath(name)).st_size} bytes")
        else:
            print(f"{RED}[✕] Information fetch unsuccessfull !")
            sleep(2)
            print(f"{GREEN}[+] Error message => {dict}")
            sleep(2)

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(4)
        print("\n\n")

    elif num == 3:
        clear()
        name = 'poirotLog.txt'
        if os.path.exists(fpath(name)):
            f = open(name,"w")
            f.close()
            print(f"{GREEN}[✓] Successfully cleared log !")
            sleep(1)
            print(f"{GREEN}[↪] File name: {name}")
            print(f"{GREEN}[↪] Location: {fpath(name)}")
            print(f"{GREEN}[↪] Size: 0 bytes")
            sleep(3)
        else:
            clear()
            print(f"{RED}[✕] Log file not found on this device !")
            sleep(2)
            print(f"{YELLOW}[+] Searched log file using name: {name}")
            sleep(2)
            print(f"{GREEN}[*] Please first create the log file and then use this option 😀")
            sleep(2)
            print(f"""{YELLOW}[+] Instructions: 
            1) Return to menu and enter the option number 1
            2) Enter <True> in the keep log question
            """)
            sleep(3)
    
    elif num == 4:
        clear() 
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for choosing Poirot 😀😁")
        sleep(2)
        print(f"{GREEN}[+] Hope you enjoyed it 🤗")
        sleep(1)
        print(f"{YELLOW}[+] If you have any suggestions or found a bug or need help feel free to contact me anytime, at this email address: new92github@gmail.com  or via Github")
        sleep(3)
        print(f"{GREEN}[+] Until we meet again 🫡")
        sleep(1)
        quit()

    else:
        clear()
        print(f"{YELLOW}[+] Thank you for using IGFollowersIncreaser 😁")
        sleep(2)
        print(f"{YELLOW}[+] See you next time 👋")
        sleep(1)
        quit()
    
    print("\n\n")
    print(f"{YELLOW}[1] Return to menu")
    print(f"{YELLOW}[2] Exit")
    opt=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
    while opt < 1 or opt > 2:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1/2]")
        sleep(2)
        opt=int(input(f"{YELLOW}[>] Please enter again a number (from the above ones): "))
    if opt == 1:
        clear()
        main()
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Poirot 😁")
        sleep(2)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(1)
        quit()

if __name__ == '__main__':
    sleep(2)
    clear()
    main()
