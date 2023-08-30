from flask import Flask, jsonify
import secrets

app = Flask(__name__)

@app.route("/authenticate", methods=["GET"])
def authenticate():
    """
    Simulates an authentication process and generates an authentication token.

    This function simulates an authentication process and generates an authentication token
    using the `secrets` module. The token is a hexadecimal string of length 64 characters.

    Returns:
        dict: A JSON response containing the generated authentication token.

    """
    # Simulate authentication and generate an auth token
    auth_token = secrets.token_hex(32)
    print(auth_token)
    return jsonify({"auth_token": auth_token})

if __name__ == "__main__":
    app.run(host="localhost", port=8000)
