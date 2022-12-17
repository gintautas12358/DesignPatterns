from Game_character import GameCharacter
from Skills import *

character = GameCharacter()

print(character.skill_boxes)
character.learn_skill(MoveForwardSkill())
character.learn_skill(SwordSwingSkill())
character.learn_skill(ForwardSwordSwing())

print(character.skill_boxes)

for i in range(4):
    character.use_skill(i)
    print()
