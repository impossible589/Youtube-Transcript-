from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')
@app.route('/loaderio-6eb9bf95da20f05ae75ff6a724761fb3.txt')
def servetest():
    return send_from_directory(app.static_folder,'loaderio-6eb9bf95da20f05ae75ff6a724761fb3.txt')
@app.route('/test')
def serve_index2():
    return send_from_directory(app.static_folder, 'test.jpeg')


@app.route('/api/hello')
def hello():
    return {"message": "Hello from Python backend"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
