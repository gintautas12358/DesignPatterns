from Gun_interface import GunInterface

class Rifle(GunInterface):

    def __init__(self) -> None:
        super().__init__()
        self.magazine_size = 4
        self.bullet_count = 0

    def load(self):
        self.bullet_count = self.magazine_size
        print(".... magazine loaded.")

    def shoot(self, target):
        if self.bullet_count:
            self.bullet_count = self.bullet_count - 1
            print("BAM!")
            target.got_shoted()
        else:
            print("Out of bullets")
            self.load()
            