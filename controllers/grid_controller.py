import tkinter as tk
from models.board_model import *
from views.board_view import *

class GridController():
    def __init__(self, board_model: BoardModel, board_view: BoardView):
        self.board_model = board_model
        self.board_view = board_view
        self.pass_model = board_model.pass_model
        self.canvas = board_view.canvas
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Button1-Motion>", self.on_drag)
        self.canvas.bind_all("<Control-z>", self.on_undo)
        self.canvas.bind("Double-Button-1>", self.on_double_click)        
    
    def on_click(self, event):
        v = self.board_view.get_mass_from_coord(event.x, event.y)
        if len(self.pass_model) == 0:
            self.pass_model.add_v(v[0], v[1])
            self.prev_v = v
        elif self.pass_model.get_end() == v:
            self.prev_v = v
        else:
            self.prev_v = (-1, -1)
    
    def on_drag(self, event):
        
        v = self.board_view.get_mass_from_coord(event.x, event.y)
        if self.prev_v != (-1, -1) and self.prev_v != v:
            try:
                self.pass_model.add_v(v[0], v[1])
            except Exception:
                return
            self.board_view.draw()
            self.prev_v = v
            
    def on_undo(self, event):
        if len(self.pass_model) == 0:
            return
        self.pass_model.pop()
        self.board_view.draw()
        
        
    def on_double_click(self, event):
        print(event.x, event.y)
        v = self.board_view.get_mass_from_coord(event.x, event.y)
        if v == (-1, -1):
            return
        self.board_model.chenge_next_board_data(v[0], v[1])
        self.board_view.draw()
        
