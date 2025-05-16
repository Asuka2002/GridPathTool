import tkinter as tk
from tkinter import ttk
from config import *
from models.board_model import *
from views.board_view import *
from controllers.grid_controller import *

class GridPathTool():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Grid Path Tool")
        
        # ウィンドウのサイズを指定
        window_size_pos = f"{INIT_WINDOW_WIDTH}x{INIT_WINDOW_HEIGHT}+{INIT_WINDOW_POS_X}+{INIT_WINDOW_POS_Y}"
        self.root.geometry(window_size_pos)
        
        # ウィンドウの最小サイズを指定
        self.root.minsize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)
        
        # モデル作成
        self.board_model = BoardModel(15, 15)
        
        # ビュー作成
        self.board_view = BoardView(self.root, self.board_model)
        
        # コントローラー作成
        self.grid_controller = GridController(self.board_model, self.board_view)       
    
    
        self.root.mainloop()

if __name__ == "__main__":
    grid_path_tool = GridPathTool()