# 📁 檔案：final/gui.py (完整解答)
import tkinter as tk

def start_adventure():
    name = name_entry.get()
    log_lbl.config(text=f"> {name} 出發冒險！")

def quit_game():
    root.destroy()                 # 關閉視窗

root = tk.Tk()
root.title("勇者傳說：覺醒")
root.geometry("360x280")
root.configure(bg="#1e293b")

title_lbl = tk.Label(root, text="勇者傳說：覺醒", font=("Arial", 18, "bold"),
                     fg="gold", bg="#1e293b")
title_lbl.pack(pady=12)

name_entry = tk.Entry(root, font=("Arial", 13), justify="center")
name_entry.insert(0, "精靈射手")
name_entry.pack(pady=5)

start_btn = tk.Button(root, text="開始冒險", width=12, command=start_adventure)
start_btn.pack(pady=4)
quit_btn = tk.Button(root, text="離開", width=12, command=quit_game)
quit_btn.pack()

log_lbl = tk.Label(root, text="> 輸入名字，按開始冒險", font=("Courier", 11),
                   fg="#4ade80", bg="#0b1220", padx=10, pady=6)
log_lbl.pack(pady=10)

root.mainloop()