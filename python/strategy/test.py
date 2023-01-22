from Hunter_game import HunterGame
from Rifle import Rifle
from Elk import Elk
from python.strategy.Hunting_odour import HuntingOdour

gun = Rifle()
tool = HuntingOdour()
target = Elk()
hg = HunterGame(gun, tool, target)

hg.play()
