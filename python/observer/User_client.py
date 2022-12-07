from Subject_interface import SubjectInterface

class UserClient(SubjectInterface):

    def __init__(self, server) -> None:
        self.netflix_newsletter_server = server

    def read_news(self):
        print(self.last_news)