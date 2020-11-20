import socket
import pyautogui
import threading
import time
from input_keys import ReleaseKey, PressKey, UP, DOWN, LEFT, RIGHT, SHIFT, ENTER, SPACEBAR
from pywinauto.findwindows import find_window
from win32gui import SetForegroundWindow

time.sleep(1)
SetForegroundWindow(find_window(title='Duskers'))
SERVER = "irc.twitch.tv"
PORT = 6667
PASS = "Twitch outh code"
BOT = "ENTER BOT NAME"
CHANNEL = "Channel name"
OWNER = "Owner aka your channel name"
message = ""
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send((  "PASS " + PASS + "\n" +
            "NICK " + BOT + "\n" +
            "JOIN #" + CHANNEL + "\n").encode())

def gameControl():
    global message
    while True:
        if '-forward' in message.lower():
            text = message.lower()
            text = text.replace('-forward', '')
            text = float(text)
            time.sleep(1)
            SetForegroundWindow(find_window(title='Duskers'))
            print(text)
            PressKey(SHIFT)
            PressKey(UP)
            time.sleep(float(text))
            ReleaseKey(UP)
            ReleaseKey(SHIFT)
            message = ""
            print("ARROW UP PRESSED")
        if '-up' in message.lower():
            text = message.lower()
            text = text.replace('-up', '')
            text = float(text)
            SetForegroundWindow(find_window(title='Duskers'))
            print(text)
            PressKey(SHIFT)
            PressKey(UP)
            time.sleep(float(text))
            ReleaseKey(UP)
            ReleaseKey(SHIFT)
            message = ""
            print("ARROW UP PRESSED")
        elif '-right' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            text = message.lower()
            text = text.replace('-right', '')
            text = float(text)
            print(text)
            PressKey(SHIFT)
            PressKey(RIGHT)
            time.sleep(text)
            ReleaseKey(RIGHT)
            ReleaseKey(SHIFT)
            message = ""
            print("ARROW RIGHT PRESSED")
        elif '-left' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            text = message.lower()
            text = text.replace('-left', '')
            text = float(text)
            print(text)
            PressKey(SHIFT)
            PressKey(LEFT)
            time.sleep(text)
            ReleaseKey(LEFT)
            ReleaseKey(SHIFT)
            message = ""
            print("ARROW left PRESSED")
        elif '-backward' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            text = message.lower()
            text = text.replace('-backward', '')
            text = float(text)
            print(text)
            PressKey(SHIFT)
            PressKey(DOWN)
            time.sleep(text)
            ReleaseKey(DOWN)
            ReleaseKey(SHIFT)
            message = ""
        elif '-down' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            text = message.lower()
            text = text.replace('-down', '')
            text = float(text)
            print(text)
            PressKey(SHIFT)
            PressKey(DOWN)
            time.sleep(text)
            ReleaseKey(DOWN)
            ReleaseKey(SHIFT)
            message = ""
        elif '-map' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            PressKey(SPACEBAR)
            time.sleep(0.5)
            PressKey(SPACEBAR)
            message = ""
            print("SPACEBAR PRESSED")
        elif '-w' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            text = message.lower()
            text = text.replace('-w ', '')
            pyautogui.write(text, interval=0.1)
            PressKey(ENTER)
            ReleaseKey(ENTER)
            message = ""
            print('WRITING ', text)
        elif '-write' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            text = message.lower()
            text = text.replace('-write ', '')
            pyautogui.write(text, interval=0.1)
            PressKey(ENTER)
            ReleaseKey(ENTER)
            message = ""
            print('WRITING ', text)
        elif '-enter' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            PressKey(ENTER)
            ReleaseKey(ENTER)
            message = ""
        elif '-write-nospace' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            text = message.lower()
            text = text.replace('-wn ', '')
            pyautogui.write(text, interval=0.25)
            message = ""
            print('WRITING-NOSPACE ', text)
        elif '-esc' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            pyautogui.press('esc')
            message = ""
            print('escape')
        elif '-b1' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            pyautogui.press('1')
            message = ""
            print('1')
        elif '-b2' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            pyautogui.press('2')
            message = ""
            print('2')
        elif '-b3' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            pyautogui.press('3')
            message = ""
            print('3')
        elif '-b4' in message.lower():
            SetForegroundWindow(find_window(title='Duskers'))
            pyautogui.press('4')
            message = ""
            print('4')
        else:
            pass

def twitch():
    def joinchat():
        Loading = True
        while Loading:
            readbuffer_join = irc.recv(1024)
            readbuffer_join = readbuffer_join.decode()
            for line in readbuffer_join.split("\n")[0:-1]:
                print(line)
                Loading = loadingComplete(line)
    def loadingComplete(line):
        if ("End of /NAMES list" in line):
            print("Bot has joined " + CHANNEL + "'s Channel!")
            sendMessage(irc, "Chat room Joined")
            return False
        else:
            return True
    def sendMessage(irc, message):
        messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
        irc.send((messageTemp + "\n").encode())
    def getUser(line):
        sepatrate = line.split(":", 2)
        user = sepatrate[1].split("!", 1)[0]
        return user
    def GetMessage(line):
        global message
        try:
            message = (line.split(":", 2))[2]
        except:
            message = ""
        return  message
    def Console(line):
        if "PRIVMSG #" in line:
            return False
        else:
            return True


    joinchat()

    while True:
        try:
            readbuffer =irc.recv(1024).decode()
        except:
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            elif "PING" in line and Console(line):
                msgg = "PONG tmi.twtich.tv\r\n". encode()
                irc.send(msgg)
                print(msgg)
                continue
            else:
                message = GetMessage(line)
                user = getUser(line)
                print("Received " + user + " : " + message)
if __name__ == '__main__':
    t1 = threading.Thread(target = twitch)
    t1.start()
    t2 = threading.Thread(target = gameControl)
    t2.start()