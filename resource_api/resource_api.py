from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/resource", methods=["GET"])
def get_resource():
    """
    Retrieves resource data using token-based authentication.

    This function simulates a resource API that requires token-based authentication.
    It checks the `Authorization` header for a valid token in the form of "Bearer <token>",
    and if the token is valid, it returns resource data.

    Returns:
        tuple: A tuple containing the resource data JSON response and an HTTP status code.

    """
    auth_header = request.headers.get("Authorization")
    print(auth_header)
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "You are not authorized to access this page."}), 401

    else:
        # If token is valid, return resource data with 200 OK status
        resource_data = {"data": "You have succesfully connected to the database. This is your resource data."}
        return jsonify(resource_data), 200

if __name__ == "__main__":
    app.run(host="localhost", port=8001)
