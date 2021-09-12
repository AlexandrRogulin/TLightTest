import json
import requests

'''
Парсинг информации о постах с сайта 
http://jsonplaceholder.typicode.com/posts
'''
response = requests.get("http://jsonplaceholder.typicode.com/posts")
posts = json.loads(response.text)
for item in posts:                               # Отсортируем данные 
    item['author'] = item.pop('userId')
    del item['id']
    item['title'] = item.pop('title')
    item['body'] = item.pop('body')
#print(posts)
posts_post = []                                  # Список для итогового результата
counter = 1                                      # Счетчик, который будет менять значение pk для постов
posts_dict = {}
for j in posts:                                  # Заносим в словарь необходимые данные
    post_dict = {
        "model": "posts.post",
        "pk": counter,
        "fields" : j
    }
    # print(j)
    # print()
    posts_post.append(post_dict)                 # Добавляем словарь в список
    counter += 1
#print(posts_list)

with open('myproject/posts_post.json', 'w', encoding='utf-8') as outfile:
    json.dump(posts_post, outfile)


'''
Парсинг информации о пользователях с сайта 
http://jsonplaceholder.typicode.com/users
'''
response_users = requests.get("http://jsonplaceholder.typicode.com/users")
users = json.loads(response_users.text)
for item in users:
    del item['id']
    item['name'] = item.pop('name')
    item['username'] = item.pop('username')
    item['email'] = item.pop('email')
    del item['address']
    item['phone'] = item.pop('phone')
    item['website'] = item.pop('website')
    del item['company']
#print(users)
posts_customuser = []
counter = 1
user_dict = {}
for j in users:
    user_dict = {
        "model": "posts.customuser",
        "pk": counter,
        "fields" : j
    }
    posts_customuser.append(user_dict)
    counter += 1
#print(posts_customuser)
with open('myproject/posts_customuser.json', 'w', encoding='utf-8') as outfile:
    json.dump(posts_customuser, outfile)