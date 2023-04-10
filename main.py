import requests


print('Задача №1'.center(60))
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
data = requests.get(url).json()
dict_superheros = {'Hulk': '', 'Captain America': '', 'Thanos': ''}
for i in data:
    if i['name'] in dict_superheros.keys():
        dict_superheros[i['name']] = i['powerstats']['intelligence']
print(f'Самый умный супергерой из {", ".join(list(dict_superheros))} - это '
      f'{max(dict_superheros)} с интеллектом {dict_superheros[max(dict_superheros)]}!', end='\n\n')

print('Задача №2'.center(60))

TOKEN = ''

upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
params = {'path': 'Шпора по GIT.txt', 'overwrite': "true"}
data = requests.get(upload_url, headers=headers, params=params).json()
url = data.get('href')  # ссылка для загрузки
response = requests.put(url, data=open('Шпора по GIT.txt', 'rb'))
if response.status_code == 201:
    print('Success')

