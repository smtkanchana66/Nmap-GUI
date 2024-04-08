import tkinter as tk
import subprocess

def run_nmap_scan():
    target = target_entry.get()
    output = subprocess.run(['nmap', target], capture_output=True, text=True)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, output.stdout)

# Create the main window
root = tk.Tk()
root.title("Nmap GUI")

# Create and pack GUI components
target_label = tk.Label(root, text="Target:")
target_label.pack()

target_entry = tk.Entry(root)
target_entry.pack()

scan_button = tk.Button(root, text="Scan", command=run_nmap_scan)
scan_button.pack()

result_text = tk.Text(root)
result_text.pack()

# Start the GUI event loop
root.mainloop()