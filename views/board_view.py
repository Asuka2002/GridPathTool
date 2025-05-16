import tkinter as tk
from tkinter import ttk
from models.board_model import *
from config import *

class BoardView():
    def __init__(self, root, board_model: BoardModel):
        self.root = root
        self.board_model = board_model
        self.canvas = tk.Canvas(root, width=1000, height=1000)
        self.canvas.place(x=0, y=0)
        self.canvas.pack()
        
        self.dark_color = "#91AF91"
        self.light_color = "#B6DFB6"
        
        # 盤面の描画
        self.draw()
        
    # 座標からマス(i, j)を取得
    def get_mass_from_coord(self, x, y):
        if x < SPACE or x > SPACE + SQUARE_SIZE * self.board_model.row or y < SPACE or y > SPACE + SQUARE_SIZE * self.board_model.col:
            return (-1, -1)
        i = (x - SPACE) // SQUARE_SIZE
        j = (y - SPACE) // SQUARE_SIZE
        return (i, j)
        
        # パスも含めた盤面の描画
    def draw(self) -> None:
        self.clear_board() # 盤面のクリア
        self.draw_board()  # 盤面の描画
        self.draw_pass()   # パスの描画
        
    def clear_board(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 1001, 1001, fill = self.light_color)
    
    # マス(x, y)の色を塗る、現在は濃い緑のみを塗る
    def color_mass(self, x, y):
        self.canvas.create_rectangle(SPACE + SQUARE_SIZE*x, SPACE + SQUARE_SIZE*y,
                                     SPACE + SQUARE_SIZE*(x+1), SPACE + SQUARE_SIZE*(y+1), fill = self.dark_color)
    
    # パスの描画
    def draw_pass(self):
        pass_model = self.board_model.pass_model
        prev_v = None
        
        # パスを描画
        for v in pass_model:
            self.color_mass(v[0], v[1])
            if prev_v is not None:        
                start_x = SPACE + SQUARE_SIZE*prev_v[0] + SQUARE_SIZE//2
                start_y = SPACE + SQUARE_SIZE*prev_v[1] + SQUARE_SIZE//2
                goal_x = SPACE + SQUARE_SIZE*v[0] + SQUARE_SIZE//2
                goal_y = SPACE + SQUARE_SIZE*v[1] + SQUARE_SIZE//2
                self.canvas.create_line(start_x, start_y, goal_x, goal_y)
            prev_v =v
        
        # 始点の長方形を描画
        if len(pass_model) != 0:
            start = pass_model[0]
            self.canvas.create_rectangle(SPACE + SQUARE_SIZE*start[0] + SQUARE_SIZE//5, SPACE + SQUARE_SIZE*start[1] + SQUARE_SIZE//5,
                                         SPACE + SQUARE_SIZE*(start[0]+1) - SQUARE_SIZE//5, SPACE + SQUARE_SIZE*(start[1]+1) - SQUARE_SIZE//5)
        
        
    # 盤面の描画
    def draw_board(self):
        row = self.board_model.row
        col = self.board_model.col
        
        # 横線
        for i in range(row + 1):
            self.canvas.create_line(SPACE, SPACE + SQUARE_SIZE*i, SPACE + SQUARE_SIZE*col, SPACE + SQUARE_SIZE*i)

        # 縦線
        for i in range(col + 1):
            self.canvas.create_line(SPACE + SQUARE_SIZE*i, SPACE, SPACE + SQUARE_SIZE*i, SPACE + SQUARE_SIZE*row)
            
        # 盤面の記号
        for i in range(row):
            for j in range(col):
                if self.board_model.board_data[i][j] == 1:
                    self.canvas.create_oval(SPACE + SQUARE_SIZE*i + SQUARE_SIZE//5, SPACE + SQUARE_SIZE*j + SQUARE_SIZE//5,
                                            SPACE + SQUARE_SIZE*(i+1) - SQUARE_SIZE//5, SPACE + SQUARE_SIZE*(j+1) - SQUARE_SIZE//5,)
    