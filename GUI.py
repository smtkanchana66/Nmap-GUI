import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import threading

def run_nmap_scan():
    target = target_entry.get()
    nmap_args = ['nmap']
    
    # Add selected Nmap functions based on checkboxes
    if ping_var.get():
        nmap_args.append('-Pn')
    if os_detection_var.get():
        nmap_args.append('-O')
    if service_version_var.get():
        nmap_args.append('-sV')
    if script_scan_var.get():
        nmap_args.append('-sC')
    
    # Add target and execute Nmap command
    nmap_args.append(target)
    scan_thread = threading.Thread(target=start_scan, args=(nmap_args,))
    scan_thread.start()

def stop_nmap_scan():
    if scan_thread and scan_thread.is_alive():
        scan_thread.join(timeout=1)
        if scan_thread.is_alive():
            scan_thread.kill()
            messagebox.showinfo("Scan Stopped", "Scan stopped successfully.")

def start_scan(nmap_args):
    global scan_thread
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    scan_progress.start(10)
    try:
        output = subprocess.run(nmap_args, capture_output=True, text=True, timeout=300)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output.stdout)
    except subprocess.TimeoutExpired:
        messagebox.showwarning("Scan Timeout", "The scan took too long to complete.")
    finally:
        scan_progress.stop()
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Nmap GUI")
root.configure(bg="#0066CC")  # Blue background color

# Create and pack GUI components with styling
title_label = tk.Label(root, text="Nmap GUI", font=("Helvetica", 24, "bold"), bg="#0066CC", fg="white")  # White text color
title_label.grid(row=0, columnspan=2, padx=10, pady=10)

target_label = tk.Label(root, text="Target:", font=("Helvetica", 12), bg="#0066CC", fg="white")  # White text color
target_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

target_entry = tk.Entry(root, font=("Helvetica", 12))
target_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

ping_var = tk.BooleanVar()
ping_checkbutton = tk.Checkbutton(root, text="Ping Scan (-Pn)", variable=ping_var, font=("Helvetica", 12), bg="#0066CC", fg="white")  # White text color
ping_checkbutton.grid(row=2, columnspan=2, sticky=tk.W, padx=5, pady=5)

os_detection_var = tk.BooleanVar()
os_detection_checkbutton = tk.Checkbutton(root, text="OS Detection (-O)", variable=os_detection_var, font=("Helvetica", 12), bg="#0066CC", fg="white")  # White text color
os_detection_checkbutton.grid(row=3, columnspan=2, sticky=tk.W, padx=5, pady=5)

service_version_var = tk.BooleanVar()
service_version_checkbutton = tk.Checkbutton(root, text="Service Version Detection (-sV)", variable=service_version_var, font=("Helvetica", 12), bg="#0066CC", fg="white")  # White text color
service_version_checkbutton.grid(row=4, columnspan=2, sticky=tk.W, padx=5, pady=5)

script_scan_var = tk.BooleanVar()
script_scan_checkbutton = tk.Checkbutton(root, text="Script Scan (-sC)", variable=script_scan_var, font=("Helvetica", 12), bg="#0066CC", fg="white")  # White text color
script_scan_checkbutton.grid(row=5, columnspan=2, sticky=tk.W, padx=5, pady=5)

start_button = tk.Button(root, text="Start Scan", command=run_nmap_scan, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)  # Green button
start_button.grid(row=6, column=0, padx=10, pady=10)

stop_button = tk.Button(root, text="Stop Scan", command=stop_nmap_scan, font=("Helvetica", 12), bg="#FF5722", fg="white", padx=10, pady=5, state=tk.DISABLED)  # Red button
stop_button.grid(row=6, column=1, padx=10, pady=10)

scan_progress = ttk.Progressbar(root, mode="indeterminate", length=200)
scan_progress.grid(row=7, columnspan=2, padx=10, pady=10)

result_text = tk.Text(root, font=("Helvetica", 12), wrap="word")
result_text.grid(row=8, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()