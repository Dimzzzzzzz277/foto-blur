"""
Flask Web Server for Hand Gesture App (Static Server Version)
Serves index.html and audio files statically from the root directory.
The actual hand gesture detection is performed entirely in JavaScript.
"""

from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def serve_static(path):
    # Safely serves files (like MP3 files) from root directory
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Runs on port 5005
    app.run(host='0.0.0.0', port=5005, debug=True, use_reloader=False)
