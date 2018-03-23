from jenkinsdashboard.ui.dashboard import Dashboard
from asciimatics.scene import Scene


class UI:
    def main(self, screen, jenkins):
        scenes = [
            Scene([Dashboard(screen, jenkins)], -1, name="Main")
        ]

        screen.play(scenes, stop_on_resize=True, start_scene=scenes[0])
