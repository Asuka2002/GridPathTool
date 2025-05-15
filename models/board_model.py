from .simple_path_model import *

class BoardModel():
    def __init__(self, row, col) -> None:                     # tk.Canvas ここにいろいろ書いていく
        self.row = row                              # 縦数
        self.col = col                              # 横数
        self.pass_data = SimplePassModel(row, col)   # パスのデータ

    ###########################################
    # 設定
    ###########################################

    # パスのセット
    def set_pass(self, p: list) -> None:
        self.pass_data.set_newpass(p)
        return 
    
    def add_point(self, x:int, y:int) -> bool:
        return self.pass_data.add_v(x, y)