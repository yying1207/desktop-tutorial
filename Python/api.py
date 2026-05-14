import requests

# Make a GET request to a URL
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f'Error: {response.status_code}')


# Define the URL and payload data
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Make a POST request with the data
response = requests.post(url, json=data)

# Check if the request was successful (HTTP status code 201 for created)
if response.status_code == 201:
    print(f'Success! New post created with ID {response.json()["id"]}')
else:
    print(f'Error: {response.status_code}')


# Define the URL and updated data
url = "https://jsonplaceholder.typicode.com/posts/1"
data = {
    'title': 'updated title',
    'body': 'updated body',
}

# Make a PUT request to update the resource
response = requests.put(url, json=data)

# Check if the request was successful (HTTP status code 200 for OK)
if response.status_code == 200:
    print(f'Success! Post updated: {response.json()}')
else:
    print(f'Error: {response.status_code}')


# Make a DELETE request to delete the resource
response = requests.delete(url)

# Check if the request was successful (HTTP status code 200 for OK)
if response.status_code == 200:
    print('Success! Post deleted.')
else:
    print(f'Error: {response.status_code}')