from flask import Flask,redirect,jsonify,session
import requests
import urllib.parse 
import datetime


app=Flask(__name__)
app.secret_key = 'a7f8g9h1j2k3l4m5n6o7p8q9r0s5t6u7v8w9x0y1z2'
CLIENT_ID="8606db6cd5a145bb8f4bae2f97b9d785"
CLIENT_SECRET="d922234379b34f3892523cb9aafad20e"
REDIRECT_URI='http://localhost:5000/callback'
AUTH_URL='https://accounts.spotify.com/authorize'
TOKEN_URL='https://accounts.spotify.com/api/token'
API_BASE_URL='https://api.spotify.com/v1/'

@app.route('/')
def index():
    return "Spotify app <a href='/login'></a>"

@app.route('/login')
def index():
    scope='user-read-private user-read-email'
    params={
        'client_id':CLIENT_ID,
        'response_type':"code",
        'scope':scope,
        'redirect_uri':REDIRECT_URI,
        'show_dialog':True   

    }
    auth_url=f"{AUTH_URL}?{urllib(params)}"
    return redirect(auth_url)
     
@app.route('/callback') 
def index():
    if 'error' in requests.args:
        return jsonify({"error": requests.args['error']}) 
    if 'code' in requests.args:
        req_body = {
            'code':requests.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret':CLIENT_SECRET
        }
        response=requests.post(TOKEN_URL,data=req_body)
        token_info=response.json()

        session['access_token']=token_info['access_token']
        session['refresh_token']=token_info['refresh_token']
        session['expires_at']=datetime.now.timestamp()+token_info['expires_in']


        return redirect('/playlists')
    

@app.route('/playlists')
def get_playlists():
    if 'access_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp()>session['expires_at']:
        return redirect('/refresh-token')
    
    headers={
        'Authorization': f"Bearer {session['access_token']}" 
    }

    response = requests.get(API_BASE_URL)