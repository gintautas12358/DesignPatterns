from Netflix_Newsletter_server import NetflixNewsletterServer
from User_client import UserClient
from Fancy_user_client import FancyUserClient

netflix_server = NetflixNewsletterServer()

users = []
for i in range(2):
    user = UserClient(f"user {i}" , netflix_server)
    users.append(user)

for i in range(2,5):
    user = FancyUserClient(f"user {i}" , netflix_server)
    users.append(user)

print(netflix_server.observer_list)

netflix_server.add_news("stock", 54)
netflix_server.add_news("sci-fi", "Star wars 4")


netflix_server.removeObserver("3")
print(netflix_server.observer_list)

