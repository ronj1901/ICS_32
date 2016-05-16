# scribble applicatio


import tkinter

_BACKGROUND_COLOR = 'orange'
_LINE_COLOR  =  '#008000'


class ScribbleApplication:
    def __init__(self):
        '''
        Initializes a new scribble applucation byt creating a winfow
        and placing a Canvas widget  inside of it. However the
        application does not  execute unitil its start() method
        is called.

        '''

        self._root_window = tkinter.Tk()

        self.scribble_canvas = tkinter.Canvas(
            master = self._root_window, width = 500, height = 400,
            background = _BACKGROUND_COLOR)


        self.scribble_canvas.bind('<Button-1>', self._on_button_down)
        self.scribble_canvas.bind('<ButtonRelease-1>', self._on_button_up)
        self.scribble_canvas.bind("<Motion>", self._on_mouse_moved)

        self.scribble_canvas.pack()

        self._button_is_down = False
        self._last_x = 0
        self._lasr_y = 0

    def start(self) -> None:

        self._root_window.mainloop()

    def _on_button_down(self, event:tkinter.Event)->None:
        '''
        Event Handler is that is called when the primary mouse button
        is down within the canvas
        '''

        self._button_is_down = True
        self._last_x = event.x
        self._last_y =  event.y

    def _on_button_up(self, event :tkinter.Event):
        self._button_is_down = False

    def _on_mouse_moved(self, event: tkinter.Event) -> None:

        if self._button_is_down :
            self.scribble_canvas.create_line(
                self._last_x, self._last_y, event.x, event.y,
                fill = _LINE_COLOR)
            
        self._last_x  = event.x
        self._last_y = event.y

if __name__ ==  '__main__':
    app =  ScribbleApplication()
    app.start()
    
