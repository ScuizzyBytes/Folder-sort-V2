# 📂 Downloads Cleaner

> **Fast, automated file organizer with a modern GUI.**

A lightweight desktop utility built in Python that eliminates folder chaos by automatically sorting clutter into clean, categorized directories.

---

## ✨ Key Features

- **Instant Sorting:** Scans and moves files into dedicated folders in milliseconds.
- **Modern UI:** Styled with `CustomTkinter` for a clean, modern aesthetic.
- **Built-in File Explorer:** Select any directory on your system using the native file picker.
- **Smart Categorization:**
  - 🖼️ **Images:** `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`
  - 📄 **Documents:** `.pdf`, `.docx`, `.txt`, `.xlsx`
  - 📦 **Archives:** `.zip`, `.rar`, `.7z`
  - ⚙️ **Programs:** `.exe`, `.msi`
  - 🎥 **Videos:** `.mp4`, `.mkv`, `.mov`
- **Safe Execution:** Skips existing subdirectories to prevent nested loop errors.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **GUI Library:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **Built-in Modules:** `os`, `shutil`, `tkinter`

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have Python installed on your machine:
```bash
python --version
