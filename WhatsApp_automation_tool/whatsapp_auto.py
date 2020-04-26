import sys
import tkinter as tk
from tkinter import filedialog
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import xlrd


def show_message():
    print("message ", e1.get())
    return e1.get()


def show_column():
    return e2.get()


def select_file():
    global path1
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")))
    print(root.filename)
    tk.Label(root, text="Path:  " + root.filename).place(x=10, y=100)

    path1 = root.filename


def select_file1():
    global path2
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=[("all files", "*.*")])
    print(root.filename)
    tk.Label(root, text="Path:  " + root.filename).place(x=10, y=220)
    path2 = root.filename


def element_presence(driver, by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except:
        is_connected()


def send_whatsapp_msg(driver, phone_no, text, is_attachment):
    global path2

    count = 0
    while count < 20:
        count += 1
        try:
            driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
            element_presence(driver, By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
            txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            break
        except:
            print('except')
            try:
                element = driver.find_element_by_class_name("_3lLzD").text
                if element == "Phone number shared via url is invalid.":
                    print("invalid Number")
                    return
            except:
                print('', end='')
                # Do nothing
        sleep(3)

    txt_box.send_keys(text)
    txt_box.send_keys("\n")

    if is_attachment:
        clipButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
        clipButton.click()
        driver.find_element_by_css_selector("input[type='file']").send_keys(path2)
        sleep(4)
        whatsapp_send_button = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
        whatsapp_send_button.click()
        sleep(1)
        print("clicked")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def process_phone_number(number_list):
    for i in range(0, len(number_list)):
        try:
            if number_list[i].index(".") > 0:
                temp = len(number_list[i]) - number_list[i].index(".")
                number_list[i] = number_list[i][:len(number_list[i]) - temp]
        except:
            print("Except in number check")

    for i in range(0, len(number_list)):
        if len(number_list[i]) == 14 and number_list[i][0] == number_list[i][2] == '9' and number_list[i][1] == number_list[i][3] == '1':
            number_list.remove(number_list[i])


def start():
    global path1
    global path2

    message_text = show_message()  # message you want to send
    try:
        attach_path = path2
        if attach_path == '':
            is_attachment = False
        else:
            is_attachment = True
    except:
        is_attachment = False

    loc = path1
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    moblie_no_list = []
    col = int(show_column())
    for i in range(0, sheet.nrows):
        if sheet.cell_value(i, col) == "":
            continue
        moblie_no_list.append("91" + str(sheet.cell_value(i, col)))
    driver = webdriver.Chrome(executable_path=resource_path("chromedriver.exe"))
    # driver.get("http://web.whatsapp.com")
    # sleep(10)  # wait time to scan the code in second

    driver.get("http://web.whatsapp.com")
    temp_flag = True
    while True:
        try:
            element = driver.find_element_by_class_name("landing-title").text
            while True:
                try:
                    element = driver.find_element_by_class_name("landing-title").text
                except:
                    temp_flag = False
                    print("inner except")
                    break
        except:
            if not temp_flag:
                break
            print("outer except")
            continue

    process_phone_number(moblie_no_list)
    sleep(3)

    for moblie_no in moblie_no_list:
        if len(moblie_no) != 12:
            print(len(moblie_no), 'continued', moblie_no)
            continue
        try:
            send_whatsapp_msg(driver, moblie_no, message_text, is_attachment)

        except Exception as e:
            sleep(10)
            print("main exception")
            is_connected()


root = tk.Tk()
root.geometry("500x500")
tk.Label(root, text="Whatsapp", fg="red", font="Verdana 20 bold").place(x=200, y=10)
tk.Label(root, text="Select path for the excel file containing phone numbers  ").place(x=10, y=60)
tk.Label(root, text="Enter the message ").place(x=10, y=140)
tk.Label(root, text="Select file to attach (if required) ").place(x=10, y=190)
tk.Label(root, text="Scan the QR code with your mobile ").place(x=300, y=350)
tk.Label(root, text="Column number containing phone numbers ").place(x=10, y=280)
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e2.place(x=300, y=280)
e1.place(x=200, y=145)
tk.Button(root, text=" Select file ", command=select_file).place(x=350, y=60)
tk.Button(root, text=" select file ", command=select_file1).place(x=350, y=190)
tk.Button(root, text=" Send Message ", command=start).place(x=200, y=350)
root.mainloop()
