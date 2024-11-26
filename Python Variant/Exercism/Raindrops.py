def convert(number):
    rainDropsNoise = ""
    
    if number % 3 == 0:
        rainDropsNoise += "Pling"
    if number % 5 == 0:
        rainDropsNoise += "Plang"
    if number % 7 == 0:
        rainDropsNoise += "Plong"
                
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    else:
        return rainDropsNoise