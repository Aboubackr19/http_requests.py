import requests

def get_request(url):
    # Sends a GET request to the given URL and prints relevant information
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Response Body (first 500 chars):", response.text[:500])

def post_request(url, data):
    # Sends a POST request with the provided data and prints relevant information
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Response Body (first 500 chars):", response.text[:500])

# Running the functions with test data
get_request("https://jsonplaceholder.typicode.com/posts")

test_data = {
    "userId": 100,
    "title": "Test Data",
    "body": "This is a test POST request"
}
post_request("https://jsonplaceholder.typicode.com/posts", test_data)
