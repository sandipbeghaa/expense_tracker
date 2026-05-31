import json
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

DATA_FILE = Path("expenses.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_expense(category, amount, note):
    data = load_data()
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be numeric.")
        return
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": category,
        "amount": amount,
        "note": note
    }
    data.append(entry)
    save_data(data)
    update_tree()
    clear_fields()

def update_tree():
    for i in tree.get_children():
        tree.delete(i)
    data = load_data()
    total = 0
    for e in data:
        tree.insert("", "end", values=(e['date'], e['category'], f"${e['amount']:.2f}", e['note']))
        total += e['amount']
    total_label.config(text=f"Total: ${total:.2f}")

def clear_fields():
    cat_entry.delete(0, tk.END)
    amt_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

def show_summary():
    data = load_data()
    summary = {}
    for e in data:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    summary_str = "\n".join([f"{c}: ${a:.2f}" for c, a in summary.items()])
    messagebox.showinfo("Summary by Category", summary_str or "No data")

# GUI
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x400")

frm = tk.Frame(root)
frm.pack(pady=10)

tk.Label(frm, text="Category:").grid(row=0, column=0)
cat_entry = tk.Entry(frm)
cat_entry.grid(row=0, column=1)

tk.Label(frm, text="Amount:").grid(row=0, column=2)
amt_entry = tk.Entry(frm)
amt_entry.grid(row=0, column=3)

tk.Label(frm, text="Note:").grid(row=0, column=4)
note_entry = tk.Entry(frm)
note_entry.grid(row=0, column=5)

tk.Button(frm, text="Add", command=lambda: add_expense(cat_entry.get(), amt_entry.get(), note_entry.get())).grid(row=0, column=6, padx=5)
tk.Button(frm, text="Summary", command=show_summary).grid(row=0, column=7)

tree = ttk.Treeview(root, columns=("Date", "Category", "Amount", "Note"), show="headings")
for col in ("Date", "Category", "Amount", "Note"):
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(fill="both", expand=True, padx=10, pady=10)

total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"))
total_label.pack(pady=5)

update_tree()
root.mainloop()