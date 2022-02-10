#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           IMPORTS                                                                                         |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from tkinter.font import BOLD
from selenium import webdriver
from time import sleep
import datetime, time
import threading
from webdriver_manager.chrome import ChromeDriverManager
import os, sys
from PIL import Image

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           START WEBDRIVER                                                                                 |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PATH = "chromedriver.exe"  

# Zefoy
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.zefoy.com")

whatsapp = webdriver.Chrome(ChromeDriverManager().install())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           TikTok Bot                                                                                      |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def loop5(vidUrl, amount, botnumb, name, idx, failureRate = 0):  # comment likes
    canvas.itemconfig(status, text="Running")
    canvas.itemconfig(status, fill="#F3F330")
    print(len(taskList))
    sleep(20)
    # sendWhatsappImage()

    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
    except:
        failureRate = failureRate+1

        if (failureRate > 9):
            taskList.pop(idx-1)
            fillQueue()

        print("Problem: You didn't solve the captcha yet. Need to refresh to avoid endless loop")
        driver.refresh()
        loop5(vidUrl, amount, botnumb, name, idx, failureRate)
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
            percentValue = str(int(realAmount)/int(amount)*100)
            percentValue= percentValue[0:3]
            percentValue = percentValue.replace(".", "")
            print(str(realAmount)+" likes of "+ str(amount) + " likes on Video"+str(idx))
            print("%s: Comment Likes Sent ✓" % (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
            print("Time remaining: %s minutes" % ((int(amount)-int(realAmount))/25))
            canvas.itemconfig(belowStatus, text=str(realAmount)+" likes of "+ str(amount) + " likes on Video "+str(idx))
            decimalNumb= (int(amount)-int(realAmount))/25
            minutes = int(decimalNumb)
            seconds= int((decimalNumb-minutes)*60)
            canvas.itemconfig(belowStatus2, text="Time remaining: "+str(minutes)+" minutes and "+ str(seconds)+" seconds")
            print("")
            
            if(idx==1):  
                queue.itemconfig(e1_percent, text=percentValue+"%")
            elif(idx==2):
                queue.itemconfig(e2_percent, text=percentValue+"%")
            elif(idx==3):
                queue.itemconfig(e3_percent, text=percentValue+"%")
            elif(idx==4):
                queue.itemconfig(e4_percent, text=percentValue+"%")
            elif(idx==5):
                queue.itemconfig(e5_percent, text=percentValue+"%")
            elif(idx==6):
                queue.itemconfig(e6_percent, text=percentValue+"%")
            failureRate = 0   
            sleep(60)
            loop5(vidUrl, amount, botnumb, name, idx, failureRate)
        else:
            if(idx==1):  
                queue.itemconfig(e1_percent, text="100%")
            elif(idx==2):
                queue.itemconfig(e2_percent, text="100%")
            elif(idx==3):
                queue.itemconfig(e3_percent, text="100%")
            elif(idx==4):
                queue.itemconfig(e4_percent, text="100%")
            elif(idx==5):
                queue.itemconfig(e5_percent, text="100%")
            elif(idx==6):
                queue.itemconfig(e6_percent, text="100%")

            canvas.itemconfig(belowStatus, text="Finished with video "+str(idx)) 
            failureRate = 0

            if(idx-1>len(taskList)):
                canvas.itemconfig(status, text="Finished", fill="#49AF25")
                return

            setThread()
            idx = idx+1
            loop5(taskList[idx-1].get('link'), taskList[idx-1].get('likes'), 5, taskList[idx-1].get('name'), idx)

    except:
        print("Problem: Something went wrong.. Processing restart")
        failureRate = failureRate+1
        if (failureRate > 9):
            taskList.pop(idx-1)
            fillQueue()

        driver.refresh()
        sleep(5)
        loop5(vidUrl, amount, botnumb, name, idx, failureRate)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           Initial Code                                                                                    |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

linkArg = None
likesArg = None
accountArg = None
whatsappNotify = False
taskList = []
settedThread = threading.Thread(target= loop5, args=[linkArg, likesArg, 5, accountArg])
window = Tk()
window.title("AutoLiker v 1.0.0")
window.iconbitmap(os.path.join(sys.path[0], 'icon.ico'))
window.geometry("1152x686")
window.configure(bg = "#FFFFFF")
        


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           TKINTER INTERFACE                                                                               |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           FINCTIONS                                                                                       |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def setLink():
    global linkArg
    linkArg = linkEntry.get()

def toggleWhatsapp():
    global whatsappNotify
    if(whatsappNotify == False):
        button_10.configure(image=button_image_5_activated)
        whatsappNotify = True
        whatsapp.get("https://web.whatsapp.com/")
    else:
        button_10.configure(image=button_image_5)
        whatsappNotify = False
        whatsapp.quit() 

def setLikes():
    global likesArg
    likesArg = int(likeEntry.get())

def setAccount():
    global accountArg
    accountArg = accountEntry.get()

def setThread():
    global settedThread
    settedThread = threading.Thread(target= loop5, args=[taskList[0].get('link'), taskList[0].get('likes'), 5, taskList[0].get('name'), 1])

def addTaskList():
    taskList.append({'link': linkArg,'likes': likesArg,'bot': 5,'name': accountArg})

def getAttributes():
    print(accountArg, linkArg, likesArg)

# def sendWhatsappImage():
#     if(driver.find_element_by_class_name("card")):
#         driver.save_screenshot("C:/Users/louis/OneDrive/Dokumente/Repos/TikTokBotNew/screenshots/ss.png")
#         whatsapp.find_element_by_xpath('//*[@title="TikTokBot"]').click()
#         sleep(2)
#         attachement_box= whatsapp.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")
#         attachement_box.click()
#         sleep(1)
#         image_box = whatsapp.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input")
#         image_box.send_keys("C:/Users/louis/OneDrive/Dokumente/Repos/TikTokBotNew/screenshots/ss.png")
#         sleep(1)
#         send_button = whatsapp.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]/div/div")
#         send_button.click()
#         sleep(1)
#         whatsapp.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys("Send CAPTCHA Code here:")
#         sleep(1)
#         whatsapp.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button").click()
#         sleep(1)
#         driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/div/div/div/div/button").click
#         elementsList = whatsapp.find_elements_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[3]/div")
#         lastElement = elementsList[-1].find_element_by_xpath("/div/div/div/div/div/span/span").get_attribute("innerHTML")
#         print(lastElement)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           TKINTER INTERFACE                                                                               |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def fillQueue(index = 1):
    for x in taskList:
        if(index==1):
            queue.itemconfig(e1_link, text= x.get("link"))
            queue.itemconfig(e1_text, text= x.get("name"))
        elif(index==2):
            queue.itemconfig(e2_link, text= x.get("link"))
            queue.itemconfig(e2_text, text= x.get("name")) 
        elif(index==3):
            queue.itemconfig(e3_link, text= x.get("link"))
            queue.itemconfig(e3_text, text= x.get("name"))       
        elif(index==4):
            queue.itemconfig(e4_link, text= x.get("link"))
            queue.itemconfig(e4_text, text= x.get("name"))  
        elif(index==5):
            queue.itemconfig(e5_link, text= x.get("link"))
            queue.itemconfig(e5_text, text= x.get("name"))  
        elif(index==6):
            queue.itemconfig(e6_link, text= x.get("link"))
            queue.itemconfig(e6_text, text= x.get("name"))  
        if(index<6):
            print(taskList[index-1], x)
            index = index+1
        else:
            return

def removeQueue():
            queue.itemconfig(e6_link, text="")
            queue.itemconfig(e6_text, text="")
            queue.itemconfig(e5_link, text="")
            queue.itemconfig(e5_text, text="")
            queue.itemconfig(e4_link, text="")
            queue.itemconfig(e4_text, text="")
            queue.itemconfig(e3_link, text="")
            queue.itemconfig(e3_text, text="")
            queue.itemconfig(e2_link, text="")
            queue.itemconfig(e2_text, text="")
            queue.itemconfig(e1_link, text="")
            queue.itemconfig(e1_text, text="")
                    


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
    outline=""
    )

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
    command=lambda: [setLikes(), setLink(), setAccount(), addTaskList(), setThread(), getAttributes(), fillQueue()],
    relief="flat"
)
button_1.place(
    x=710.0,
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
    x=640.0,
    y=594.0,
    width=101.0,
    height=43.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))

button_image_4 = PhotoImage(
    file=relative_to_assets("button_41.png"))

button_image_5 = PhotoImage(
    file=relative_to_assets("button_10.png")
)
button_image_5_activated = PhotoImage(
    file=relative_to_assets("button_10_activated.png")
)

button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [settedThread.join(), canvas.itemconfig(status, text="Inactive"), canvas.itemconfig(status, fill="#AF2626")],
    relief="flat"
)
button_3.place(
    x=790.0,
    y=594.0,
    width=101.0,
    height=43.0
)
canvas.create_text(
    700.0,
    303.0,
    anchor="nw",
    text="Queue:",
    fill="#B0B0B0",
    font=("ReadexPro Regular", 40 * -1)
)

queue = Canvas(
    height=210,
    width=600,
    bg="#3D3D3D",
    highlightthickness=0,
    relief = "ridge"
)
queue.place(
    x= 465,
    y=360
)

canvas.create_text(
    135.0,
    134.0,
    anchor="nw",
    text="Status:",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 36 * -1)
)
canvas.create_text(
    28.0,
    500.0,
    anchor="nw",
    text="Wanna activate Whatsapp Notification?",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 18 * -1)
)
button_10 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [toggleWhatsapp()],
    relief="flat"
)
button_10.place(
    x=160.0,
    y=535.0,
    width=50.0,
    height=50.0
)
status = canvas.create_text(
    146.0,
    180.0,
    anchor="nw",
    text="Inactive",
    fill="#AF2626",
    font=("ReadexPro Regular", 24 * -1)
)
belowStatus = canvas.create_text(
    70.0,
    210.0,
    anchor="nw",
    text="",
    fill="#888888",
    font=("ReadexPro Regular", 18 * -1)
)
belowStatus2 = canvas.create_text(
    70.0,
    230.0,
    anchor="nw",
    text="",
    fill="#888888",
    font=("ReadexPro Regular", 14 * -1)
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

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           GENERATED QUEUE COMPONENT                                                                       |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

queue.create_rectangle(
    7.0,
    7.0,
    300.0,
    71.0,
    fill="#454545",
    outline="")

queue.create_rectangle(
    7.0,
    71.0,
    300.0,
    138.0,
    fill="#4B4B4B",
    outline="")

queue.create_rectangle(
    7.0,
    138.0,
    300.0,
    202.0,
    fill="#454545",
    outline="")

queue.create_rectangle(
    300.0,
    7.0,
    593.0,
    71.0,
    fill="#4B4B4B",
    outline="")

queue.create_rectangle(
    300.0,
    71.0,
    593.0,
    138.0,
    fill="#454545",
    outline="")

queue.create_rectangle(
    300.0,
    138.0,
    593.0,
    202.0,
    fill="#4B4B4B",
    outline="")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           QUEUE ELEMENTS                                                                                  |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Element 1

e1_numb=queue.create_text(
    20.0,
    24.0,
    anchor="nw",
    text="1",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 24 * -1)
)
queue.create_text(
    53.0,
    11.0,
    anchor="nw",
    text="Link: ",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e1_link= queue.create_text(
    54.0,
    24.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
queue.create_text(
    53.0,
    39.0,
    anchor="nw",
    text="Included text:",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e1_text= queue.create_text(
    54.0,
    52.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
e1_percent= queue.create_text(
    254.0,
    29.0,
    anchor="nw",
    text="0%",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 18 * -1)
)
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [taskList.pop(0), removeQueue(), fillQueue()],
    relief="flat"
)
button_4.place(
    x=750.0,
    y=367.0,
    width=13.0,
    height=13.0
)
# Element 2

e2_numb= queue.create_text(
    20.0,
    89.0,
    anchor="nw",
    text="2",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 24 * -1)
)
queue.create_text(
    53.0,
    74.0,
    anchor="nw",
    text="Link: ",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e2_link= queue.create_text(
    55.0,
    87.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
queue.create_text(
    53.0,
    103.0,
    anchor="nw",
    text="Included text:",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e2_text= queue.create_text(
    55.0,
    120.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
e2_percent= queue.create_text(
    254.0,
    94.0,
    anchor="nw",
    text="0%",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 18 * -1)
)
button_5 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [taskList.pop(1), removeQueue(), fillQueue()],
    relief="flat"
)
button_5.place(
    x=751.0,
    y=431.0,
    width=13.0,
    height=13.0
)
# Element 3

e3_numb= queue.create_text(
    20.0,
    155.0,
    anchor="nw",
    text="3",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 24 * -1)
)
queue.create_text(
    53.0,
    142.0,
    anchor="nw",
    text="Link: ",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e3_link= queue.create_text(
    53.0,
    153.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
queue.create_text(
    53.0,
    169.0,
    anchor="nw",
    text="Included text:",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e3_text= queue.create_text(
    54.0,
    185.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
e3_percent= queue.create_text(
    254.0,
    159.0,
    anchor="nw",
    text="0%",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 18 * -1)
)
button_6 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [taskList.pop(2), removeQueue(), fillQueue()],
    relief="flat"
)
button_6.place(
    x=751.0,
    y=498.0,
    width=13.0,
    height=13.0
)
# Element 4

e4_numb= queue.create_text(
    313.0,
    24.0,
    anchor="nw",
    text="4",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 24 * -1)
)
queue.create_text(
    346.0,
    11.0,
    anchor="nw",
    text="Link: ",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)

e4_link= queue.create_text(
    347.0,
    24.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
queue.create_text(
    346.0,
    38.0,
    anchor="nw",
    text="Included text:",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)

e4_text= queue.create_text(
    347.0,
    52.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
e4_percent= queue.create_text(
    547.0,
    29.0,
    anchor="nw",
    text="0%",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 18 * -1)
)
button_7 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [taskList.pop(3), removeQueue(), fillQueue()],
    relief="flat"
)
button_7.place(
    x=1045.0,
    y=367.0,
    width=13.0,
    height=13.0
)
# Element 5

e5_numb= queue.create_text(
    313.0,
    90.0,
    anchor="nw",
    text="5",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 24 * -1)
)

queue.create_text(
    346.0,
    75.0,
    anchor="nw",
    text="Link: ",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e5_link= queue.create_text(
    347.0,
    88.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
queue.create_text(
    346.0,
    103.0,
    anchor="nw",
    text="Included text:",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e5_text= queue.create_text(
    347.0,
    117.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
e5_percent= queue.create_text(
    547.0,
    94.0,
    anchor="nw",
    text="0%",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 18 * -1)
)
button_8 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [taskList.pop(4), removeQueue(), fillQueue()],
    relief="flat"
)
button_8.place(
    x=1045.0,
    y=432.0,
    width=13.0,
    height=13.0
)
# Element 6

e6_numb= queue.create_text(
    313.0,
    155.0,
    anchor="nw",
    text="6",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 24 * -1)
)
queue.create_text(
    346.0,
    143.0,
    anchor="nw",
    text="Link: ",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e6_link= queue.create_text(
    347.0,
    154.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
queue.create_text(
    346.0,
    169.0,
    anchor="nw",
    text="Included text:",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 10, BOLD)
)
e6_text= queue.create_text(
    347.0,
    182.0,
    anchor="nw",
    text="",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 12 * -1)
)
e6_percent= queue.create_text(
    547.0,
    159.0,
    anchor="nw",
    text="0%",
    fill="#A5A5A5",
    font=("ReadexPro Regular", 18 * -1)
)
button_9 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: [taskList.pop(5), removeQueue(), fillQueue()],
    relief="flat"
)
button_9.place(
    x=1045.0,
    y=497.0,
    width=13.0,
    height=13.0
)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                           START WINDOW LOOP                                                                               |
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

window.resizable(False, False)
window.mainloop()



 


