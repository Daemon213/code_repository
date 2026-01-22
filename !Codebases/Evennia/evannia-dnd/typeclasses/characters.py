"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move - Launches the "look" command after every move.
    at_post_unpuppet(player) -  when Player disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Player has disconnected"
                    to the room.
    at_pre_puppet - Just before Player re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "PlayerName has entered the game" to the room.

    """
    _skills = {"athletics": "strength",
               "acrobatics": "dexterity",
               "sleight of hand": "dexterity",
               "stealth": "dexterity",
               "arcana": "intelligence",
               "history": "intelligence",
               "investigation": "intelligence",
               "nature": "intelligence",
               "religion": "intelligence",
               "animal handling": "wisdom",
               "insight": "wisdom",
               "medicine": "wisdom",
               "perception": "wisdom",
               "survival": "wisdom",
               "deception": "charisma",
               "intimidation": "charisma",
               "performance": "charisma",
               "persuasion": "charisma"}

    def at_object_creation(self):
        self.db.attributes = {"strength": 0,
                              "dexterity": 0,
                              "constitution": 0,
                              "intelligence": 0,
                              "wisdom": 0,
                              "charisma": 0}
        self.db.skillprofs =  {"athletics": False,
                               "acrobatics": False,
                               "sleight of hand": False,
                               "stealth": False,
                               "arcana": False,
                               "history": False,
                               "investigation": False,
                               "nature": False,
                               "religion": False,
                               "animal handling": False,
                               "insight": False,
                               "medicine": False,
                               "perception": False,
                               "survival": False,
                               "deception": False,
                               "intimidation": False,
                               "performance": False,
                               "persuasion": False}

        self.db.saveprofs = {"strength": False,
                             "dexterity": False,
                             "constitution": False,
                             "intelligence": False,
                             "wisdom": False,
                             "charisma": False}
        self.db.level = 1

    def proficiency_bonus(self):
        return 2

    def get_attribute_value(self, attribute):
        return self.db.attributes[attribute]

    def get_attribute_bonus(self, attribute):
        return (self.get_attribute_value(attribute) - 10) / 2

    def has_skill_proficiency(self, skill):
        return self.db.skillprofs[skill]

    def has_save_proficiency(self, attribute):
        return self.db.saveprofs[attribute]

    def get_skill_bonus(self, skill):
        if not self._skills[skill]:
            raise TypeError(skill + ' is not a skill.')
        else:
            bonus = self.get_attribute_bonus(self._skills[skill])
            if self.db.skillprofs[skill]:
                bonus = bonus + self.proficiency_bonus()
            return bonus

    def get_saving_throw_bonus(self, attribute):
        bonus = self.get_attribute_bonus(attribute)
        if self.db.saveprofs[attribute]:
            bonus = bonus + self.proficiency_bonus()
        return bonus

    def get_name(self):
        return self.name

    def get_race(self):
        if not self.db.race:
            return 'Raceless'
        else:
            return self.db.race

    def get_class(self):
        if not self.db.clas:
            return 'Classless'
        else:
            return self.db.clas

    def get_alignment(self):
        if not self.db.align:
            return 'True Neutral'
        else:
            return self.db.align

    def get_background(self):
        if not self.db.bg:
            return 'Wanderer'
        else:
            return self.db.bg

    def get_level(self):
        if not self.db.level:
            return 0
        else:
            return self.db.level

    def get_xp(self):
        if not self.db.xp:
            return 0
        else:
            return self.db.xp

    def get_xptnl(self):
        return 0

    def get_weight(self):
        return reduce(lambda x, y: x+y.get_weight(),self.contents)

    def get_carry_limit(self):
        return 15 * self.get_attribute_value('strength')
