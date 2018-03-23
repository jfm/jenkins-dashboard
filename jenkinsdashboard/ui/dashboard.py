from asciimatics.widgets import Frame, Layout
from asciimatics.exceptions import StopApplication


class Dashboard(Frame):
    def __init__(self, screen, jenkins):
        super(Dashboard, self).__init__(screen,
                                        screen.height,
                                        screen.width,
                                        on_load=self._reload_list,
                                        hover_focus=True,
                                        title="Joblist")

        layout = Layout([1, 1])
        self.add_layout(layout)

    def _reload_list(self):
        pass

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")
