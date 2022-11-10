import requests
import urllib3
import random


username = 'theemilydied'
password = 'BWYqVD4hnD7yRrD'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'

#Fetch the available memes
data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]



#define lists
names = ["WSP", "Ze", "Vesto", "Muesli", "Septic", "8bit", "Elwi", "Maxi", "Memey", "Blees", "Tut", "Saul", "Nite", "Sosa"]
bad_jokes = ["when child", "doing the incident", "comiting genocide", "eat balls", "at Nuremberg", "deleting the server", "nuking yugoslavia", "doing the dishes", "fucking a potato", "being gay", "eating a potato cock", "bashing poland"]

#randomize
id = random.randrange(1, 101)
text0 = random.choice(names)
text1 = random.choice(bad_jokes)

#Fetch the generated meme
URL = 'https://api.imgflip.com/caption_image'
params = {
    'username':username,
    'password':password,
    'template_id':images[id-1]['id'],
    'text0':text0,
    'text1':text1
}
response = requests.request('POST',URL,params=params).json()
print("Copy url for your meme")
print(response)

