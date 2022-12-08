from Gun_interface import GunInterface

class Rifle(GunInterface):

    def __init__(self) -> None:
        super().__init__()
        self.magazine_size = 4
        self.bullet_count = 0

    def load(self):
        self.bullet = self.magazine_size

    def shoot(self):
        if self.bullet_count:
            self.bullet_count = self.bullet_count - 1
            print("BAM!")
        else:
            print("Out of bullets")
            