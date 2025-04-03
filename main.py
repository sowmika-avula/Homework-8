from flask import Flask

app = Flask(__name__)
VERSION = "1.0.0"

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>DevOps Demo</title>
            <style>
                body { 
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background: #f0f2f5;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                h1 { color: #1a73e8; }
                .version { color: #666; font-size: 0.9em; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to DevOps Demo</h1>
                <p>This is a simple Flask application containerized with Docker and deployed using GitHub Actions.</p>
                <p>Created by: Sowmika Avula</p>
                <p class="version">Version: """ + VERSION + """</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)