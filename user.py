class User:
    def __init__(self, name, messages_list, help_got=0, help_given=0):
        self.name = name
        self.messages_list = messages_list
        self.help_got = help_got
        self.help_given = help_given

