from os import getlogin, listdir
from io import BytesIO
from winsound import Beep
from PIL import Image, ImageGrab
from keyboard import wait, send
from pyperclip import copy
from requests import put, get
from time import sleep

version = ""
req = str(get("https://github.com/Statuxia/AutoScreenPoster").content)
req = req.split('<span class="css-truncate css-truncate-target text-bold mr-2" style="max-width: none;">')
for i in req[1]:
    if i != "<":
        version += i
    else:
        break

def Vime(hotkey, screenshots):
    while True:
        total_screens = len(listdir(screenshots))
        if hotkey == "F2":
            wait("F2")
        else:
            wait(hotkey)
            send("F2")
        new_screen = False
        while not new_screen:
            if total_screens >= len(listdir(screenshots)):
                sleep(.2)
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
        res = put("https://image.vimetools.cf/upload", data=raw_image.getvalue(), headers={"user-agent": "Vime Tools"},
                  timeout=10000)
        copy(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
        print(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
        Beep(300, 100)
        Beep(200, 50)

def Fast(hotkey):
    while True:
        wait(hotkey)
        main = ImageGrab.grab()
        raw_image = BytesIO()
        main.save(raw_image, format='PNG')

        res = put("https://image.vimetools.cf/upload", data=raw_image.getvalue(), headers={"user-agent": "Vime Tools"},
                  timeout=10000)
        copy(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
        print(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
        Beep(300, 100)
        Beep(200, 50)




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
             ╚═╝     ╚╝""")

if version == "V0.6":
    print("ASP V0.6\n")
else:
    print(f"You ASP version is too old, Download {version} version: https://github.com/Statuxia/AutoScreenPoster\n")

print("Как пользоваться: https://github.com/Statuxia/AutoScreenPoster/blob/main/README.md\n")

choose = input("""Выберите способ создания ссылки
Vime - создание ссылки через [F2] (будут провисания)
Fast - создание ссылки производя скриншот экрана.
Способ создания ссылки: """)

hotkey = input("\nВыберите клавишу создания скриншота [для Fast нет смысла использовать F2, если вы не меняли клавишу создания снимка экрана в настройках игры]: ")
if hotkey != "":
    print("Успешно.")
else:
    print("Клавиша не выбрана. Закрываю программу.")
    exit()
if choose == "Vime":
    login = getlogin()
    screenshots = fr"C:\Users\{login}\AppData\Roaming\.vimeworld\minigames\screenshots"
    pathh = input(f"""
Введите адрес папки со скриншотами
Если вы согласны с адресом {screenshots}, то можете нажать [Enter]
Путь до скриншотов: """)
    if pathh != "":
        screenshots = pathh
    print(f"Выбран путь {screenshots}")
    print(" ")
    Vime(hotkey, screenshots)
elif choose == "Fast":
    print(" ")
    Fast(hotkey)
else:
    print("\nНекорректный способ создания ссылки.")