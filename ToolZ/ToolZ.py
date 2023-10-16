"""
Author: new92
Contributors: [Itsfizziks]
Github: @new92
Leetcode: @new92

ToolZ: Python script for keeping track on the users which unfollowed you.

*********IMPORTANT*********
User's login credentials (such as: username, password) will not be stored or saved ! 
Will be used only for the purpose of this script.
***************************
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! ToolZ requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[*] Please install Python 3 and then use ToolZ ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ['sys', 'time', 'rich', 'platform', 'os', 'json', 'datetime','requests', 'colorama']
    with console.status('[bold dark_orange]Loading module...') as status:
        for mod in mods:
            sleep(0.8)
            console.log(f'[[bold red]{mod}[/]] => [bold dark_green]okay')
    import platform
    from os import system
    import os
    import json
    import instaloader
    import requests
    from colorama import init, Fore
    from datetime import datetime
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in ToolZ have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Error ! Cannot install the required modules !")
                sleep(1)
                print(f"[*] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall ToolZ")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall ToolZ")
                    print("[2] Exit")
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
                    print("[✓] Files and dependencies uninstalled successfully !")
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    quit(0)
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
console.print("[bold dark_green][✓] Successfully loaded modules.")
sleep(0.8)
console.clear()

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def checkUser(username: str) -> bool:
    return len(username) > 30 or username in ['', ' ']

def valUser(username: str) -> bool:
    return requests.get(f'https://www.instagram.com/{username}/', allow_redirects=False).status_code != 200

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

def clear():
    system('cls') if platform.system() == 'Windows' else system('clear')

def validate(path: str) -> bool:
    return os.path.exists(path)

TABLE = [
    [
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://github.com/new92[/]"
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

console = Console()
table = Table(show_footer=False)
centered = Align.center(table)

def extract(raw_path: str):
    index = raw_path.find('session-')
    return raw_path[index + len('session-'):] if index != -1 else None 

def ScriptInfo():
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    fp = True if not fpath(f) == None else False
    fsize = 0 if not fp else os.stat(fpath(f)).st_size
    print(f"{YELLOW}[+] Author: {conf['author']}")
    print(f"{YELLOW}[+] Contributors: {conf['contributors']}")
    print(f"{YELLOW}[+] Github: @{conf['author']}")
    print(f"{YELLOW}[+] Leetcode: @{conf['author']}")
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

ANS = ['yes', 'no']

def logo() -> str:
    return f"""{YELLOW}
         tttt                                            lllllll
      ttt:::t                                            l:::::l
      t:::::t                                            l:::::l
      t:::::t                                            l:::::l
ttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l zzzzzzzzzzzzzzzzz
t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l z:::::::::::::::z
t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l z::::::::::::::z 
tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l zzzzzzzz::::::z  
      t:::::t          o::::o     o::::oo::::o     o::::o l::::l       z::::::z   
      t:::::t          o::::o     o::::oo::::o     o::::o l::::l      z::::::z    
      t:::::t          o::::o     o::::oo::::o     o::::o l::::l     z::::::z     
      t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l    z::::::z      
      t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::l  z::::::zzzzzzzz
      tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::l z::::::::::::::z
        tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::lz:::::::::::::::z
          ttttttttttt     ooooooooooo      ooooooooooo   llllllllzzzzzzzzzzzzzzzzz
    """


def main():
    table = Table(show_footer=False)
    print(logo())
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    print(f"{YELLOW}[+] ToolZ: Python tool which keeps track on the users who unfollowed you on Instagram.")
    print("\n")
    print(f"{YELLOW}[1] Initiate ToolZ")
    print(f"{YELLOW}[2] Display ToolZ's info")
    print(f"{YELLOW}[3] Clear log file")
    print(f"{YELLOW}[4] Uninstall ToolZ")
    print(f"{YELLOW}[5] Exit")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 5:
        print(f"{RED}[!] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers: [1-5]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        print(f"{GREEN}[+] Acceptable answers: [yes/no]")
        sleep(1)
        con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
        while con.lower() not in ANS or con in ['', ' ']:
            if con in ['', ' ']:
                print(f"{RED}[!] This field can't be blank !")
            else:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [yes/no]")
            sleep(1)
            con=str(input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? "))
        if con.lower() == ANS[0]:
            with open('cons.txt', 'a', encoding='utf8') as f:
                f.write(f"\n[=] Date: {datetime.now()}\n")
                f.write("[=] User: Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
                f.write("-"*40)
        else:
            print(f"{YELLOW}[OK]")
            sleep(1)
            print(f"{YELLOW}[1] Exit")
            print(f"{YELLOW}[2] Uninstall ToolZ and exit")
            num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
            valErr = num in [1,2]
            while not valErr:
                try:
                    print(f"{YELLOW}[1] Exit")
                    print(f"{YELLOW}[2] Uninstall ToolZ and exit")
                    sleep(1)
                    num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                    valErr = num in [1,2]
                except ValueError:
                    print(f"{RED}[!] Please enter a valid number.")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable numbers: [1,2]")
                    sleep(1)
            if num == 1:
                clear()
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                quit(0)
            else:
                clear()
                print(Uninstall())
                sleep(2)
                print(f"{YELLOW}[+] Exiting...")
                sleep(1)
                print(f"{YELLOW}[+] Thank you for using ToolZ 🫡")
                sleep(2)
                print(f"{YELLOW}[+] Until we meet again 👋")
                sleep(1)
                quit(0)
        sleep(1)
        print(f'{GREEN}|---------------|LOGIN|---------------|')
        session=str(input(f"{YELLOW}[::] Please enter the cookie file path: "))
        session = session.lower().strip()
        sleep(0.5)
        print(f"{YELLOW}Using session file: {session}")
        sleep(1)
        while not validate(session):
            print(f"{RED}[!] Invalid file path !")
            sleep(1)
            session=str(input(f"{YELLOW}[::] Please enter again the cookie file path: "))
        username = extract(session)
        sleep(0.5)
        print(f"{YELLOW}[+] Extracted username: {username}...")
        sleep(1)
        print(f"{GREEN}[+] Using session file: {session}...")
        sleep(2)
        try: 
            with open(session, 'rb') as sessionfile:
                loader.context.load_session_from_file(username, sessionfile)
                print(f"{GREEN}[✓] Session loaded successfully !")
                sleep(1)
        except instaloader.exceptions.ConnectionException as ex:
            print(f"{RED}[✕] Error loading session file !")
            sleep(1)
            print(f"{YELLOW}[+] Error message: {ex}")
            sleep(2)
            print(f"{YELLOW}[+] Exiting...")
            quit(0)
        profile = None
        try:
            profile = instaloader.Profile.from_username(loader.context, username)
        except instaloader.ProfileNotExistsException:
            print(f"{RED}[!] Profile not found")
            sleep(1)
            print(f"{YELLOW}[+] Exiting...")
            quit(0)

        if profile:
            name = 'ToolZ_Log.txt'
            print(f"{GREEN}[✓] Login successfull !")
            sleep(1)
            print(f'{YELLOW}[+] User ID: {profile.userid}')
            print(f'{YELLOW}[+] Full name: {profile.full_name}')
            sleep(2)
            print(f"{GREEN}[*] Initiating ToolZ...")
            sleep(2)
            print(f"{YELLOW}[*] Acceptable answers: [yes/no]")
            sleep(1)
            kp=str(input(f"{YELLOW}[?] Keep log ? "))
            while kp.lower() not in ANS or kp in ['', ' ']:
                print(f"{RED}[!] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers: [yes/no]")
                sleep(2)
                kp=str(input(f"{YELLOW}[?] Keep log ? "))
            kp = True if kp.lower() == ANS[0] else False
            if kp:
                f = open(name, 'w')
            profile = instaloader.Profile.from_username(loader.context, username)
            FOLLOWERS = [follower.username for follower in profile.get_followers()]
            FOLLOWINGS = [following.username for following in profile.get_followees()]
            sleep(2)
            clear()
            print(f"{YELLOW}[1] Live tracker")
            print(f"{YELLOW}[2] One-time tracker")
            opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 2:
                print(f"{RED}[!] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers: [1/2]")
                sleep(1)
                opt=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
            if opt == 1:
                UNFOLLOWERS = []
                while len(FOLLOWERS) == len(FOLLOWINGS):
                    print(f"{YELLOW}[*] Checking for unfollowers...")
                    sleep(5)
                    profile = instaloader.Profile.from_username(loader.context, username)
                    FOLLOWERS = [follower.username for follower in profile.get_followers()]
                    FOLLOWINGS = [following.username for following in profile.get_followees()]
                    print(f"{GREEN}[+] No unfollowers found...")
                    sleep(5)
                    print(f"{YELLOW}[*] Sleeping for 20 secs before checking again...")
                    sleep(20)
                for i in range(len(FOLLOWINGS)):
                    verProf = instaloader.Profile.from_username(loader.context, FOLLOWINGS[i])
                    if FOLLOWINGS[i] not in FOLLOWERS and not verProf.is_verified:
                        UNFOLLOWERS.append(FOLLOWINGS[i])
                if kp:
                    f.write(f"[&] Detected a total of {len(UNFOLLOWERS)} unfollowers\n\n")
                    f.write("-"*25+'\n\n')
                    for i in range(len(UNFOLLOWERS)):
                        f.write(f"[>] Username >>> {UNFOLLOWERS[i]}\n")
                    sleep(1)
                    print(f"{GREEN}[✓] Successfully saved log !")
                    sleep(2)
                    print(f"{YELLOW}[↪] Name: {name}")
                    print(f"{YELLOW}[↪] Location: {fpath(name)}")
                    print(f"{YELLOW}[↪] Size: {os.stat(fpath(name)).st_size} bytes")
                    sleep(3)
                sleep(5)
                print(f"{GREEN}[+] Captured a total of {len(UNFOLLOWERS)} unfollowers.")
                sleep(2)
                print(f'{YELLOW}|--------|USERNAMES|--------|')
                sleep(0.75)
                for i in range(len(UNFOLLOWERS)):
                    print(f"{YELLOW}[>] Username >>> {UNFOLLOWERS[i]}")
            else:
                if len(FOLLOWERS) == len(FOLLOWINGS):
                    print(f"{YELLOW}[+] No unfollowers found !")
                else:
                    L = []
                    for i in range(len(FOLLOWINGS)):
                        verProf = instaloader.Profile.from_username(loader.context, FOLLOWINGS[i])
                        if FOLLOWINGS[i] not in FOLLOWERS and not verProf.is_verified:
                            L.append(FOLLOWINGS[i])
                    print(f"{GREEN}[✓] OK")
                    sleep(2)
                    print(f"{YELLOW}[+] Found a total of: {len(L)} unfollowers")
                    sleep(1)
                    print(f"{YELLOW}[+] Usernames: ")
                    print("\n")
                    for i in range(len(L)):
                        print(f"{YELLOW}[>] Username{i+1} >>> {L[i]}")
                    sleep(2)
                    if kp:
                        f.write(f"[&] Detected a total of {len(L)} unfollowers\n\n")
                        f.write("-"*25+'\n\n')
                        for i in range(len(L)):
                            f.write(f"[>] Username >>> {L[i]}\n")
                        f.close()
                        sleep(1)
                        print(f"{GREEN}[✓] Successfully saved log !")
                        sleep(2)
                        print(f"{YELLOW}[↪] Name: {name}")
                        print(f"{YELLOW}[↪] Location: {fpath(name)}")
                        print(f"{YELLOW}[↪] Size: {os.stat(fpath(name)).st_size} bytes")
                        sleep(3)
        elif num == 2:
            clear()
            ScriptInfo()
            print("\n\n")
            sleep(5)
        elif num == 3:
            clear()
            f = open(name,'w')
            f.close()
            print(f"{GREEN}[✓] Successfully cleared log file !")
            sleep(2)
        elif num == 4:
            clear()
            print(Uninstall())
            sleep(2)
            print(f"{GREEN}[+] Thank you for using ToolZ 😁")
            sleep(2)
            print(f"{GREEN}[+] Until next time 🫡")
            sleep(1)
            quit(0)
        else:
            clear()
            print(f"{GREEN}[+] Thank you for using ToolZ 😁")
            sleep(2)
            print(f"{GREEN}[+] See you next time 👋")
            sleep(1)
            quit(0)
        print(f"{YELLOW}[1] Back to menu")
        print(f"{YELLOW}[2] Exit")
        num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        while num < 1 or num > 2:
            print(f"{RED}[!] Invalid number !")
            sleep(1)
            num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones): "))
        if num == 1:
            clear()
            main()
        else:
            print(f"{GREEN}[+] Thank you for using ToolZ 😃")
            sleep(2)
            print(f"{GREEN}[+] Until next time 🤗")
            sleep(1)
            print(f"{YELLOW}[+] Exiting...")
            quit(0)

    if __name__ == '__main__':
        main()
