import re
from imgur_python import Imgur

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

md_original = []
with open('Readme.md') as f:
    md_original = f.readlines()

imgur = Imgur(conf)

hashes = [d['id'] for d in imgur.album_images('wwcN6Rm')['response']['data']]
imgs = [f'{i:03d}' for i in range(1, 53)]
img2hash = dict(zip(imgs, hashes))

# original img url: ![title](./xxx.png)
#  xxx: 3 digits number
# new img url: ![title](https://i.imgur.com/yyyyyy.png)
#  yyyyyy: img hash

img_line = re.compile(r'!\[.*\]\((\./(\d{3})\.png)\)')
md_new = []
for line in md_original:
    if line.startswith('!['):
        img_path = img_line.search(line).group(1)
        img_name = img_line.search(line).group(2)
        img_hash = img2hash[img_name]
        line = line.replace(img_path, f'https://i.imgur.com/{img_hash}.png')

with open('Readme_new.md', 'w') as f:
    f.writelines(md_new)
