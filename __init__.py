from mycroft import MycroftSkill, intent_file_handler


class LonelySkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.lonely.intent')
    def handle_skill_lonely(self, message):
        self.speak_dialog('skill.lonely')


def create_skill():
    return LonelySkill()

