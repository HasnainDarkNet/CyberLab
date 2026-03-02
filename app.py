import os
import sys
import time
import subprocess

# ================= Check & Install Flask =================
try:
    from flask import Flask, render_template, send_file
except ImportError:
    print("\n⚠ Flask is not installed. Installing now...\n")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Flask>=2.3.0,<3.0"])
    print("\n✅ Flask installed! Please re-run the tool.\n")
    sys.exit()

# ================= Terminal Clear Function =================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ================= CyberLab Banner =================
def cyberlab_banner():
    clear()
    banner = r"""
   ╔════════════════════════════╗
   ║      C Y B E R   L A B     ║
   ╚════════════════════════════╝
░▒▓█ HASNAIN DARK NET CYBER LAB █▓▒░
    """
    print("\033[1;32m" + banner + "\033[0m")
    subtitle = "Learn Safe File Handling & Cyber Awareness"
    for char in subtitle:
        sys.stdout.write("\033[0;32m" + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

# ================= Initialize Flask =================
app = Flask(__name__)
selected_file_path = None

# ================= Terminal File Selector =================
def select_file():
    global selected_file_path
    print("\n===== CYBERLAB FILE SELECTOR =====\n")
    try:
        path = input("Enter full path of your file to make downloadable: ").strip()
        if os.path.exists(path) and os.path.isfile(path):
            selected_file_path = path
            print(f"\n✅ File selected: {selected_file_path}\n")
            print("Open your browser and visit http://127.0.0.1:5000 to download the file.\n")
            return True
        else:
            print("\n❌ File not found or invalid path!")
            return False
    except KeyboardInterrupt:
        print("\n❌ User canceled.")
        sys.exit()

# ================= Routes =================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download():
    global selected_file_path
    if selected_file_path:
        filename = os.path.basename(selected_file_path)
        # Serve file ONLY for browser download
        return send_file(selected_file_path, as_attachment=True, download_name=filename)
    return "❌ No file selected! Go back to terminal and select a file first."

# ================= Run =================
if __name__ == "__main__":
    cyberlab_banner()
    if select_file():
        # Disable Flask debug mode for safe local use
        app.run(host="0.0.0.0", port=5000)
# ================= Initialize Flask =================
app = Flask(__name__)
selected_file_path = None

# ================= Terminal File Selector =================
def select_file():
    global selected_file_path
    print("\n===== CYBERLAB FILE SELECTOR =====\n")
    path = input("Enter full path of your file to make downloadable: ").strip()

    if os.path.exists(path) and os.path.isfile(path):
        selected_file_path = path
        print(f"\n✅ File selected: {selected_file_path}\n")
        print("Open your browser and visit http://127.0.0.1:5000 to download the file.\n")
        return True
    else:
        print("\n❌ File not found or invalid path!")
        return False

# ================= Routes =================
@app.route("/")
def home():
    return render_template("index.html")  # Browser interface

@app.route("/download")
def download():
    global selected_file_path
    if selected_file_path:
        filename = os.path.basename(selected_file_path)
        return send_file(selected_file_path, as_attachment=True, download_name=filename)
    return "No file selected!"

# ================= Run =================
if __name__ == "__main__":
    cyberlab_banner()
    if select_file():
        app.run(host="0.0.0.0", port=5000, debug=True)
