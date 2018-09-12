from rasa_core.actions import Action
from rasa_core.events import SlotSet
# from rasa_core_sdk import Action

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

class ShowMyEvents(Action):

    def name(self):
        # you can then use action_example in your stories
        return "action_show_my_events"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        return []

class CheckRoomAvailable(Action):

    def name(self):
        # you can then use action_example in your stories
        return "action_check_room_available"

    def run(self, dispatcher, tracker, domain):
        print('test check room available action=====================>')
        # SlotSet("is_room_available", True)
        # what your action should do
        return [SlotSet("is_room_available", True)]
        # return tracker._set_slot("is_room_available", True)
