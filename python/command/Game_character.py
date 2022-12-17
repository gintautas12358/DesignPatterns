from Skills import NoSkill

class GameCharacter():

    def __init__(self) -> None:
        self.skill_boxes = [NoSkill()] * 4
        self.last_skill_index = 0

    def learn_skill(self, skill):
        if self.last_skill_index < 4:
            self.skill_boxes[self.last_skill_index] = skill
            self.last_skill_index += 1
        else:
            print("No space for new skills")

    def use_skill(self, box_number):
        self.skill_boxes[box_number].execute()

