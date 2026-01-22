from evennia import Command
from evennia.utils import evform

class SheetCmd(Command):
    """
    Shows your character sheet or that of another character.

    Usage:
        sheet [<character>]
    """
    key = "sheet"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            "Character's own sheet"
            char = self.caller
        else:
            "Another sheet, players can see their own characters' sheets, otherwise need to be (either PlayerHelper or Wizard, unsure)"
            char = self.caller

        form = evform.EvForm("forms/sheet.py")
        """
        1 Character info
        2 Prof Bonus/Inspiration/Perception
        3 STR
        4 DEX
        5 CON
        6 INT
        7 WIS
        8 CHA
        9 AC
        0 Init
        A Speed
        B HP
        C Death Saves
        D Proficiencies
        """

        info = ('{name}\n'
                '{race}\n'
                '{clas}\n'
                '{align}\n'
                '{bg}\n'
                '{level} ({xp}/{xptnl}XP)')

        def proficiency(prof):
            if prof:
                return 'o'
            else:
                return ' '

        strength = ('STRENGTH                  [{attr:>2d}] [{attrbon:>+2d}]\n'
                    'Saving Throws              [{attrsavprof}] [{attrsavbon:>+2d}]\n'
                    'Athletics                  [{athlprof}] [{athlbon:>+2d}]')

        dexterity = ('DEXTIRITY                 [{attr:>2d}] [{attrbon:>+2d}]\n'
                     'Saving Throws              [{attrsavprof}] [{attrsavbon:>+2d}]\n'
                     'Acrobatics                 [{acroprof}] [{acrobon:>+2d}]\n'
                     'Sleight of Hand            [{sohprof}] [{sohbon:>+2d}]\n'
                     'Stealth                    [{steprof}] [{stebon:>+2d}]')

        constitution = ('CONSTITUTION              [{attr:>2d}] [{attrbon:>+2d}]\n'
                        'Saving Throws              [{attrsavprof}] [{attrsavbon:>+2d}]')

        intelligence = ('INTELLIGENCE              [{attr:>2d}] [{attrbon:>+2d}]\n'
                        'Saving Throws              [{attrsavprof}] [{attrsavbon:>+2d}]\n'
                        'Arcana                     [{arcprof}] [{arcbon:>+2d}]\n'
                        'History                    [{hisprof}] [{hisbon:>+2d}]\n'
                        'Investigation              [{invprof}] [{invbon:>+2d}]\n'
                        'Nature                     [{natprof}] [{natbon:>+2d}]\n'
                        'Religion                   [{relprof}] [{relbon:>+2d}]')

        wisdom = ('WISDOM                    [{attr:>2d}] [{attrbon:>+2d}]\n'
                  'Saving Throws              [{attrsavprof}] [{attrsavbon:>+2d}]\n'
                  'Animal Handling            [{aniprof}] [{anibon:>+2d}]\n'
                  'Insight                    [{insprof}] [{insbon:>+2d}]\n'
                  'Medicine                   [{medprof}] [{medbon:>+2d}]\n'
                  'Perception                 [{perprof}] [{perbon:>+2d}]\n'
                  'Survival                   [{surprof}] [{surbon:>+2d}]')

        charisma = ('CHARISMA                  [{attr:>2d}] [{attrbon:>+2d}]\n'
                    'Saving Throws              [{attrsavprof}] [{attrsavbon:>+2d}]\n'
                    'Deception                  [{decprof}] [{decbon:>+2d}]\n'
                    'Intimidation               [{intprof}] [{intbon:>+2d}]\n'
                    'Performance                [{perfprof}] [{perfbon:>+2d}]\n'
                    'Persuasion                 [{persprof}] [{persbon:>+2d}]')

        form.map(cells = {1: info.format(name=char.get_name(),
                             race=char.get_race(),
                             clas=char.get_class(),
                             align=char.get_alignment(),
                             bg=char.get_background(),
                             level=char.get_level(),
                             xp=char.get_xp(),
                             xptnl=char.get_xptnl()),
                          3: strength.format(attr=char.get_attribute_value('strength'),
                             attrbon=char.get_attribute_bonus('strength'),
                             attrsavprof=proficiency(char.has_save_proficiency('strength')),
                             attrsavbon=char.get_saving_throw_bonus('strength'),
                             athlprof=proficiency(char.has_skill_proficiency('athletics')),
                             athlbon=char.get_skill_bonus('athletics')),
                          4: dexterity.format(attr=char.get_attribute_value('dexterity'),
                             attrbon=char.get_attribute_bonus('dexterity'),
                             attrsavprof=proficiency(char.has_save_proficiency('dexterity')),
                             attrsavbon=char.get_saving_throw_bonus('dexterity'),
                             acroprof=proficiency(char.has_skill_proficiency('acrobatics')),
                             acrobon=char.get_skill_bonus('acrobatics'),
                             sohprof=proficiency(char.has_skill_proficiency('sleight of hand')),
                             sohbon=char.get_skill_bonus('sleight of hand'),
                             steprof=proficiency(char.has_skill_proficiency('stealth')),
                             stebon=char.get_skill_bonus('stealth')),
                          5: constitution.format(attr=char.get_attribute_value('constitution'),
                             attrbon=char.get_attribute_bonus('constitution'),
                             attrsavprof=proficiency(char.has_save_proficiency('constitution')),
                             attrsavbon=char.get_saving_throw_bonus('constitution')),
                          6: intelligence.format(attr=char.get_attribute_value('intelligence'),
                             attrbon=char.get_attribute_bonus('intelligence'),
                             attrsavprof=proficiency(char.has_save_proficiency('intelligence')),
                             attrsavbon=char.get_saving_throw_bonus('intelligence'),
                             arcprof=proficiency(char.has_skill_proficiency('arcana')),
                             arcbon=char.get_skill_bonus('arcana'),
                             hisprof=proficiency(char.has_skill_proficiency('history')),
                             hisbon=char.get_skill_bonus('history'),
                             invprof=proficiency(char.has_skill_proficiency('investigation')),
                             invbon=char.get_skill_bonus('investigation'),
                             natprof=proficiency(char.has_skill_proficiency('nature')),
                             natbon=char.get_skill_bonus('nature'),
                             relprof=proficiency(char.has_skill_proficiency('religion')),
                             relbon=char.get_skill_bonus('religion')),
                          7: wisdom.format(attr=char.get_attribute_value('wisdom'),
                             attrbon=char.get_attribute_bonus('wisdom'),
                             attrsavprof=proficiency(char.has_save_proficiency('wisdom')),
                             attrsavbon=char.get_saving_throw_bonus('wisdom'),
                             aniprof=proficiency(char.has_skill_proficiency('animal handling')),
                             anibon=char.get_skill_bonus('animal handling'),
                             insprof=proficiency(char.has_skill_proficiency('insight')),
                             insbon=char.get_skill_bonus('insight'),
                             medprof=proficiency(char.has_skill_proficiency('medicine')),
                             medbon=char.get_skill_bonus('medicine'),
                             perprof=proficiency(char.has_skill_proficiency('perception')),
                             perbon=char.get_skill_bonus('perception'),
                             surprof=proficiency(char.has_skill_proficiency('survival')),
                             surbon=char.get_skill_bonus('survival')),
                          8: charisma.format(attr=char.get_attribute_value('charisma'),
                             attrbon=char.get_attribute_bonus('charisma'),
                             attrsavprof=proficiency(char.has_save_proficiency('charisma')),
                             attrsavbon=char.get_saving_throw_bonus('charisma'),
                             decprof=proficiency(char.has_skill_proficiency('deception')),
                             decbon=char.get_skill_bonus('deception'),
                             intprof=proficiency(char.has_skill_proficiency('intimidation')),
                             intbon=char.get_skill_bonus('intimidation'),
                             perfprof=proficiency(char.has_skill_proficiency('performance')),
                             perfbon=char.get_skill_bonus('performance'),
                             persprof=proficiency(char.has_skill_proficiency('persuasion')),
                             persbon=char.get_skill_bonus('persuasion')),
                          9 : 0,
                          0 : 0,
                         "A": 0})

        self.msg(unicode(form).lstrip('\r\n'))
