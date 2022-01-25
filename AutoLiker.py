
from asyncio import tasks
from pathlib import Path
from shutil import ExecError
from tkinter import END, VERTICAL, Tk, Canvas, Entry, Text, Button, PhotoImage, Scrollbar
import webbrowser
from flask import Flask, render_template, request
from selenium import webdriver
from time import sleep
import datetime, time
import threading
from webdriver_manager.chrome import ChromeDriverManager
import os, sys

PATH = "chromedriver.exe"  
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.zefoy.com")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           TikTok Bot                                                                                      |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def loop5(vidUrl, amount, botnumb, name):  # comment likes
    canvas.itemconfig(status, text="Active")
    canvas.itemconfig(status, fill="#49AF25")
    sleep(20)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
    except:
        print("Problem: You didn't solve the captcha yet. Need to refresh to avoid endless loop")
        driver.refresh()
        loop5(vidUrl, amount, botnumb, name)
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9r\"]/div/div/form/button").click()
        sleep(5)
        realAmount = driver.find_element_by_xpath("//*[contains(text(), '%s')]/following-sibling::div/span" % (name)).get_attribute("innerText")
        realAmount = realAmount.replace(",", "")
        if int(realAmount) < int(amount):
            driver.find_element_by_xpath("//*[contains(text(), '%s')]/following-sibling::button" % (name)).click()
            driver.refresh()
            print("")
            print(str(realAmount)+" likes of "+ str(amount) + " likes.")
            print("%s: Comment Likes Sent ✓" % (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
            print("Time remaining: %s minutes" % ((int(amount)-int(realAmount))/25))
            print("")
            sleep(60)
            loop5(vidUrl, amount, botnumb, name)
        else:
            print("✓✓✓ Your Amount of Likes were successfully reached ✓✓✓")
    except:
        print("Problem: Something went wrong.. Processing restart")
        driver.refresh()
        sleep(5)
        loop5(vidUrl, amount, botnumb, name)




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           TKINTER INTERFACE                                                                               |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

linkArg = None
likesArg = None
accountArg = None
taskList = []
settedThread = threading.Thread(target= loop5, args=[linkArg, likesArg, 5, accountArg])
window = Tk()
window.title("AutoLiker v 1.0.0")
window.iconbitmap(os.path.join(sys.path[0], 'icon.ico'))
window.geometry("1152x686")
window.configure(bg = "#FFFFFF")

def setLink():
    global linkArg
    linkArg = linkEntry.get()

def setLikes():
    global likesArg
    likesArg = int(likeEntry.get())

def setAccount():
    global accountArg
    accountArg = accountEntry.get()

def setThread():
    global settedThread
    settedThread = threading.Thread(target= loop5, args=[linkArg, likesArg, 5, accountArg])

def setTaskList():
    print("TaskList")

def getAttributes():
    print(accountArg, linkArg, likesArg)
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 686,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1152.0,
    686.0,
    fill="#2F2F2F",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    377.0,
    686.0,
    fill="#2C2C2C",
    outline="")

canvas.create_rectangle(
    563.0,
    27.0,
    894.0,
    83.0,
    fill="#3D3D3D",
    outline="")

canvas.create_text(
    571.0,
    32.0,
    anchor="nw",
    text="Link:",
    fill="#B0B0B0",
    font=("ReadexPro Regular", 18 * -1)
)

canvas.create_rectangle(
    563.0,
    106.0,
    894.0,
    162.0,
    fill="#3D3D3D",
    outline="")

canvas.create_text(
    571.0,
    111.0,
    anchor="nw",
    text="Included text:",
    fill="#B0B0B0",
    font=("ReadexPro Regular", 18 * -1)
)

canvas.create_rectangle(
    563.0,
    179.0,
    894.0,
    235.0,
    fill="#3D3D3D",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [setLikes(), setLink(), setAccount(), setTaskList(), setThread(), getAttributes()],
    relief="flat"
)
button_1.place(
    x=678.0,
    y=248.0,
    width=101.0,
    height=43.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: settedThread.start(),
    relief="flat"
)
button_2.place(
    x=592.0,
    y=594.0,
    width=101.0,
    height=43.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [settedThread.join(), canvas.itemconfig(status, text="Inactive"), canvas.itemconfig(status, fill="#AF2626")],
    relief="flat"
)
button_3.place(
    x=764.0,
    y=594.0,
    width=101.0,
    height=43.0
)

canvas.create_text(
    641.0,
    303.0,
    anchor="nw",
    text="Queue:",
    fill="#B0B0B0",
    font=("ReadexPro Regular", 40 * -1)
)

queue = canvas.create_rectangle(
    430.0,
    379.0,
    1038.0,
    566.0,
    fill="#3D3D3D",
    outline="",
)

canvas.create_text(
    110.0,
    134.0,
    anchor="nw",
    text="Status:",
    fill="#B0B0B0",
    font=("ReadexPro Regular", 36 * -1)
)

status = canvas.create_text(
    146.0,
    179.0,
    anchor="nw",
    text="Inactive",
    fill="#AF2626",
    font=("ReadexPro Regular", 24 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    377.0,
    106.0,
    fill="#252525",
    outline="")

canvas.create_text(
    35.0,
    27.0,
    anchor="nw",
    text="AutoLiker v 1.0.0",
    fill="#888888",
    font=("ReadexPro Regular", 40 * -1)
)

canvas.create_rectangle(
    26.0,
    236.0,
    351.0,
    637.0,
    fill="#3D3D3D",
    outline="")

canvas.create_text(
    571.0,
    184.0,
    anchor="nw",
    text="Amount of likes:",
    fill="#B0B0B0",
    font=("ReadexPro Regular", 18 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    733.5,
    218.5,
    image=entry_image_1
)
likeEntry = Entry(
    bd=0,
    bg="#3D3D3D",
    highlightthickness=0,
    fg="#888888",
    font=("ReadexPro Regular", 14 * -1)
)
likeEntry.place(
    x=576.0,
    y=207.0,
    width=315.0,
    height=21.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    728.5,
    145.5,
    image=entry_image_2
)
accountEntry = Entry(
    bd=0,
    bg="#3D3D3D",
    highlightthickness=0,
    fg="#888888",
    font=("ReadexPro Regular", 14 * -1)
)
accountEntry.place(
    x=571.0,
    y=134.0,
    width=315.0,
    height=21.0,
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    728.5,
    64.5,
    image=entry_image_3
)
linkEntry = Entry(
    bd=0,
    bg="#3D3D3D",
    highlightthickness=0,
    fg="#888888",
    font=("ReadexPro Regular", 14 * -1)
)
linkEntry.place(
    x=571.0,
    y=53.0,
    width=315.0,
    height=21.0
)
window.resizable(False, False)
window.mainloop()



 


