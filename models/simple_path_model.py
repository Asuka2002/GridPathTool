class SimplePassModel():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.v_list = []
        
    
    def __iter__(self):
        for i in self.v_list:
            yield i
    
    def __getitem__(self, i: int):
        if type(i) != int:
            raise Exception('i is not \"int\"')
        return self.v_list[i]
        
    def __len__(self):
        return len(self.v_list)
    
    def add_v(self, x:int, y:int) -> bool: 
        # 例外処理
        if not(0 <= x < self.row and 0 <= y < self.col):
            raise Exception(f'({x}, {y}) is out of range.')
        if (x, y) in self.v_list:
            raise Exception(f'({x}, {y}) already exists.')
        if len(self.v_list) != 0 and (abs(self.v_list[-1][0] - x) + abs(self.v_list[-1][1] - y) != 1):
            raise Exception(f'({x}, {y}) is not element of pass.')
        
        self.v_list.append((x, y))
        return True
    
    def clear_pass(self) -> None:
        self.v_list = []
        
    def get_start(self) -> tuple:
        if len(self.v_list) == 0:
            raise Exception('pass is empty')
        return self.v_list[0]
    
    def get_end(self):
        if len(self.v_list) == 0:
            raise Exception('pass is empty')
        return self.v_list[-1]
    
    def pop(self):
        if len(self.v_list) == 0:
            raise Exception('pass is empty')
        return self.v_list.pop()
        
    
    def set_newpass(self, p):
        self.clear_pass()
        for i in range(len(p)):
            try:
                self.add_v(p[i][0], p[i][1])
            except Exception as e:
                print("エラー情報:", e)
                break