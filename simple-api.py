from flask import Flask, jsonify, request

app = Flask('test_app')

error_codes = {
    "31": "Invalid configuration file.",
    "32": "Administrator has blocked backup.",
    "33": "Failed to read recovery point.",
    "34": "The session is invalid.",
}

@app.route('/')
def get_error_description():
    code = request.args.get('code')  # Get the 'code' query parameter
    if code:
        description = error_codes.get(code, "Unknown error code. Contact Support")
        return jsonify({"code": code, "description": description})
    else:
        return jsonify({"message": "Ready!"})  # Return JSON response for the "Ready" state

if __name__ == '__main__':
    app.run(debug=True)