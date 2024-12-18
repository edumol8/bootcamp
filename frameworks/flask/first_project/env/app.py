from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "<h1>hello world from flask</h1>"

if __name__ == '__main__':
    print("servidor ejecutado !")
    app.run(debug=True)
