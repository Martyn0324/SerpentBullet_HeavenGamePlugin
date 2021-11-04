from serpent.game import Game

from .api.api import Bullet_HeavenAPI

from serpent.utilities import Singleton




class SerpentBullet_HeavenGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Bullet Heaven 2"

        kwargs["app_id"] = "412670"
        kwargs["app_args"] = None
        

        super().__init__(**kwargs)

        self.api_class = Bullet_HeavenAPI
        self.api_instance = None

        self.frame_transformation_pipeline_string = "RESIZE:12x12"

    @property
    def screen_regions(self):
        regions = {
            #"Score": (100, 0, 144, 248)
            "Score": (36, 154, 74, 418)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
