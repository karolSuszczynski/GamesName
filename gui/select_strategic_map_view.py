from gui.view_type import ViewType
from gui.abstract_select_from_list_view import AbstractSelectFromListView

class SelectStrategicMapView(AbstractSelectFromListView):
    AVAILABLE_MAPS = [
        ("Random map 10x10", "rand_10_10"),
    ]

    def __init__(self, main_window):
        super().__init__(main_window, self.AVAILABLE_MAPS)

    def on_button_click(self, id):
        map = self.AVAILABLE_MAPS[id]
        print(f"you clicked at {id} :   {map[0]}")

        strategic_view = self.main_window.views[ViewType.STRATEGIC_MAP_VIEW]
        strategic_view.set_strategic_map(map[1].get_battlefield())
        self.main_window.open_view(ViewType.STRATEGIC_MAP_VIEW)