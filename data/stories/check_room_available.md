## check_room_available_01
* greet
    - utter_how_can_help
* check_room_available {"room_name": "first conference room", "time": "2018-09-04T11:29:43.000+03:00"}
    - utter_on_it
    - action_check_room_available
    - slot {"is_room_available": "True"}
    - utter_room_is_free

## check_room_available_0101
* greet
    - utter_how_can_help
* check_room_available {"room_name": "first conference room", "time": "2018-09-04T11:29:43.000+03:00"}
    - utter_on_it
    - action_check_room_available
    - slot {"is_room_available": "False"}
    - utter_room_is_busy

## check_room_available_02
* greet
    - utter_how_can_help
* check_room_available {"room_name": "second conference room"}
    - action_check_room_available
    - slot {"is_room_available": "False"}
    - utter_room_is_busy

## check_room_available_03
* greet
    - utter_how_can_help
* check_room_available {"time": "2018-09-04T11:29:43.000+03:00"}
    - utter_ask_room_name
* inform{"room_name": "second conference room"}
    - action_check_room_available
    - slot {"is_room_available": "False"}
    - utter_room_is_busy

## check_room_available_0201
* greet
    - utter_how_can_help
* check_room_available {"room_name": "second conference room"}
    - action_check_room_available
    - slot {"is_room_available": "True"}
    - utter_room_is_free

## check_room_available_0301
* greet
    - utter_how_can_help
* check_room_available {"time": "2018-09-04T11:29:43.000+03:00"}
    - utter_ask_room_name
* inform{"room_name": "second conference room"}
    - action_check_room_available
    - slot {"is_room_available": "True"}
    - utter_room_is_free

## check_room_available_0303
* check_room_available {"room_name": "second conference room", "time": "2018-09-04T11:29:43.000+03:00"}
    - action_check_room_available
    - slot {"is_room_available": "True"}
    - utter_room_is_free

## check_room_available_0304
* check_room_available {"room_name": "second conference room", "time": "2018-09-04T11:29:43.000+03:00"}
    - action_check_room_available
    - slot {"is_room_available": "False"}
    - utter_room_is_busy
