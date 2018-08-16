from rasa_core.actions import Action


class CreateEvent(Action):

    def name(self):
        # you can then use action_example in your stories
        return "action_create_event"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        return []

class RemoveEvent(Action):

    def name(self):
        # you can then use action_example in your stories
        return "action_remove_event"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        return []
