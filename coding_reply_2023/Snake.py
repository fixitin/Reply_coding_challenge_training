import uuid


class Snake:
    
    def __init__(self, name):
        self.uuid = uuid.uuid4()
        self.pos_X = 0
        self.pos_Y = 0
        self.name = ""
        
        
    def get_name(self):
        return self.name
    
    def set_position(self, x, y):
        self.pos_X = x
        self.pos_Y = y
        
    def get_position(self):
        return [self.pos_X, self.pos_Y]
    
    def get_uuid():
        return self.uuid