from flask import Flask, render_template
import os

app = Flask(__name__)

# Define the path to the log file
LOG_FILE_PATH = "farmcheck.log"

@app.route('/')
def index():
    # Check if the log file exists
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'r') as file:
            log_content = file.read()
    else:
        log_content = "Log file not found."
    
    return render_template('index.html', log_content=log_content)

if __name__ == '__main__':
    app.run(debug=True)