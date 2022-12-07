from Observer_interface import ObserverInterface

class UserClient(ObserverInterface):

    def __init__(self, name, server) -> None:
        super().__init__()
        self.netflix_newsletter_server = server
        self.name = name
        self.current_news = None
        self.netflix_newsletter_server.addObserver(self)

    def update(self, news):
        self.current_news = news
        print(f"{self.name}: \n{self.current_news}")
    
    def read_news(self):
        print(self.current_news)