from random import randint


class Scene(object):

    def enter(self):
        print("hi")
        exit(1)


class CentralCoridor(Scene):
    def enter(self):
        print("action: piu, run, kidding")
        action = raw_input("> ")
        if action == "piu":
            print ("you killed")
            return "death"
        elif action == "run":
            return "death"
        elif action == "kidding":
            print ("To Tell him kidding :)")
            return "laser_weapon_armory"
        else:
            print "this no action"
            return "central_corridor"


class Death(Scene):

    quips = [
        "You died.",
        "Nice try",
        "Failed."
    ]

    def enter(self):
        print (Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class TheFuelcell(Scene):
    def enter(self):
        print("You setup amory! BUH")
        print ("drop_a_bomb", "setup bomb", "your choice")
        action = raw_input("> ")
        if action == "drop_a_bomb":
            return "death"
        elif action == "setup bomb":
            return "escape_pod"
        else:
            print "This no action"
            return "the_fuelcell"


class LaserWeaponArmory(Scene):
    def enter(self):
        code = "%d %d %d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        print (code)
        print ("You see armory. You could find right code (3 numbers)")

        guess = raw_input("[keypad]> ")
        guesses = 0

        while int(guess != code) and guesses < 10:
            if guess > code:
                print ("your guess > code. Doing <")
            else:
                print ("your guess < code. Doing >")
            print ("VZHIK")
            guesses += 1
            guess = raw_input("[keypad]> ")
        if guess == code:
            print ("You run to the fuel cell. You saved")
            return "the_fuelcell"
        else:
            print ("You died. ")
            return "death"


class EscapePod(Scene):
    def enter(self):
        print ("Find right number capsule ( 1-4) ")
        good_pod = randint(1, 5)
        print (good_pod)
        guess = raw_input("[pod #]> ")

        if guess != good_pod:
            return "death"
        else:
            print ("You saved")
            return "finished"


class Finished(Scene):
    def enter(self):
        print ("You win!")
        return "finished"
