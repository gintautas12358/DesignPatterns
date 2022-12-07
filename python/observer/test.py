from Netflix_Newsletter_server import NetflixNewsletterServer
from User_client import UserClient

netflix_server = NetflixNewsletterServer()

users = []
for i in range(5):

    user = UserClient(f"user {i}" , netflix_server)
    users.append(user)


print(netflix_server.observer_list)

netflix_server.add_news("stock", 54)
netflix_server.add_news("sci-fi", "Star wars 4")



