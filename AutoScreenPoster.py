from os import getlogin, listdir
from pyperclip import copy
from imgurpython import ImgurClient
from keyboard import is_pressed
from time import time
from winsound import Beep
login = getlogin()
screenshots = fr"C:\Users\{login}\AppData\Roaming\.vimeworld\minigames\screenshots"
log = fr"C:\Users\{login}\AppData\Roaming\.vimeworld\minigames\logs\latest.log"
client_id = 'you_imgur_client_id'
client_secret = 'you_imgur_secret_id'
client = ImgurClient(client_id, client_secret)
while True:
    try:
        if is_pressed("F2"):
            screen_true = False
            start_time = time()
            while not screen_true:
                f = open(log, 'r')
                all_lines = f.readlines()
                for i in range(1, 3):
                    if "Снимок экрана сохранён как" in all_lines[i * -1]:
                        screen_true = True
                f.close()
            path = fr"{screenshots}\{listdir(screenshots)[-1]}"
            items = client.upload_from_path(path, config=None, anon=True)
            copy(items["link"])
            Beep(300, 100)
            Beep(200, 50)
    except:
        continue
