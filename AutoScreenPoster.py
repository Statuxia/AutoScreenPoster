from os import getlogin, listdir
from pyperclip import copy
from requests import put
from io import BytesIO
from PIL import Image
from keyboard import wait
from winsound import Beep

login = getlogin()
screenshots = fr"C:\Users\{login}\AppData\Roaming\.vimeworld\minigames\screenshots"
url = "https://image.vimetools.cf/upload"
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
    path = fr"{screenshots}\{listdir(screenshots)[-1]}"
    ready = False
    while not ready:
        try:
            main = Image.open(path)
            raw_image = BytesIO()
            main.save(raw_image, format='PNG')
            ready = True
        except:
            ready = False
    res = put(url, data=raw_image.getvalue(), headers={"user-agent": "Vime Tools"},
              timeout=10000)
    copy(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
    print(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
    total_screens = len(listdir(screenshots))
    Beep(300, 100)
    Beep(200, 50)
