from Subject_interface import SubjectInterface

class NetflixNewsletterServer(SubjectInterface): 

    def __init__(self) -> None:
        self.news = {}

    def add_news(self, type, message):
        self.news[type] = message

