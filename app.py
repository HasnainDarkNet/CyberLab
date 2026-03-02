from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

selected_file_path = None  # Ye variable runtime me file store karega

# ================= Terminal Se File Select =================
def select_file():
    global selected_file_path
    print("\n===== HASNAIN DARK NET FILE SELECTOR =====\n")
    path = input("Enter full path of your file to make downloadable: ").strip()

    if os.path.exists(path) and os.path.isfile(path):
        selected_file_path = path
        print("\n✅ File selected successfully!")
        print(f"File: {selected_file_path}\n")
        return True
    else:
        print("\n❌ File not found or invalid path!")
        return False

# ================= Routes =================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download():
    global selected_file_path
    if selected_file_path:
        filename = os.path.basename(selected_file_path)
        return send_file(selected_file_path, as_attachment=True, download_name=filename)
    return "No file selected!"

# ================= Run =================
if __name__ == "__main__":
    if select_file():
        app.run(host="0.0.0.0", port=5000, debug=True)
