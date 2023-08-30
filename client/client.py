import requests

def main():
    """
    Simulates the interaction between a client and a resource API with token-based authentication.

    This function simulates the process of obtaining an authentication token from an authorization server,
    and then using that token to access a resource API. The user is prompted to input an authentication token,
    and if the provided token matches the auth token obtained from the authorization server, the resource data
    is accessed and displayed.

    Raises:
        requests.exceptions.RequestException: If there's an error during the HTTP requests.

    """
    auth_server_url = "http://localhost:8000/authenticate"
    resource_api_url = "http://localhost:8001/resource"

    try:
        # Simulate authentication
        response = requests.get(auth_server_url)
        response.raise_for_status()  # Raise an exception if the response status code indicates an error
        auth_token = response.json().get("auth_token")

        user_token = input("Enter the authentication token: ")

        if user_token == auth_token:
            headers = {"Authorization": f"Bearer {auth_token}"}
            response = requests.get(resource_api_url, headers=headers)

            if response.status_code == 200:
                resource_data = response.json()
                print(resource_data)
        else:
            print("Access to resource API was denied due to unsuccessful token authentication.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
