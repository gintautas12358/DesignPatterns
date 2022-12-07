class ObserverInterface:

    def __init__(self) -> None:
        self.current_news = None

    def update(self, news):
        self.current_news = news
    