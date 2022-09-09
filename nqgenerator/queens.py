class Queens:
    def __init__(self, n: int):
        self._queen_symbol = 'Q'
        
        self.create_chessboard(n)
        
    def create_chessboard(self, n: int):
        chessboard = []
        for x in range(n):
            row = []
            for y in range(n):
                row.append('')
            chessboard.append(row)
            
        print(chessboard)
                
                
        