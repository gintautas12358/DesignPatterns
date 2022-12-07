from Observer_interface import ObserverInterface
from Display_interface import DisplayInterface

class UserClient(ObserverInterface, DisplayInterface):

    def __init__(self, name, server) -> None:
        super().__init__()
        self.netflix_newsletter_server = server
        self.name = name
        self.current_news = None
        self.netflix_newsletter_server.addObserver(self)

    def update(self, news):
        self.current_news = news
        self.display()
    
    def display(self):
        print(f"{self.name}: \n{self.current_news}")