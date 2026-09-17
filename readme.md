### Goto path e:\workspace in commandline
E:\workspace>

### Clone the project from git repository into workspace folder
'''
E:\workspace> git clone git@github.com:ykullal/FastAPI_AWS_EC2_Deployment_Demo.git

Change the directory

E:\workspace> cd FastAPI_AWS_EC2_Deployment_Demo
'''

### Creating virtual environment, and activating it:
'''
Command for bash shell on windows: 

E:\workspace\FastAPI_AWS_EC2_Deployment_Demo> /c/Python312/python -m venv venv

Command for windows commandline: 

E:\workspace\FastAPI_AWS_EC2_Deployment_Demo> python -m venv venv

Activate the virtual  environment (On Windows)
E:\workspace\FastAPI_AWS_EC2_Deployment_Demo>venv\scripts\Activate
'''

### Create a requirements.txt file in project root folder and add the required python packages into it:
'''
fastapi
fastapi[standard]
uvicorn[standard]
'''

### Install all the require python packages
'''
(venv) E:\workspace\FastAPI_AWS_EC2_Deployment_Demo>pip install -r requirements.txt
'''

### Create a main.py file in project root folder and implement all required API endpoints 
'''
Here are the sample code for get & delete API's:

@app.get("/songs")
async def get_songs():
	return songs

@app.delete("/songs/{sing_id}")
async def delete_item():
	for song in songs:
		if sing_id == song['id']
			songs.remove(song)
		return song
	raise HTTPError(f"The song with id {song_id} not found")
,,,


### Starting the REST API server in development environment.
'''
Older way: 
	uvicorn main:app --reload  (This uses the default port of 8000)
	          or
	uvicorn main:app --port 8888 --reload
	
Newer way:
	fastapi dev main.py
			OR
	fastapi dev main.py --port 8888 --reload
	
'''

### Testing the API's
#### Use POSTMAN or Bruno tool. We can also use the built-in swagger UI provided by the FastAPI framework
#### Using the curl command
'''
curl -X 'GET' 'http://127.0.0.1:8000/songs' -H 'accept: application/json'
curl -X 'GET' 'http://127.0.0.1:8000/songs?limit=10' -H 'accept: application/json'
curl -X 'GET' 'http://127.0.0.1:8000/songs/5' -H 'accept: application/json'

curl -X 'POST' 'http://127.0.0.1:8000/songs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
"language": "Kannada", 
"title": "Nesara nodu", 
"genre": "movie"
}'

curl -X 'PUT' 'http://127.0.0.1:8000/songs/21' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
"language": "Kannada", 
"title": "Yaaru thiliyaru ninna", 
"genre": "movie"
}'

curl -X 'DELETE' 'http://127.0.0.1:8000/songs/21' -H 'accept: application/json'
'''
### Swagger API documents
#### http://127.0.0.1:8000/docs#


