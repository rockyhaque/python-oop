# Practicing OOP

# Base Class, Parent Class, Common attribute + functionality class

# Derived Class/Child Class, uncommon attribute + functionality class


class Device:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running Laptop: {self.brand}'
    
class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    def run(self):
        return f'Running Laptop: {self.brand}'
    
    def coding(self):
        return f'Leanrning python and practicing'
    
class Phone:
    def __init__(self, dual_sim) -> None:
        self.dual_sim = dual_sim

      
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with {text}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass