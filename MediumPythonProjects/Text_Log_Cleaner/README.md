# 🧹 Text Log Cleaner using Pandas

A lightweight Python utility that cleans raw chat logs by removing timestamps, system messages, and formatting speaker/message pairs for readability.

---

## ✨ Features

- 🕒 Removes timestamps using a flexible regex pattern  
- 🧠 Filters out system or server messages (`SYSTEM`, `ERROR`, `WARNING`, etc.)  
- 🗣️ Splits each line into **speaker** and **message** columns  
- 💾 Writes a cleaned, UTF-8 encoded text file to `/Output`  
- 📊 Prints a friendly summary of processed data  

---

## 📂 Project Structure

```
Text_Log_Cleaner/
│
├── Logs/
│   └── messy_log.txt           # Raw input file
│
├── Output/
│   └── cleaned_raw_pandas.txt  # Generated cleaned output
│
├── pandas_cleaner.py           # Main cleaning script
└── README.md                   # This file
```

---

## 🧩 Example

**Input:**
```
[2025-10-09 10:12:43] SYSTEM: Server started
[2025-10-09 10:13:11] LukFury: broooo did u roll that d20 😭
[2025-10-09 10:13:42] randomGuy_12: wait is this thing even working??
```

**Output:**
```
[2025-10-09 10:13:11] LukFury       : broooo did u roll that d20 😭
[2025-10-09 10:13:42] randomGuy_12  : wait is this thing even working??
```

**Console Summary:**
```
Summary:
         speaker              message
0        LukFury   broooo did u roll that d20 😭
1   randomGuy_12  wait is this thing even working??

🧮 Total lines processed: 23
✅ Valid lines kept: 16
```

---

## ⚙️ Usage

1. Place your raw `.txt` log file in the `Logs` folder.  
2. Run the cleaner:
   python pandas_cleaner.py
   
3. The cleaned log will appear in `Output/cleaned_raw_pandas.txt`.

---

## 🧰 Requirements

- Python 3.10+  
- Pandas ≥ 2.0  

Install dependencies:
    pip install pandas


---

## 👤 Author

**Lukasz Basczask**  
📅 *Created:* November 2025  
🧠 Built as part of the **Medium Python Projects** series.  

---

## 🧠 Notes

This project demonstrates:
- Data cleaning and string manipulation in Python  
- Regular expressions for structured text parsing  
- Practical use of `pandas` and `pathlib`  
- Modular, error-safe, and readable code design
