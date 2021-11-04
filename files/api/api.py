from serpent.game_api import GameAPI
from serpent.input_controller import MouseEvent, MouseEvents, MouseButton
from serpent.input_controller import InputController, MouseButton

from serpent.config import config

from redis import StrictRedis

import pickle

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


        self.game_inputs2 = {
            "MOUSE": {
                "A,1": [MouseEvent(MouseEvents.MOVE,  x=406, y=883)],
                "A,2": [MouseEvent(MouseEvents.MOVE,  x=406, y=788)],
                "A,3": [MouseEvent(MouseEvents.MOVE,  x=406, y=689)],
                "A,4": [MouseEvent(MouseEvents.MOVE,  x=406, y=600)],
                "A,5": [MouseEvent(MouseEvents.MOVE,  x=406, y=506)],
                "A,6": [MouseEvent(MouseEvents.MOVE,  x=406, y=408)],
                "A,7": [MouseEvent(MouseEvents.MOVE,  x=406, y=312)],
                "A,8": [MouseEvent(MouseEvents.MOVE,  x=406, y=215)],
                "B,1": [MouseEvent(MouseEvents.MOVE,  x=503, y=883)],
                "B,2": [MouseEvent(MouseEvents.MOVE,  x=503, y=788)],
                "B,3": [MouseEvent(MouseEvents.MOVE,  x=503, y=689)],
                "B,4": [MouseEvent(MouseEvents.MOVE,  x=503, y=600)],
                "B,5": [MouseEvent(MouseEvents.MOVE,  x=503, y=506)],
                "B,6": [MouseEvent(MouseEvents.MOVE,  x=503, y=408)],
                "B,7": [MouseEvent(MouseEvents.MOVE,  x=503, y=312)],
                "B,8": [MouseEvent(MouseEvents.MOVE,  x=503, y=215)],
                "C,1": [MouseEvent(MouseEvents.MOVE,  x=594, y=883)],
                "C,2": [MouseEvent(MouseEvents.MOVE,  x=594, y=788)],
                "C,3": [MouseEvent(MouseEvents.MOVE,  x=594, y=689)],
                "C,4": [MouseEvent(MouseEvents.MOVE,  x=594, y=600)],
                "C,5": [MouseEvent(MouseEvents.MOVE,  x=594, y=506)],
                "C,6": [MouseEvent(MouseEvents.MOVE,  x=594, y=408)],
                "C,7": [MouseEvent(MouseEvents.MOVE,  x=594, y=312)],
                "C,8": [MouseEvent(MouseEvents.MOVE,  x=594, y=215)],
                "D,1": [MouseEvent(MouseEvents.MOVE,  x=691, y=883)],
                "D,2": [MouseEvent(MouseEvents.MOVE,  x=691, y=788)],
                "D,3": [MouseEvent(MouseEvents.MOVE,  x=691, y=689)],
                "D,4": [MouseEvent(MouseEvents.MOVE,  x=691, y=600)],
                "D,5": [MouseEvent(MouseEvents.MOVE,  x=691, y=506)],
                "D,6": [MouseEvent(MouseEvents.MOVE,  x=691, y=408)],
                "D,7": [MouseEvent(MouseEvents.MOVE,  x=691, y=312)],
                "D,8": [MouseEvent(MouseEvents.MOVE,  x=691, y=215)],
                "E,1": [MouseEvent(MouseEvents.MOVE,  x=784, y=883)],
                "E,2": [MouseEvent(MouseEvents.MOVE,  x=784, y=788)],
                "E,3": [MouseEvent(MouseEvents.MOVE,  x=784, y=689)],
                "E,4": [MouseEvent(MouseEvents.MOVE,  x=784, y=600)],
                "E,5": [MouseEvent(MouseEvents.MOVE,  x=784, y=506)],
                "E,6": [MouseEvent(MouseEvents.MOVE,  x=784, y=408)],
                "E,7": [MouseEvent(MouseEvents.MOVE,  x=784, y=312)],
                "E,8": [MouseEvent(MouseEvents.MOVE,  x=784, y=215)],
                "F,1": [MouseEvent(MouseEvents.MOVE,  x=878, y=883)],
                "F,2": [MouseEvent(MouseEvents.MOVE,  x=878, y=788)],
                "F,3": [MouseEvent(MouseEvents.MOVE,  x=878, y=689)],
                "F,4": [MouseEvent(MouseEvents.MOVE,  x=878, y=600)],
                "F,5": [MouseEvent(MouseEvents.MOVE,  x=878, y=506)],
                "F,6": [MouseEvent(MouseEvents.MOVE,  x=878, y=408)],
                "F,7": [MouseEvent(MouseEvents.MOVE,  x=878, y=312)],
                "F,8": [MouseEvent(MouseEvents.MOVE,  x=878, y=215)],
                "G,1": [MouseEvent(MouseEvents.MOVE,  x=974, y=883)],
                "G,2": [MouseEvent(MouseEvents.MOVE,  x=974, y=788)],
                "G,3": [MouseEvent(MouseEvents.MOVE,  x=974, y=689)],
                "G,4": [MouseEvent(MouseEvents.MOVE,  x=974, y=600)],
                "G,5": [MouseEvent(MouseEvents.MOVE,  x=974, y=506)],
                "G,6": [MouseEvent(MouseEvents.MOVE,  x=974, y=408)],
                "G,7": [MouseEvent(MouseEvents.MOVE,  x=974, y=312)],
                "G,8": [MouseEvent(MouseEvents.MOVE,  x=974, y=215)],
                "H,1": [MouseEvent(MouseEvents.MOVE,  x=1066, y=883)],
                "H,2": [MouseEvent(MouseEvents.MOVE,  x=1066, y=788)],
                "H,3": [MouseEvent(MouseEvents.MOVE,  x=1066, y=689)],
                "H,4": [MouseEvent(MouseEvents.MOVE,  x=1066, y=600)],
                "H,5": [MouseEvent(MouseEvents.MOVE,  x=1066, y=506)],
                "H,6": [MouseEvent(MouseEvents.MOVE,  x=1066, y=408)],
                "H,7": [MouseEvent(MouseEvents.MOVE,  x=1066, y=312)],
                "H,8": [MouseEvent(MouseEvents.MOVE,  x=1066, y=215)]
            }
        }


    def my_api_function(self):
        pass

    class MyAPINamespace:

        @classmethod
        def my_namespaced_api_function(cls):
            api = Bullet_HeavenAPI.instance