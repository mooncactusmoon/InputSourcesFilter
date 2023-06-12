import tkinter as tk
from tkinter import ttk
import json

window = tk.Tk()
window.title("Input Sources Filter")
window.minsize(500, 500)
window.maxsize(600, 600)

def get_json(file_name):
    with open(file_name, encoding="utf-8") as f:
        data = json.load(f)
        return data

errMessage = tk.StringVar()
errMessage.set('')
input_sources_data = get_json("test_input_sources.json")
deviceList = list(input_sources_data.keys())

selectTitle = tk.Label(window, font=30, text="【請選擇要比較的裝置 Please select the devices】").grid(row=0, columnspan=3)
deviceMenu1 = ttk.Combobox(values=deviceList)
deviceMenu2 = ttk.Combobox(values=deviceList)
deviceMenu1.grid(row=2, column=1)
deviceMenu2.grid(row=2, column=2)

errText = tk.Label(window, font=20, textvariable=errMessage, fg='red').grid(row=1, columnspan=2)

def check_devices(device1, device2):
    if device1 == '' or device2 == '':
        return '請不要空白'
    if device1 == device2:
        return '請不要選同一台裝置'
    if device1 not in deviceList:
        return '找不到目標機器 : ' + device1
    if device2 not in deviceList:
        return '找不到目標機器 : ' + device2

    return True


def button_event():
    errMessage.set('')
    device1 = deviceMenu1.get()
    device2 = deviceMenu2.get()
    tk_check = check_devices(device1, device2)
    if tk_check == True:
        get_result(device1, device2)
    else:
        err_Message(tk_check)

def get_result(device1 ,device2):
    device1_value = input_sources_data[device1]
    device2_value = input_sources_data[device2]
    print(f"{device1} => {device1_value}")
    print(f"{device2} => {device2_value}")
    commen_values = set(device1_value) & set(device2_value)
    print(commen_values)
    tk.Label(window, font=30, text=device1).grid(row=5, column=0)
    for value in device1_value:
        if value not in commen_values:
            tk.Label(window, font=20, text=value, fg='red').grid(column=0)
            print(f"{device1}的{value}是獨特的")
        else:
            tk.Label(window, font=20, text=value).grid(column=0)
            print(f"{device1}和其他機器都有{value}")

    tk.Label(window, font=40, text="------", fg="blue").grid(column=0)
    tk.Label(window, font=30, text=device2).grid(column=0)
    for value in device2_value:
        if value not in commen_values:
            tk.Label(window, font=20, text=value, fg='red').grid(column=0)
            print(f"{device2}的{value}是獨特的")
        else:
            tk.Label(window, font=20, text=value).grid(column=0)
            print(f"{device2}和其他機器都有{value}")
    

def err_Message(err):
    errMessage.set(err)

subBtn = tk.Button(window, text="submit", command=button_event)
subBtn.grid(row=4, columnspan=4, pady=5)

window.mainloop()
