class ObjectBase:
    pass

class PosI:
    def __init__(self,x:int, y:int):
        self.x=x
        self.y=y

class PosF:
    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y
    def toPosI(self)->PosI:
        return PosI(int(self.x),int(self.y))
        
    def __add__(self, trg):
        return PosF(self.x+trg.x, self.y+trg.y)
    pass

class VecF(PosF):
    def __init(self,x:float,y:float):
        super().__init__(x,y)


def main():
    pass

if __name__ == '__main__':
    main()
