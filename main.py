from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def greeting():
    args = request.args
    name = args.get('name')
    message = args.get('message')
    final_message = f"Hello {name}! {message}!"
    return render_template('index.html', final_message=final_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

