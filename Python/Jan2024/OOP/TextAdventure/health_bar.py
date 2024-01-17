import os

os.system("")

class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colours: dict = {"red": "\033[91m",
                     "blue": "\33[34m",
                     "green": "\033[92m",
                     "yellow": "\33[93m",
                     "default": "\033[0m"}
    
    def __init__(self, 
                 entity, 
                 length:int = 20, 
                 is_coloured = True, 
                 colour = ""):
        
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_coloured = is_coloured
        self.colour = self.colours.get(colour) or self.colours["default"]
    
    def update(self):
        self.current_value = self.entity.health

    def draw(self):
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}")
        print(f"{self.barrier}"
              f"{self.colour if self.is_coloured else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colours['default'] if self.is_coloured else ''}"
              f"{self.barrier}")