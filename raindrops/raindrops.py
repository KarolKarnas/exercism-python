from enum import Enum

class Sound(Enum):
    THREE = 'Pling'
    FIVE = 'Plang'
    SEVEN = 'Plong'
    
def convert(number):
    result = ''
    is_div_three = number % 3 == 0
    is_div_five = number % 5 == 0
    is_div_seven = number % 7 == 0
    
    if (is_div_three):
        result += Sound.THREE.value
    if (is_div_five):
        result += Sound.FIVE.value
    if (is_div_seven):
        result += Sound.SEVEN.value
    if result == '':
        result = str(number)
    return  result
    
    