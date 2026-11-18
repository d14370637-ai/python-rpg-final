# 📁 檔案：final/w10_label.py
import tkinter as tk

root = tk.Tk()
root.geometry("320x180")
root.configure(bg="#1e293b")

title_lbl = tk.Label(root, text="勇者傳說：覺醒",
                     font=("Arial", 20, "bold"),
                     fg="gold", bg="#1e293b")
title_lbl.pack(pady=10)

hp_lbl = tk.Label(root, text="HP 100\nMP 30",
                  font=("Courier", 12), justify="left")
hp_lbl.pack()

hp_lbl.config(text="HP 85\nMP 30")   # 建立之後也能改文字

root.mainloop()