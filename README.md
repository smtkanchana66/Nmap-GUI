
# Nmap GUI Documentation

<p align="center">
  <img src="https://github.com/smtkanchana66/Nmap-GUI/blob/main/nmap.jpg" />
</p>

### Overview
The Nmap GUI is a graphical user interface built using the Tkinter library in Python. It provides a user-friendly interface to interact with the Nmap network scanning tool. With this GUI, users can specify target hosts and customize scanning options easily.

### Features
- Input field for specifying the target host.
- Checkboxes to enable/disable various Nmap scan options.
- Start and Stop buttons to initiate and halt the scan process.
- Progress bar to indicate the progress of the scan.
- Text area to display the scan results.

### Usage
01. Target Entry: Enter the target host IP address or hostname in the input field provided.
02. Scan Options:
    - Ping Scan (-Pn): Enable/disable ping scan.
    - OS Detection (-O): Enable/disable operating system detection.
    - Service Version Detection (-sV): Enable/disable service version detection.
    - Script Scan (-sC): Enable/disable script scanning.
    - Start Scan: Click this button to start the Nmap scan with the specified options and target host.

03. Stop Scan: Click this button to stop the currently running scan process. This button is enabled only during an active scan.
04. Progress Bar: Displays the progress of the scan process. It moves from left to right as the scan progresses.
05. Scan Results: Displays the output of the Nmap scan. This area is updated in real-time as the scan progresses.

### Dependencies
- Python 3.x
- Tkinter (Standard Python library for GUI development)
- Nmap (Network scanning tool)

### Installation
01. Install Python from the official website: <a href="https://www.python.org/downloads/"> Python Downloads </a>
02. Install Nmap using package managers like apt, yum, or by downloading from the official website: <a href="https://nmap.org/download.html"> Nmap Download </a>

### How to Run
01. Clone the repository or download the GUI.py file.
02. Open a terminal or command prompt.
03. Navigate to the directory containing GUI.py.
04. Run the following command:
```bash
python GUI.py
```
05. The Nmap GUI window should appear, allowing you to perform network scans using the graphical interface.

### Contributing
Contributions to this project are welcome! If you encounter any bugs, have suggestions for improvements, or want to add new features, please feel free to open an issue or submit a pull request on GitHub.

### License
This project is licensed under the MIT License.


