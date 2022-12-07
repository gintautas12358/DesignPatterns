from Observer_interface import ObserverInterface

class UserClient(ObserverInterface):

    def __init__(self, server) -> None:
        super().__init__()
        self.netflix_newsletter_server = server

    def read_news(self):
        print(self.current_news)