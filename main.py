from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def greeting():
    args = request.args
    name = args.get('name')
    message = args.get('message')
    return f"Hello {name}! {message}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

