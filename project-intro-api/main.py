# import requests

# # Component	Value
# # Protocol	http
# # Domain	localhost
# # Port	3000
# # Path	/lyrics/random
# # Artist filter parameter	artist
# # Include track parameter	include_track

# # Add the `include_track` parameter
# query_params = {'artist': 'Deep Purple', 'include_track' : True}

# response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

# # Print the response URL
# print(response.url)

# # Print the lyric
# print(response.text)

# # Perform a DELETE request to the playlist API using the path to playlist with PlaylistId 2
# requests.delete('http://localhost:3000/playlists/2')

# # Get the list of all existing playlists again
# response = requests.get('http://localhost:3000/playlists')
# print(response.text)

# # Create a dictionary with the playlist info
# playlist_data = {"Name": "Rock Ballads"}
# # Perform a POST request to the playlists API with your dictionary as data parameter
# response = requests.post('http://localhost:3000/playlists', data=playlist_data)
# print(response.text)

# response = requests.get('http://localhost:3000/lyrics')

# # Check the response status code
# if (response.status_code == 200):
#   print('The server responded succesfully!')

# Make a request to the movies endpoint of the API
# response = requests.get('http://localhost:3000/movies')

# if (response.status_code == 200):
#   print('The server responded succesfully!')
  
# # Check the response status code
# elif (response.status_code == 404):
#   print('Oops, that API could not be found!')


# response = requests.get('http://localhost:3000/movies')

# # Check if the response.status_code is equal to the requests.codes value for "200 OK"
# if (response.status_code == requests.codes.ok ):
#   print('The server responded succesfully!')
  
# # Or if the request was not successful because the API did not exist
# elif (response.status_code == requests.codes.not_found):
#   print('Oops, that API could not be found!')


# response = requests.get('http://localhost:3000/lyrics')

# # Print the response content-type header
# print(response.headers["content-type"])


# response = requests.get('http://localhost:3000/lyrics')

# # Print the response accept header
# print(response.headers["accept"])

# import requests

# headers = {"accept": "application/json"}
# response = requests.get('http://localhost:3000/lyrics', headers=headers)

# print(response.text)

# # Add a header to use in the request
# headers = {"accept": "application/xml"}
# response = requests.get('http://localhost:3000/lyrics', headers=headers)

# # Check if the server did not accept the request
# if (response.status_code == requests.codes.not_acceptable):
#   print('The server can not respond in XML')
  
#   # Print the accepted content types
#   print('These are the content types the server accepts: ' + response.headers["accept"])
# else:
#   print(response.text)


# # Create the authentication tuple with the correct values for basic authentication
# authentication = ("john@doe.com","Warp_ExtrapolationsForfeited2")

# # Use the correct function argument to pass the authentication tuple to the API
# response = requests.get('http://localhost:3000/albums', auth = authentication)

# if(response.status_code == 200):
#     print("Success!")
# elif(response.status_code == 401):
#     print('Authentication failed')
# else:
#     print('Another error occurred')

# # Create a dictionary containing the API key using the correct key-value combination
# params = {"access_token": "8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3"}
# # Add the dictionary to the requests.get() call using the correct function argument
# response = requests.get('http://localhost:3000/albums', params=params)

# if(response.status_code == 200):
#     print("Success!")
# elif(response.status_code == 401):
#     print('Authentication failed')
# else:
#     print('Another error occurred')

# # Create a headers dictionary containing and set the API key using the correct key and value 
# headers = {"Authorization": "Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3"}
# # Add the headers dictionary to the requests.get() call using the correct function argument
# response = requests.get('http://localhost:3000/albums', headers=headers)

# if(response.status_code == 200):
#     print("Success!")
# elif(response.status_code == 401):
#     print('Authentication failed')
# else:
#     print('Another error occurred')


# headers = {
#     'Authorization': 'Bearer ' + API_TOKEN,
#     # Add a header to request JSON formatted data
#     "accept": "application/json"
# }
# response = requests.get('http://localhost:3000/albums/1/', headers=headers)

# # Get the JSON data as a Python object from the response object
# album = response.json()

# # Print the album title
# print(album["Title"])


# import requests

# playlists = [{"Name": "Rock ballads"}, {"Name": "My favorite songs"}, {"Name": "Road Trip"}]

# # POST the playlists array to the API using the json argument
# requests.post('http://localhost:3000/playlists/', json=playlists)

# # Get the list of all created playlists
# response = requests.get('http://localhost:3000/playlists')

# # Print the response text to inspect the JSON text
# print(response.text)


# import requests
# from requests.exceptions import ConnectionError

# url = "http://wronghost:3000/albums"

# try:
#     r = requests.get(url)
#     print(r.status_code)
# # Use the imported class to intercept the connection error
# except ConnectionError as conn_err:
#     print(f'Connection Error! {conn_err}.')


# # Import the correct exception class
# from requests.exceptions import HTTPError

# url ="http://localhost:3000/albums/"
# try: 
#     r = requests.get(url) 
# 	# Enable raising errors for all error status_codes
#     r.raise_for_status()
#     print(r.status_code)
# # Intercept the error 
# except HTTPError as http_err:
#     print(f'HTTP error occurred: {http_err}')