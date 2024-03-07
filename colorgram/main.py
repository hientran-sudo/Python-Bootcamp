import colorgram

list = []
colors = colorgram.extract('R.jpg', 6)
for i in range(6):    
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    list.append((r,g,b))
print(list)
