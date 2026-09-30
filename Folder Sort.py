import shutil
import os
from tkinter import filedialog
import customtkinter as ctk

root = ctk.CTk()

root.geometry("600x300")
root.title("Sorting Downloads")

root.attributes("-alpha", 0.85)

def select_folder():
        path = filedialog.askdirectory()
        if path:
            entry1.delete(0, "end")
            entry1.insert(0, path)


def sort_folder():
        folder_path = entry1.get().strip()
        if not folder_path or not os.path.exists(folder_path):
            return

        rules = {
            "Images": [".png", ".jpg", ".gif", ".webp"],
            "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
            "archives": [".zip", ".rar", ".7z"],
            "programs": [".exe", ".msi"],
            "Videos": [".mp4", ".mkv", ".mov"]
        }

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isdir(file_path):
                continue        

            _, ext = os.path.splitext(file_name)
            for category, exts in rules.items():
                if ext.lower() in exts:
                    target_dir = os.path.join(folder_path, category)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_dir, file_name))
                    break

frame = ctk.CTkFrame(root, fg_color="transparent")
frame.pack(pady=20)

entry1 = ctk.CTkEntry(frame, width=320, placeholder_text="Take a Folder...")
entry1.pack(side="left", padx=(0, 10))

btn_browse = ctk.CTkButton(frame, text="Обзор...", width=100, height=32, command=select_folder)
btn_browse.pack(side="left")

btn_start = ctk.CTkButton(
    root, 
    text="Отсортировать файлы", 
    width=200, 
    height=40, 
    font=("Arial", 14, "bold"), 
    command=sort_folder
    )
btn_start.pack(pady=10)

label = ctk.CTkLabel(
    root, 
    text="You don't need a second folder to sort.\nIt sorts files automatically inside the selected directory.", 
    font=("Arial", 25), 
    wraplength=450, 
    justify="center"
    )
label.pack(pady=20)

root.mainloop()
