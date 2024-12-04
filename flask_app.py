from flask import Flask, request, render_template, jsonify
import json
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Route to handle GET request with query parameters in URL (log messages)
@app.route('/log', methods=['GET'])
def log_messages():
    # Get messages from the URL query parameters
    message1 = request.args.get('message1', '')
    message2 = request.args.get('message2', '')
    message3 = request.args.get('message3', '')  # New message

    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create a dictionary for the log entry
    log_entry = {
        'datetime': current_time,
        'message1': message1,
        'message2': message2,
        'message3': message3  # Include the third message
    }

    # Open the log file and write the log entry as JSON
    with open('app.log', 'a') as log_file:
        log_file.write(json.dumps(log_entry) + '\n')

    # Return a success response
    return jsonify({'status': 'success', 'message': 'Messages logged successfully'}), 200


# Route to display log entries in a table
@app.route('/view')
def view_logs():
    log_entries = []
    
    # Read the log file and load each JSON entry
    try:
        with open('app.log', 'r') as log_file:
            for line in log_file:
                log_entries.append(json.loads(line.strip()))
    except FileNotFoundError:
        pass  # If the file doesn't exist, no logs are available

    # Render the view template with the log entries
    return render_template('view_logs.html', log_entries=log_entries)


if __name__ == '__main__':
    app.run(debug=True)
## http://127.0.0.1:5000/log?message1=Bishop 108&message2=80&message3=22
## http://127.0.0.1:5000/view
