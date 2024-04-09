import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess
import threading

scan_thread = None  # Global variable to track the scan thread
stop_flag = False  # Flag to indicate if the scan should be stopped

def run_nmap_scan():
    global scan_thread, stop_flag
    stop_flag = False  # Reset the stop flag
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
    global stop_flag
    stop_flag = True  # Set the stop flag to indicate the scan should stop

def start_scan(nmap_args):
    global stop_flag
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    scan_progress.start(10)
    try:
        output = subprocess.run(nmap_args, capture_output=True, text=True, timeout=300)
        if not stop_flag:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, output.stdout)
    except subprocess.TimeoutExpired:
        if not stop_flag:
            messagebox.showwarning("Scan Timeout", "The scan took too long to complete.")
    finally:
        scan_progress.stop()
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Nmap GUI")
root.geometry("500x400")  # Set the window size

# Define colors
background_color = "#f0f0f0"
accent_color = "#0078d4"

# Set the background color
root.configure(bg=background_color)

# Create and pack GUI components with styling
target_label = tk.Label(root, text="Target:", bg=background_color)
target_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

target_entry = tk.Entry(root)
target_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

ping_var = tk.BooleanVar()
ping_checkbutton = tk.Checkbutton(root, text="Ping Scan (-Pn)", variable=ping_var, bg=background_color)
ping_checkbutton.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

os_detection_var = tk.BooleanVar()
os_detection_checkbutton = tk.Checkbutton(root, text="OS Detection (-O)", variable=os_detection_var, bg=background_color)
os_detection_checkbutton.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

service_version_var = tk.BooleanVar()
service_version_checkbutton = tk.Checkbutton(root, text="Service Version Detection (-sV)", variable=service_version_var, bg=background_color)
service_version_checkbutton.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

script_scan_var = tk.BooleanVar()
script_scan_checkbutton = tk.Checkbutton(root, text="Script Scan (-sC)", variable=script_scan_var, bg=background_color)
script_scan_checkbutton.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

start_button = tk.Button(root, text="Start Scan", command=run_nmap_scan, bg=accent_color, fg="white")
start_button.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

stop_button = tk.Button(root, text="Stop Scan", command=stop_nmap_scan, state=tk.DISABLED, bg=accent_color, fg="white")
stop_button.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

scan_progress = ttk.Progressbar(root, mode="indeterminate", length=400)
scan_progress.grid(row=6, columnspan=2, padx=10, pady=10)

result_text = tk.Text(root)
result_text.grid(row=7, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configure row and column weights
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure((0, 1), weight=1)

# Start the GUI event loop
root.mainloop()
