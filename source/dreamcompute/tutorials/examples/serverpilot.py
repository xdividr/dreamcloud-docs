# step-1
import requests
import shade
import json

client_id = 'CLIENT ID GOES HERE'
api_key = 'API KEY GOES HERE'
server_name = 'serverpilot'

# step-2
server_info = json.loads('{"name": "' + server_name + '"}')
server_endpoint = 'https://api.serverpilot.io/v1/servers'

session = requests.Session()
session.auth = (client_id, api_key)
session.headers = {'Content-Type': 'application/json'}
response_raw = session.post(server_endpoint, json.dumps(server_info))
print(response_raw.content)
response_json = json.loads(response_raw.content)

# step-3
cloud_init='''#!/bin/bash
sudo apt-get update && sudo apt-get -y install wget ca-certificates && \
sudo wget -nv -O serverpilot-installer \
https://download.serverpilot.io/serverpilot-installer && \
sudo sh serverpilot-installer \
--server-id={serverid} \
--server-apikey={serverapikey}
'''.format(serverid=response_json['data']['id'], serverapikey=response_json['data']['apikey'])

# step-4
image_name = 'Ubuntu-16.04'
flavor_id = '100'
key_name = 'KEY NAME GOES HERE'

# step-5
conn = shade.OpenStackCloud()

image = conn.get_image(image_name)
conn.create_server(image=image, flavor=flavor_id,
        name=server_info['name'], network='public', userdata=cloud_init,
        key_name=key_name)
