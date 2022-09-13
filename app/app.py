from flask import Flask

print('Reading config')

try:
    with open('/config/config.txt') as f:
        config = f.read()
        print(config)

except Exception as e:
    print(e.__class__)
    raise e

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'