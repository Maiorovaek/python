from Engine import Engine
from Scenes import CentralCoridor, Death, LaserWeaponArmory, EscapePod, Finished, TheFuelcell


class Map(object):

    scenes = {
        "central_corridor": CentralCoridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_fuelcell": TheFuelcell(),
        "escape_pod": EscapePod(),
        "finished": Finished(),
        "death": Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        print ("Next scene")
        return val

    def opening_scene(self):
        print ("Openning scene ...")
        return self.next_scene(self.start_scene)


if __name__ == '__main__':
    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()

