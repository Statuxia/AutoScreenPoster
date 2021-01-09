from PyQt5 import QtWidgets, QtCore, QtGui
from os import getlogin, listdir
from io import BytesIO
from sys import exit
from winsound import Beep
from PIL import Image, ImageGrab
from keyboard import wait, send
from requests import get, put
from pyperclip import copy
from time import sleep

version = ""
req = str(get("https://github.com/Statuxia/AutoScreenPoster").content)
req = req.split('<span class="css-truncate css-truncate-target text-bold mr-2" style="max-width: none;">')
for i in req[1]:
    if i != "<":
        version += i
    else:
        break
login = getlogin()
screenshots = fr"C:\Users\{login}\AppData\Roaming\.vimeworld\minigames\screenshots"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 350)
        MainWindow.setMinimumSize(QtCore.QSize(1030, 350))
        MainWindow.setMaximumSize(QtCore.QSize(1030, 350))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #1A202C")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-6, -1, 1041, 411))
        self.tabWidget.setStyleSheet("color: #000000")
        self.tabWidget.setObjectName("tabWidget")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.frame = QtWidgets.QFrame(self.settings)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1041, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.AutoScreenPoster = QtWidgets.QLabel(self.frame)
        self.AutoScreenPoster.setGeometry(QtCore.QRect(15, 0, 548, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AutoScreenPoster.setFont(font)
        self.AutoScreenPoster.setStyleSheet("color: #EDEDEE")
        self.AutoScreenPoster.setObjectName("AutoScreenPoster")
        self.MadebyFQGM = QtWidgets.QLabel(self.frame)
        self.MadebyFQGM.setGeometry(QtCore.QRect(740, 270, 238, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.MadebyFQGM.setFont(font)
        self.MadebyFQGM.setStyleSheet("color: #BA1314")
        self.MadebyFQGM.setObjectName("MadebyFQGM")
        self.choosetext = QtWidgets.QLabel(self.frame)
        self.choosetext.setGeometry(QtCore.QRect(15, 100, 364, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.choosetext.setFont(font)
        self.choosetext.setStyleSheet("color: #EDEDEE")
        self.choosetext.setObjectName("choosetext")
        self.hotkeytext = QtWidgets.QLabel(self.frame)
        self.hotkeytext.setGeometry(QtCore.QRect(15, 158, 413, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.hotkeytext.setFont(font)
        self.hotkeytext.setStyleSheet("color: #EDEDEE")
        self.hotkeytext.setObjectName("hotkeytext")
        self.pathtext = QtWidgets.QLabel(self.frame)
        self.pathtext.setGeometry(QtCore.QRect(15, 220, 391, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pathtext.setFont(font)
        self.pathtext.setStyleSheet("color: #EDEDEE")
        self.pathtext.setObjectName("pathtext")
        self.choose = QtWidgets.QComboBox(self.frame)
        self.choose.setGeometry(QtCore.QRect(360, 90, 61, 51))
        self.choose.setStyleSheet("color: #EDEDEE")
        self.choose.setObjectName("choose")
        self.choose.addItem("")
        self.choose.addItem("")
        self.hotkey = QtWidgets.QKeySequenceEdit(self.frame)
        self.hotkey.setGeometry(QtCore.QRect(400, 160, 111, 24))
        self.hotkey.setAutoFillBackground(False)
        self.hotkey.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(9,11,15);\n"
"color: #EDEDEE")
        self.hotkey.setInputMethodHints(QtCore.Qt.ImhNone)
        self.hotkey.setKeySequence("")
        self.hotkey.setObjectName("hotkey")
        self.path = QtWidgets.QLineEdit(self.frame)
        self.path.setGeometry(QtCore.QRect(390, 223, 481, 22))
        self.path.setStyleSheet("color: #EDEDEE;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(9,11,15)\n"
"")
        self.path.setObjectName("path")
        self.version = QtWidgets.QLabel(self.frame)
        self.version.setGeometry(QtCore.QRect(570, 34, 435, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.version.setFont(font)
        self.version.setStyleSheet("color: #EDEDEE")
        self.version.setObjectName("version")
        self.button = QtWidgets.QPushButton(self.frame)
        self.button.setGeometry(QtCore.QRect(15, 260, 211, 41))
        self.button.setStyleSheet("color: #EDEDEE;\n"
"radius: 30")
        self.button.setObjectName("button")
        self.tabWidget.addTab(self.settings, "")
        self.screenshots = QtWidgets.QWidget()
        self.screenshots.setObjectName("screenshots")
        self.frame_2 = QtWidgets.QFrame(self.screenshots)
        self.frame_2.setGeometry(QtCore.QRect(-30, 0, 1071, 391))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(40, 10, 331, 301))
        self.textBrowser.setStyleSheet("color: #4777E6;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20;\n"
"border-color: rgb(9,11,15)\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(380, 10, 93, 28))
        self.pushButton.setStyleSheet("color: #EDEDEE")
        self.pushButton.setObjectName("pushButton")
        self.MadebyFQGM_2 = QtWidgets.QLabel(self.frame_2)
        self.MadebyFQGM_2.setGeometry(QtCore.QRect(770, 270, 242, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.MadebyFQGM_2.setFont(font)
        self.MadebyFQGM_2.setStyleSheet("color: #BA1314")
        self.MadebyFQGM_2.setObjectName("MadebyFQGM_2")
        self.tabWidget.addTab(self.screenshots, "")
        self.help = QtWidgets.QWidget()
        self.help.setObjectName("help")
        self.frame_3 = QtWidgets.QFrame(self.help)
        self.frame_3.setGeometry(QtCore.QRect(-20, 0, 1070, 391))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.mark = QtWidgets.QLabel(self.frame_3)
        self.mark.setGeometry(QtCore.QRect(470, 200, 585, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.mark.setFont(font)
        self.mark.setStyleSheet("color: #EDEDEE")
        self.mark.setObjectName("mark")
        self.vimetext = QtWidgets.QLabel(self.frame_3)
        self.vimetext.setGeometry(QtCore.QRect(530, 80, 59, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.vimetext.setFont(font)
        self.vimetext.setStyleSheet("color: #EDEDEE")
        self.vimetext.setObjectName("vimetext")
        self.fasthelp = QtWidgets.QLabel(self.frame_3)
        self.fasthelp.setGeometry(QtCore.QRect(780, 120, 247, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fasthelp.setFont(font)
        self.fasthelp.setStyleSheet("color: #EDEDEE")
        self.fasthelp.setObjectName("fasthelp")
        self.vimehelp = QtWidgets.QLabel(self.frame_3)
        self.vimehelp.setGeometry(QtCore.QRect(470, 110, 247, 87))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.vimehelp.setFont(font)
        self.vimehelp.setStyleSheet("color: #EDEDEE")
        self.vimehelp.setObjectName("vimehelp")
        self.programwork = QtWidgets.QLabel(self.frame_3)
        self.programwork.setGeometry(QtCore.QRect(640, 50, 235, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.programwork.setFont(font)
        self.programwork.setStyleSheet("color: #EDEDEE")
        self.programwork.setObjectName("programwork")
        self.texthelp = QtWidgets.QLabel(self.frame_3)
        self.texthelp.setGeometry(QtCore.QRect(462, 5, 137, 38))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.texthelp.setFont(font)
        self.texthelp.setStyleSheet("color: #EDEDEE")
        self.texthelp.setObjectName("texthelp")
        self.settingstext = QtWidgets.QLabel(self.frame_3)
        self.settingstext.setGeometry(QtCore.QRect(40, 90, 402, 175))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.settingstext.setFont(font)
        self.settingstext.setStyleSheet("color: #EDEDEE")
        self.settingstext.setObjectName("settingstext")
        self.settingshelp = QtWidgets.QLabel(self.frame_3)
        self.settingshelp.setGeometry(QtCore.QRect(140, 50, 129, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.settingshelp.setFont(font)
        self.settingshelp.setStyleSheet("color: #EDEDEE")
        self.settingshelp.setObjectName("settingshelp")
        self.fasttext = QtWidgets.QLabel(self.frame_3)
        self.fasttext.setGeometry(QtCore.QRect(870, 80, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.fasttext.setFont(font)
        self.fasttext.setStyleSheet("color: #EDEDEE")
        self.fasttext.setObjectName("fasttext")
        self.MadebyFQGM_3 = QtWidgets.QLabel(self.frame_3)
        self.MadebyFQGM_3.setGeometry(QtCore.QRect(760, 270, 238, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        self.MadebyFQGM_3.setFont(font)
        self.MadebyFQGM_3.setStyleSheet("color: #BA1314")
        self.MadebyFQGM_3.setObjectName("MadebyFQGM_3")
        self.tabWidget.addTab(self.help, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoScreenPoster"))
        self.AutoScreenPoster.setText(_translate("MainWindow", "AutoScreenPoster"))
        self.MadebyFQGM.setText(_translate("MainWindow", "Made by FQGM"))
        self.choosetext.setText(_translate("MainWindow", "Выберите способ создания ссылки"))
        self.hotkeytext.setText(_translate("MainWindow", "Нажмите клавишу для создания ссылки"))
        self.pathtext.setText(_translate("MainWindow", "Выберите папку VimeWorld (для Vime)"))
        self.choose.setItemText(0, _translate("MainWindow", "Vime"))
        self.choose.setItemText(1, _translate("MainWindow", "Fast"))
        self.path.setText(_translate("MainWindow", "Ошибка, не найден путь."))
        self.version.setText(_translate("MainWindow", "Ошибка, версия не найдена."))
        self.button.setText(_translate("MainWindow", "Запуск"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Настройки"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Очистить"))
        self.MadebyFQGM_2.setText(_translate("MainWindow", "Made by FQGM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.screenshots), _translate("MainWindow", "Скриншоты"))
        self.mark.setText(_translate("MainWindow", "Не рекомендуется нажимать другие клавиши в момент нажатия\n"
"выбранной клавиши, так как это может помешать работе программы."))
        self.vimetext.setText(_translate("MainWindow", "Vime"))
        self.fasthelp.setText(_translate("MainWindow", "1)Нажимаем клавишу\n"
"2)Заходим в \"Скриншоты\"\n"
"3)Копируем ссылку"))
        self.vimehelp.setText(_translate("MainWindow", "1)Заходим на VimeWorld\n"
"2)Нажимаем клавишу\n"
"3)Заходим в \"Скриншоты\"\n"
"4)Копируем ссылку"))
        self.programwork.setText(_translate("MainWindow", "Работа программы"))
        self.texthelp.setText(_translate("MainWindow", "Помощь"))
        self.settingstext.setText(_translate("MainWindow", "1)Выбираем способ создания скриншота \n"
"Vime - через скриншот вайма\n"
"Fast - через скриншот экрана\n"
"2)Выбираем клавишу по которой будет\n"
"производиться отправка скриншота.\n"
"3)Если вы выбрали Vime, то нужно указать\n"
"адрес папки со скриншотами вайма.\n"
"4)Нажимаем кнопку \"Запуск\""))
        self.settingshelp.setText(_translate("MainWindow", "Настройка"))
        self.fasttext.setText(_translate("MainWindow", "Fast"))
        self.MadebyFQGM_3.setText(_translate("MainWindow", "Made by FQGM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.help), _translate("MainWindow", "Помощь"))

class work(QtCore.QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow

    def run(self):
        while True:
            buttontext(QtCore.QCoreApplication.translate("MainWindow", f"Запуск ({hotkey})"))
            if choose == "Vime":
                while choose == "Vime":
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
                    res = put("https://image.vimetools.cf/upload", data=raw_image.getvalue(),
                              headers={"user-agent": "Vime Tools"},
                              timeout=10000)
                    copy(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
                    self.mainwindow.ui.textBrowser.append(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
                    Beep(300, 100)
                    Beep(200, 50)

            elif choose == "Fast":
                wait(hotkey)
                main = ImageGrab.grab()
                raw_image = BytesIO()
                main.save(raw_image, format='PNG')

                res = put("https://image.vimetools.cf/upload", data=raw_image.getvalue(),
                          headers={"user-agent": "Vime Tools"},
                          timeout=10000)
                copy(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
                self.mainwindow.ui.textBrowser.append(f"https://image.vimetools.cf/get/{str(res.content)[2:-1]}")
                Beep(300, 100)
                Beep(200, 50)


class mywindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('name.ico'))
        if version == "V0.6":
            self.ui.version.setText(QtCore.QCoreApplication.translate("MainWindow", version))
        else:
            self.ui.version.setText(QtCore.QCoreApplication.translate("MainWindow", version + " (OLD)"))
        self.ui.path.setText(QtCore.QCoreApplication.translate("MainWindow", screenshots))
        global buttontext
        buttontext = self.ui.button.setText
        self.ui.button.clicked.connect(self.main)
        self.ui.button.clicked.connect(self.start)
        self.ui.button = work(mainwindow=self)

    def start(self):
        self.ui.button.start()

    def main(self):
        global choose, hotkey, screenshots
        choose = self.ui.choose.currentText()
        hotkey = self.ui.hotkey.keySequence().toString(QtGui.QKeySequence.NativeText).split(", ")[0]
        screenshots = self.ui.path.text()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

exit(app.exec())