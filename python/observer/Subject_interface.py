class SubjectInterface:

    def __init__(self) -> None:
        self.observer_list = {}
        self.id_counter = 0

    def addObserver(self, ob):
        self.observer_list[str(self.id_counter)] = ob
        self.id_counter = self.id_counter + 1

    def removeObserver(self, id):
        self.observer_list.popitem(id)

    def notify(self, news):
        for ob in self.observer_list.items():
            ob.update(news)

    