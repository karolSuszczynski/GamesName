from tkinter import *
from PIL import Image, ImageTk
from maps.randomap import RandomMap
from maps.armyduel import ArmyDuelMap
from maps.cavalry_duel import CavalryDuelMap
from maps.archersduel import ArchersDuelMap
from maps.betterarmies import BetterArmiesMap
from maps.marcelsmap import MarcelsMap

BOARD_WIDTH = 16
BOARD_HEIGT = 11

window =Tk()
#current_map=RandomMap(BOARD_WIDTH, BOARD_HEIGT)
#current_map=ArmyDuelMap()
#current_map=CavalryDuelMap()
#current_map=DuelMap()
current_map=ArchersDuelMap()
#current_map=BetterArmiesMap()
#current_map=MarcelsMap()
battlefield = current_map.get_battlefield(window)
battlefield.init_batle()

window.title("gra")
window.mainloop()