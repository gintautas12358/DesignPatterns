from Netflix_Newsletter_server import NetflixNewsletterServer
from User_client import UserClient

netflix_server = NetflixNewsletterServer()
netflix_server.add_news("stock", 54)
netflix_server.add_news("sci-fi", "Star wars 4")

user0 = UserClient(netflix_server)
user1 = UserClient(netflix_server)

netflix_server.addObserver(user0)
netflix_server.addObserver(user1)

user0.read_news()
user1.read_news()


