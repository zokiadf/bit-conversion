import tkinter as tk
from tkinter import ttk
from tkinter import font


def decimal_to_bin(decimal_num):
    bin_num = ""
    while decimal_num > 0:
        remainer = decimal_num % 2
        bin_num = str(remainer) + bin_num
        decimal_num = decimal_num // 2
    return bin_num
        
def decimal_to_octal(decimal_num):
    octal_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_num = str(remainder) + octal_num
        decimal_num = decimal_num // 8
    return octal_num

def decimal_to_hex (decimal_num):
    hex_chars = "0123456789ABCDEF"
    hex_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_num = hex_chars[remainder] + hex_num
        decimal_num = decimal_num // 16
    return hex_num
def convert_base():
    decimal_num = int(entry1.get())
    target_base = int(basebox.get())
    
    if target_base == 2:
        result = decimal_to_bin(decimal_num)
    elif target_base == 8:
        result = decimal_to_octal(decimal_num)
    elif target_base == 16:
        result = decimal_to_hex(decimal_num)
    else:
        result = str(decimal_num)
    label_result.config(text="{} 轉換成 {} 進位 為 {}".format(decimal_num, target_base, result))

window = tk.Tk()
window.title("轉換器")
window.minsize(width=600,height=800)
window.resizable(width=False,height=False)

label1 = tk.Label(window,text='轉換器')

entry_font = font.Font(size=13)

#選擇輸入的位元以及值
chosebox = ttk.Combobox(window, values=[2,8,10,16],state = 'readonly')
chosebox.set(10) 
entry1 = tk.Entry(window,font=entry_font)

#選擇輸出的位元
basebox = ttk.Combobox(window, values=[2,8,10,16],state='readonly')
basebox.set(10)

button = tk.Button(window, text="開始轉換",font = (10),command = convert_base)
label_result = tk.Label(window,text='',font=('Arial',26))

label1.pack()
chosebox.pack()
entry1.pack()
basebox.pack()
button.pack()
label_result.pack()


window.mainloop()