from flask import Flask

print("Reading config")

try:
    with open("/config/config.txt") as f:
        config = f.read()
        print(config)

except Exception as e:
    print(e.__class__)
    raise e

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, Docker!"


@app.route("/config")
def output_config():
    return config


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
