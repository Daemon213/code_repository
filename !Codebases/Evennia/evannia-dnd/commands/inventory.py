from evennia.utils import evtable
from commands.command import Command

class InvCmd(Command):
    key = "inv"
    aliases = ['i']

    def func(self):
        table = evtable.EvTable("", "Weight")
        for obj in self.caller.contents:
            table.add_row(obj.name, obj.get_weight() + 'lb')
        self.msg(table)
        self.msg('Current weight: {0}lb Carry Limit: {1}lb'.format(caller.get_weight(), caller.get_carry_limit()))
