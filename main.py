from tkinter import *
from gui.main_window import MainWindow
from gui.select_batle_view import SelectBatleView
window =Tk()
main_window = MainWindow(window)
main_window.open_view(SelectBatleView(main_window))
window.title("gra")
window.mainloop()



