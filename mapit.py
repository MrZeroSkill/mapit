# To run mapitools via source, you will need your own API key. Go to mcprofile.io, sign up, generate an API key, and insert it below.
import requests
def run():
    name = input('Username Lookup: ')
    data = requests.get('https://mcprofile.io/api/v1/java/username/' + name, headers={'x-api-key': ''}) # Insert your MCProfile API Key here!
    try:
        data.json()['username']
        print('This username is taken.')
    except:
        print('This username is available!')
    run()

run()