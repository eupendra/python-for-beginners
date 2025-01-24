from flask import Flask, request

app = Flask('test_app')

error_codes = {
    31: "Invalid configuration file.",
    32: "Administrator has blocked backup.",
    33: "Failed to read recovery point.",
    34: "The session is invalid.",
}


@app.route('/')
def index():
    return {"message": "Ready!"}


@app.route('/<int:code>')
def get_error_description(code):
    if code:
        description = error_codes.get(code, "Unknown error code. Contact Support")
        return {"code": code, "description": description}
    else:
        return {"message": "Ready!"}


if __name__ == '__main__':
    app.run(debug=True)
