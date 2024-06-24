from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/get_cookie', methods=['GET'])
def get_cookie():
    email = request.args.get('email')
    password = request.args.get('password')
    if not email or not password:
        return {"error": "Email and password are required"}, 400
    
    # Dummy cookie for demonstration
    dummy_cookie = "sessionid=abc123; csrftoken=xyz789"
    return {"cookie": dummy_cookie}

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
