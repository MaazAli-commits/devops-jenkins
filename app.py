from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Containerized CI/CD Application</h1>
    <h2>Name : Mohammed Maaz Ali</h2>
    <h2>Roll Number: 2023BCS0202</h2>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)