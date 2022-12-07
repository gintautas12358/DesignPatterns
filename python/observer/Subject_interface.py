class SubjectInterface:

    def __init__(self) -> None:
        self.observer_list = {}

    def addObserver(self, ob):
        self.observer_list["001"] = ob

    def removeObserver(self, id):
        self.observer_list.popitem(id)

    def notify(self):
        for ob in self.observer_list.items():
            ob.update()