import tkinter as tk
import subprocess

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
    output = subprocess.run(nmap_args, capture_output=True, text=True)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, output.stdout)

# Create the main window
root = tk.Tk()
root.title("Nmap GUI")

# Create and pack GUI components
target_label = tk.Label(root, text="Target:")
target_label.grid(row=0, column=0)

target_entry = tk.Entry(root)
target_entry.grid(row=0, column=1)

ping_var = tk.BooleanVar()
ping_checkbutton = tk.Checkbutton(root, text="Ping Scan (-Pn)", variable=ping_var)
ping_checkbutton.grid(row=1, columnspan=2, sticky=tk.W)

os_detection_var = tk.BooleanVar()
os_detection_checkbutton = tk.Checkbutton(root, text="OS Detection (-O)", variable=os_detection_var)
os_detection_checkbutton.grid(row=2, columnspan=2, sticky=tk.W)

service_version_var = tk.BooleanVar()
service_version_checkbutton = tk.Checkbutton(root, text="Service Version Detection (-sV)", variable=service_version_var)
service_version_checkbutton.grid(row=3, columnspan=2, sticky=tk.W)

script_scan_var = tk.BooleanVar()
script_scan_checkbutton = tk.Checkbutton(root, text="Script Scan (-sC)", variable=script_scan_var)
script_scan_checkbutton.grid(row=4, columnspan=2, sticky=tk.W)

scan_button = tk.Button(root, text="Scan", command=run_nmap_scan)
scan_button.grid(row=5, columnspan=2)

result_text = tk.Text(root)
result_text.grid(row=6, columnspan=2)

# Start the GUI event loop
root.mainloop()
