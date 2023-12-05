"""Basic user interface for the order form
Creates initial window and frame.
"""
import tkinter as tk

class BasicApplication():
    INITIAL_WIDTH = 500
    INITIAL_HEIGHT = 500
    PADDING = 20

    def __init__(self):
        # create basic tk window
        self._window = tk.Tk()

        # create the associated
        self._frame = tk.Frame(self._window)

        # init main window
        self._init_main_window()

    def _init_main_window(self):
        # ensure basic setup: title
        self._window.title("Order Entry Form")

        # set window geometry
        self._window.geometry("{width}x{height}".format(
                width = BasicApplication.INITIAL_WIDTH,
                height = BasicApplication.INITIAL_HEIGHT
            )
        )
        
        # add necessary padding
        self._window["padx"] = BasicApplication.PADDING
        self._window["pady"] = BasicApplication.PADDING
        
        # prevent window resizing
        self._window.resizable(False, False)
        
        # init frame grid
        self._frame.grid(padx = 0, pady = 0)

    def run(self):
        self._window.mainloop()


if __name__ == "__main__":
    application = BasicApplication()
    application.run()
