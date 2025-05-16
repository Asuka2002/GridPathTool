from models.simple_path_model import *

class BoardModel():
    def __init__(self, row, col) -> None:                     # tk.Canvas ここにいろいろ書いていく
        self.row = row                              # 縦数
        self.col = col                              # 横数
        self.pass_model = SimplePassModel(row, col)   # パスのデータ
        self.pass_model.clear_pass()
        self.board_data = [[0 for j in range(col)] for i in range(row)]

    ###########################################
    # 設定
    ###########################################

    # パスのセット
    def set_pass(self, p: list) -> None:
        self.pass_model.set_newpass(p)
        return 
    
    def add_point(self, x:int, y:int) -> bool:
        return self.pass_model.add_v(x, y)
    
    # ボードの状態の0, 1をもう一方に変える
    def chenge_next_board_data(self, x:int, y:int) -> None:
        self.board_data[x][y] = 1 - self.board_data[x][y]
        return
    