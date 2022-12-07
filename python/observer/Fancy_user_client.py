from User_client import UserClient

class FancyUserClient(UserClient):

    def __init__(self, name, server) -> None:
        super().__init__(name, server)

    def display(self):
        print(f"# Current news for {self.name}:")
        for k, v in self.current_news.items():
            print(f"# On the subject {k}: {v}")
