from flask import Flask, make_response, request

app = Flask(__name__, static_url_path="")


@app.route("/ping", methods=["GET", "POST"])
def ping():
    return make_response({
        "message": "Pong"
    })


@app.route("/ping/<int:num>", methods=["GET", "POST"])
def ping_with_int(num):
    return make_response({
        "message": "Pong",
        "num": num,
    })


@app.route("/request", methods=["GET"])
def print_request():
    return make_response({
        "url": request.url,
        "path": request.path,
        "args": request.args,
    })


@app.route("/request/<int:num>", methods=["GET"])
def print_request_with_num(num):
    return make_response({
        "url": request.url,
        "path": request.path,
        "args": request.args,
        "num": num,
    })


if __name__ == '__main__':
    app.run(debug=True, port=10000)
