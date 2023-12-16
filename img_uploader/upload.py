from imgur_python import Imgur
import os
import re
import sys
conf = {
    'client_id': '527c261aeb98955',
    'client_secret': '1c9b1ac89aadd5bb2792f4092f6d26abf5c8358e',
    'access_token': '3905d3f16ddadee475305facb8986bb6b066f72c',
    'expires_in': 315360000,
    'token_type': 'bearer',
    'refresh_token': '3b0c220221b482cb82552b8094d5704b3ae2f35c',
    'account_username': 'Ewderna',
    'account_id': 92730897
}


imgur = Imgur(conf)
img2hash = {}

# print(imgur.image_upload('001.png', '001', '', '9uaZtkg'))
# exit()

album_id = 'wwcN6Rm'

print(f'Album ID: {album_id}')
for file in os.listdir(sys.argv[1]):
    if file.endswith('.png'):
        file_name = file[:-4]
        print(f'Uploading {file_name}({file})...')
        img_id = imgur.image_upload(
            filename=file, title=file_name, description='', album=album_id)['response']['data']['id']
        img2hash[file_name] = img_id
