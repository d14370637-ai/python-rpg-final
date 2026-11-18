# 📁 檔案：final/w10_button.py
import tkinter as tk

def talk():
    npc_lbl.config(text="村長：勇者，歡迎來到新手村！")

root = tk.Tk()
root.geometry("340x150")

npc_lbl = tk.Label(root, text="村長：……", font=("Arial", 13))
npc_lbl.pack(pady=20)

talk_btn = tk.Button(root, text="和村長說話", command=talk)
talk_btn.pack()

root.mainloop()