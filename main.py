from tkinter import *
from gui.main_window import MainWindow
from gui.view_type import ViewType

window =Tk()
window.geometry("1000x700")
main_window = MainWindow(window)

main_window.open_view(ViewType.MAIN_MENU_VIEW)
window.title("gra")
window.mainloop()



