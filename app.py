from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Somya Kukreti"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME")
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    # Get top command output
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -10", shell=True, text=True)
    except Exception as e:
        top_output = str(e)

    return f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
