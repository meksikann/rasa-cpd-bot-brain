## create calendar event 01
* greet
    - utter_how_can_help
* create_event
    - utter_on_it
    - utter_ask_event_name
* inform{"event_name": "book room two"}
    - utter_on_it
    - action_create_event
    - utter_event_saved
* thank
    - utter_thank
* bye
    - utter_bye


## create calendar event 02
* create_event
    - utter_on_it
    - utter_ask_event_name
* inform{"event_name": "room two"}
    - utter_on_it
    - action_create_event
    - utter_event_saved
* thank
    - utter_thank
* bye
    - utter_bye


## deny create calendar event 02
* create_event
    - utter_on_it
    - utter_ask_event_name
* deny
    - utter_bye
