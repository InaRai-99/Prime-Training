# Mix RGB color tuples

color1 = (255, 0, 0)   
color2 = (0, 0, 255)
ratio = 0.3
mixed = ()

for i in range(3):
    component = int(color1[i] * ratio + color2[i] * (1 - ratio))
    mixed += (component,)

print(f"Red: {color1}")
print(f"Blue: {color2}")
print(f"Mixed ({int(ratio*100)}% red): {mixed}")