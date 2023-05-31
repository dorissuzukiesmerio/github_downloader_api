import json
import requests
import pandas

# Using the confidential data (that is stored in .gitignore and thus not uploaded to github)
f = open("token", "r")
token = f.read()
f.close()

f = open("username", "r")
username = f.read()
f.close()

# Creating a session
github_session = requests.Session()
github_session.auth = (username, token) # authentication

access_point = "https://api.github.com"

# # Check Rate Limit:
rate_limit_url = access_point + "/rate_limit"
result = json.loads(github_session.get(rate_limit_url).text)
print(result)
# # Reading the results : core : we have the limit of using the api for 5000

# # Downloading something from the user:
user_url = access_point + "/users/aarlt"
result = json.loads(github_session.get(user_url).text)
# print(result)

# To read:
# print(result['public_repos']) # just call the key of the json file

# The person's infor:
followers_url = result['followers_url']
print(followers_url)
result = json.loads(github_session.get(followers_url).text)
print(result)

#### python github_downloader.py > temp.json 
# saves the output of the program in a temporary file


followers = [item['followers'] for item in result]
print(followers) # list of all the followers

for follower in followers:
	user_url = access_point + "/users/" + follower
	result = json.loads(github_session.get(user_url).text)
	df = df.append({
	'follower_id' : follower,
	'public_repos' : result['public_repos'],
	'followers': result['followers'],
	'following': result['following'],
	'created_at': result['created_at'],
	'updated_at': result['updated_at'],
	}, ignore_index = True )

df.to_csv("github_followers_dataset.csv")
# to append into a csv

