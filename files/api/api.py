from serpent.game_api import GameAPI
from serpent.input_controller import MouseEvent, MouseEvents, MouseButton
from serpent.input_controller import InputController, MouseButton

class Bullet_HeavenAPI(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)
        self.game_inputs = {
            "MOVEMENT": {
                "Secondary weapon": [
                    MouseEvent(MouseEvents.CLICK, MouseButton.LEFT),
                    MouseEvent(MouseEvents.CLICK, MouseButton.LEFT)
                    ],
                "Bomb": [
                    MouseEvent(MouseEvents.CLICK, MouseButton.RIGHT)
                ],
                "Nothing": []
            },
        }

        # Let's use a small range while we are testing
        values = [a for a in range(34,1220)]
        dictionary = dict()
        for i in range(34,1220):
            dictionary[str(i)] = values[i-34]

        self.game_inputs2 = {
            "MOUSE": dictionary
        }


    def my_api_function(self):
        pass

    class MyAPINamespace:

        @classmethod
        def my_namespaced_api_function(cls):
            api = Bullet_HeavenAPI.instance
