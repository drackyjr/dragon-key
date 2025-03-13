Here’s a professional **GitHub project description** for your keylogger:  

---

# **Dragon-Key: A Real-Time Keylogger for Security Auditing**  

## 🛡️ **About the Project**  
**Dragon-Key** is a lightweight, real-time keylogger designed for security auditing, penetration testing, and ethical hacking in controlled environments. This project demonstrates how keystrokes can be captured and sent remotely over TCP, helping cybersecurity professionals assess vulnerabilities in systems.  

⚠️ **Disclaimer:** This project is strictly for educational and ethical hacking purposes. Unauthorized use of this tool for malicious intent is illegal and punishable by law.  

## 🎯 **Features**  
✔️ Captures keystrokes in real-time  
✔️ Sends logged keystrokes to a remote server  
✔️ Simple client-server architecture using Python  
✔️ Supports key formatting (e.g., Enter, Backspace, Shift)  
✔️ Logs keystrokes in a text file for review  

## 🔧 **Installation & Usage**  

### **1️⃣ Install Dependencies**  
Ensure Python is installed, then run:  
```bash
pip install pynput
```

### **2️⃣ Run the Keylogger (Client)**  
Modify `SERVER_IP` to your attacker's machine IP and execute:  
```bash
python client.py
```

### **3️⃣ Run the Listener (Server)**  
Start the server to receive logs:  
```bash
python server.py
```

## 🛠 **How It Works**  
1️⃣ The **client** captures keystrokes using the `pynput` library  
2️⃣ Keystrokes are sent over **TCP** to a remote **server**  
3️⃣ The **server** logs keystrokes in real-time  

## 🏆 **Why Use Dragon-Key?**  
- **Penetration Testers**: Evaluate security weaknesses  
- **Cybersecurity Enthusiasts**: Learn about keylogging techniques  
- **Ethical Hackers**: Understand remote keystroke monitoring  

## 📜 **Legal Notice**  
This tool is intended for legal **security testing** and **educational purposes** only. Do not use it on unauthorized systems.  

## 🖥️ **Contributing**  
Feel free to contribute by submitting pull requests! 🚀  

---  

