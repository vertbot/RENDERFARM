from flask import Flask, request, jsonify
import json
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Route to handle GET request with query parameters in URL
@app.route('/log', methods=['GET'])
def log_messages():
    # Get messages from the URL query parameters
    message1 = request.args.get('message1', '')
    message2 = request.args.get('message2', '')

    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create a dictionary for the log entry
    log_entry = {
        'datetime': current_time,
        'message1': message1,
        'message2': message2
    }

    # Open the log file and write the log entry as JSON
    with open('app.log', 'a') as log_file:
        log_file.write(json.dumps(log_entry) + '\n')

    # Return a success response
    return jsonify({'status': 'success', 'message': 'Messages logged successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)