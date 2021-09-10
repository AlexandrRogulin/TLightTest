import json
import requests
# from django.core.management.base import BaseCommand
# from posts.models import Post

# response = requests.get("http://jsonplaceholder.typicode.com/users")
# users = json.loads(response.text)
# print(users == response.json())
# print(type(users))
# print(users)



dict_users = {}
response_users = requests.get("http://jsonplaceholder.typicode.com/users")
users = response_users.json()
for i in users:
	if 'name' in i:
		dict_users[i['id']] = [i['name']]
print(dict_users)
# print(users)
    # dict_posts ={}
    # response_posts = requests.get("http://jsonplaceholder.typicode.com/posts")
    # posts = response_posts.json()
    # for j in posts:
    #     if 'userId' in j:
    #         dict_posts[j['userId']]= [j['title'], j['body']]
#print(dict_posts)
#print(posts)

# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         with open('recipes/data/ingredients.csv', encoding='utf-8') as file:
#             for row in file:
#                 # do something with row data.
#                 userId, title, body = row
#                 Post.objects.get_or_create(userId=userId, title=title, body=body)
#                 # print(name + ', ' + unit)

'''
for k, v in dict_posts.items():
    if k in dict_users:
        dict_users[k].extend(v)
    else:
        dict_users[k] = v

dict_results = dict_users
'''
# print(dict_results)
# print(dict_results[10])