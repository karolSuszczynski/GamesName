from tkinter import *
from gui.i_view import IView
from gui.view_type import ViewType
from gui.abstract_select_from_list_view import AbstractSelectFromListView

class MainMenuView(AbstractSelectFromListView):
    AVAILABLE_VIEWS = [
        ("Strategic Map", ViewType.SELECT_STRATEGIC_MAP_VIEW),
        ("Battle", ViewType.SELECT_BATTLE_VIEW),
    ]

    def __init__(self, main_window):
        super().__init__(main_window, self.AVAILABLE_VIEWS, back_is_visible=False)

    def on_button_click(self, id):
        view = self.AVAILABLE_VIEWS[id]
        print(f"you clicked at {id} :   {view[0]}")

        self.main_window.open_view(view[1])