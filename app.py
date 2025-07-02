from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from docker+ecr - CI/CD Pipeline Test! 🚀'

@app.route('/health')
def health():
    return {'status': 'healthy', 'version': '1.1'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 