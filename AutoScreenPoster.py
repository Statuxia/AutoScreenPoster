from tkinter import Tk, Button, Entry, Text, INSERT, DISABLED, NORMAL, END
from keyboard import is_pressed
from PIL import ImageGrab
from io import BytesIO
from requests import put
from pyperclip import copy
from winsound import Beep

global themenow
themenow = False


def copyy():
    txt.clipboard_clear()
    txt.clipboard_append(txt.get(1.0, END)[:-1])


def delete():
    txt.config(state=NORMAL)
    txt.delete('1.0', END)
    txt.config(state=DISABLED)

def show(event):
    if event.keysym != "Return":
        if str(window.focus_get()) == ".!entry":
            lenn = len(window.focus_get().get())
            window.focus_get().delete(0, lenn)
            if "_L" in event.keysym and event.keysym[-1] == "L":
                window.focus_get().insert(1, event.keysym[0:-2])
            elif "_R" in event.keysym and event.keysym[-1] == "R":
                window.focus_get().insert(1, event.keysym[0:-2])
            else:
                window.focus_get().insert(1, event.keysym)


def theme():
    global themenow
    if not themenow:
        themenow = True
        window.configure(bg="#FFFFFF")
        buttontheme.configure(text=u"\uE708", bg="#FFFFFF", fg="#000000")
        hotkey.configure(bg="#FFFFFF", fg="#000000")
        txt.configure(bg="#FFFFFF", fg="#000000", font=("Arial", 10, "bold"))
        hotkeyconfirm.configure(bg="#FFFFFF", fg="#000000")
        copyt.configure(bg="#FFFFFF", fg="#000000")
        clear.configure(bg="#FFFFFF", fg="#000000")
    else:
        themenow = False
        window.configure(bg="#1A202C")
        buttontheme.configure(text=u"\uE706", bg="#1A202C", fg="#EDEDEE")
        hotkey.configure(bg="#1A202C", fg="#FFFFFF")
        txt.configure(bg="#1A202C", fg="#FFFFFF", font=("Arial", 10, "bold"))
        hotkeyconfirm.configure(bg="#1A202C", fg="#FFFFFF")
        copyt.configure(bg="#1A202C", fg="#FFFFFF")
        clear.configure(bg="#1A202C", fg="#FFFFFF")


def clicked():
    if is_pressed(hotkey.get()):
        main = ImageGrab.grab()
        raw_image = BytesIO()
        main.save(raw_image, format='PNG')

        res = put("https://image.vimetools.cf/upload", data=raw_image.getvalue(),
                  headers={"user-agent": "Vime Tools"},
                  timeout=10000)
        copy(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
        txt.config(state=NORMAL)
        txt.insert(INSERT, f"https://image.vimetools.cf/get/{str(res.content)[2:-1]} \n")
        txt.config(state=DISABLED)
        Beep(300, 100)
        Beep(200, 50)
    window.after(50, clicked)


window = Tk()
window.title("AutoScreenPoster")
window.geometry("300x286")
window.resizable(width=False, height=False)
window.configure(bg="#1A202C")
window.bind_all("<Key>", show)
try:
    window.iconbitmap("icon.ico")
except:
    pass

hotkey = Entry(window, width=17)
hotkey.place(x=10, y=12)
hotkey.insert("end", "Нажмите клавишу")
hotkey.configure(bg="#1A202C", fg="#FFFFFF", font=("Arial", 10, "bold"))
hotkeyconfirm = Button(window, text="Подтвердить", command=clicked, font=("Arial", 10, "bold"))
hotkeyconfirm.place(x=140, y=10)
hotkeyconfirm.configure(bg="#1A202C", fg="#FFFFFF")

txt = Text(window, width=40, height=10)
txt.place(x=10, y=60)
txt.configure(bg="#1A202C", fg="#FFFFFF", font=("Arial", 10, "bold"))
txt.config(state=DISABLED)

buttontheme = Button(window, text=u"\uE706", command=theme, font=("Arial", 18, "bold"))
buttontheme.place(x=256, y=10)
buttontheme.configure(bg="#1A202C", fg="#FFFFFF", highlightthickness=0, bd=0)

copyt = Button(window, text="Скопировать", command=copyy)
copyt.place(x=10, y=230, width=130, height=50)
copyt.configure(bg="#1A202C", fg="#FFFFFF", font=("Arial", 10, "bold"))

clear = Button(window, text="Очистить", command=delete)
clear.place(x=195, y=230, width=100, height=50)
clear.configure(bg="#1A202C", fg="#FFFFFF", font=("Arial", 10, "bold"))

window.mainloop()
