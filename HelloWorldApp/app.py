from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

# GitHub Pages does not support custom ports, and all traffic is served over the standard 
# HTTP and HTTPS ports (80 and 443, respectively). Therefore, you do not need to specify a 
# port number for your Flask application when deploying it to GitHub Pages.

# By default, Flask runs on http://localhost:5000/, but you should modify the app.run() 
# line in your "app.py" file to listen on all available network interfaces using 0.0.0.0 as the host address