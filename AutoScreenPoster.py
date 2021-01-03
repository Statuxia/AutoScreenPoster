from os import getlogin, listdir
from pyperclip import copy
from imgurpython import ImgurClient
from keyboard import wait
from time import sleep
from winsound import Beep
login = getlogin()
screenshots = fr"C:\Users\{login}\AppData\Roaming\.vimeworld\minigames\screenshots"
client_id = 'you_imgur_client_id'
client_secret = 'you_imgur_secret_id'
client = ImgurClient(client_id, client_secret)
print("""

 █████╗     ██████╗   ██████╗    
██╔══██╗   ██╔════╝   ██╔══██╗   
███████║   ╚█████╗    ██████╔╝   
██╔══██║    ╚═══██╗   ██╔═══╝    
██║  ██║██╗██████╔╝██╗██║
╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝╚═╝

       ╔╗  ╔╗   ╔══╦══╦══╦═╦═╗
╔══╦═╗╔╝╠═╗║╚╦╦╗║═╦╣╔╗║╔═╣║║║║
║║║║╬╚╣╬║╩╣║╬║║║║╔╝║╚╝║╚╗║║║║║
╚╩╩╩══╩═╩═╝╚═╬╗║╚╝ ╚═╗╠══╩╩═╩╝
             ╚═╝     ╚╝
""")

print("""Как пользоваться:
Заходите на VimeWorld;
Нажимаете F2;
Ждете...
Получаете ссылку на ваш скриншот.
""")
pathh = input(f"Путь до скриншотов: {screenshots}\n"
             f"Введите адрес, где хранятся скриншоты (Enter, если согласны с адресом выше):")
if pathh != "":
    screenshots = pathh
print(f"Выбран путь {screenshots}\n")

total_screens = len(listdir(screenshots))
while True:
    wait("F2")
    new_screen = False
    while not new_screen:
        if total_screens >= len(listdir(screenshots)):
            continue
        else:
            new_screen = True
            total_screens = len(listdir(screenshots))
            path = fr"{screenshots}\{listdir(screenshots)[-1]}"
            sleep(1)
            items = client.upload_from_path(path, config=None, anon=True)
            copy(items["link"])
            print(items["link"])
            Beep(300, 100)
            Beep(200, 50)
