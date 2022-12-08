

class HunterGame:

    def __init__(self, gun, tool, target) -> None:
        self.gun = gun
        self.tool = tool
        self.target = target

    def play(self):
        print("""
        ###########   Game Starts   ###########
        
        """)
        job_done = False
        self.tool.use(self.target)
        self.gun.load()
        for i in range(10):
            self.gun.shoot(self.target)
            if not self.target.is_alive():
                job_done = True
                break

        if not job_done:
            print("Unlucky day :(")
        else:
            print("Dinner will be served!")