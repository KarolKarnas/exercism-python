YEAR = 60 * 60 * 24 * 365.25

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(self.seconds / (0.2408467 * YEAR), 2)
    
    def on_venus(self):
        return round(self.seconds / (0.61519726 * YEAR), 2)
    
    def on_earth(self):
        return round(self.seconds / (1.0 * YEAR), 2)

    def on_mars(self):
        return round(self.seconds / (1.8808158 * YEAR), 2)

    def on_jupiter(self):
        return round(self.seconds / (11.862615 * YEAR), 2)
    
    def on_saturn(self):
        return round(self.seconds / (29.447498 * YEAR), 2)
    
    def on_uranus(self):
        return round(self.seconds / (84.016846 * YEAR), 2)

    def on_neptune(self):
        return round(self.seconds / (164.79132  * YEAR), 2)
    
x=2121
y=32332

a = [y, x]
b = a

m = type(x)
n = type(y)
    
print(id(x))
print(id(y))
print(y is x)    
print(a is b)
print(id(m))
print(id(n))