from Subject_interface import SubjectInterface

class NetflixNewsletterServer(SubjectInterface): 

    def __init__(self) -> None:
        super().__init__()
        self.news = {}
        self.observer_list = {}
        self.id_counter = 0

    def addObserver(self, ob):
        self.observer_list[str(self.id_counter)] = ob
        self.id_counter = self.id_counter + 1

    def removeObserver(self, id):
        self.observer_list.pop(id)

    def notify(self, news):
        for ob in self.observer_list.values():
            ob.update(news)

    def add_news(self, type, message):
        self.news[type] = message
        self.notify(self.news)
