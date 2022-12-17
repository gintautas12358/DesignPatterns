from Skill_interface import SkillInterface

class NoSkill(SkillInterface):


    def execute(self):
        print("No skill learned")

class SwordSwingSkill(SkillInterface):

    def execute(self):
        print("Swing sword")

class MoveForwardSkill(SkillInterface):

    def execute(self):
        print("Move forward")

class MultiSkill(SkillInterface):

    def __init__(self, *skills) -> None:
        self.multi_skills = skills

    def execute(self):
        for s in self.multi_skills:
            s.execute()

class ForwardSwordSwing(MultiSkill):

    def __init__(self) -> None:
        super().__init__(MoveForwardSkill(), SwordSwingSkill())
