import tkinter as tk
from tkinter import ttk,Frame
import json

window = tk.Tk()
window.title("Input Sources Filter")
window.geometry('700x650')

def get_json(file_name):
    with open(file_name, encoding="utf-8") as f:
        data = json.load(f)
        return data

errMessage = tk.StringVar()
errMessage.set('')
input_sources_data = get_json("test_input_sources.json")
deviceList = list(input_sources_data['individual_deivce'][0])
all_input_sources = list(input_sources_data['all_input_sources'])

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
        clear_event()
        get_result(device1, device2)
    else:
        err_Message(tk_check)

def get_result(device1 ,device2):
    device1_value = input_sources_data['individual_deivce'][0][device1]
    device2_value = input_sources_data['individual_deivce'][0][device2]
    commen_values = set(device1_value) & set(device2_value)
    union_values = set(device1_value).union(set(device2_value))

    create_frame('frame1', 5, 0, device1, commen_values, device1_value)
    create_frame('frame2', 5, 1, device2, commen_values, device2_value)
    create_frame('frame3', 5, 2, "所有訊號源\n(紅字為兩台裝置都沒有的)", union_values, all_input_sources)

def create_frame(frame, ro, col, device_name, compare_arr, target_arr):
    frame = tk.LabelFrame(window, padx=2, pady=2)
    tk.Label(frame, font=40, text=device_name, fg='blue').grid()
    for value in target_arr:
        if value not in compare_arr:
            tk.Label(frame, font=20, text=value, fg='red').grid()
        else:
            tk.Label(frame, font=20, text=value, fg='grey').grid()
    frame.grid(row=ro, column=col)

def err_Message(err):
    errMessage.set(err)

def clear_event():
    frame1 = tk.LabelFrame(window, padx=2, pady=2)
    tk.Label(frame1).grid()
    frame1.grid(row=5,sticky=tk.N+tk.S+tk.W+tk.E,columnspan=3)


subBtn = tk.Button(window, text="submit", command=button_event)
subBtn.grid(row=4, columnspan=4, pady=5)

window.mainloop()
