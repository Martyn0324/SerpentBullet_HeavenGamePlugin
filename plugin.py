import offshoot


class SerpentBullet_HeavenGamePlugin(offshoot.Plugin):
    name = "SerpentBullet_HeavenGamePlugin"
    version = "0.1.0"

    libraries = []

    files = [
        {"path": "serpent_Bullet_Heaven_game.py", "pluggable": "Game"}
    ]

    config = {
        "fps": 2
    }

    @classmethod
    def on_install(cls):
        print("\n\n%s was installed successfully!" % cls.__name__)

    @classmethod
    def on_uninstall(cls):
        print("\n\n%s was uninstalled successfully!" % cls.__name__)


if __name__ == "__main__":
    offshoot.executable_hook(SerpentBullet_HeavenGamePlugin)
