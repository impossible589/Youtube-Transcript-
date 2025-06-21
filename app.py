from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/hello')
def hello():
    return {"message": "Hello from Python backend"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
