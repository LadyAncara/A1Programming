from boxdraw import drawbox

x = "Lilith"
y = "Witch"
prev = drawbox('TOP', [], 42+len(x), 1, f"Name: {x}", 30+len(x), "Level:")
prev = drawbox('MIDDLE', prev, 42+len(x), 1, f"Class: {y}", 12+len(x), "Archytype")
prev = drawbox('BOTTOM', prev, 42+len(x), 1, f"Name: {x}", 12+len(x), "Level:")
drawbox('SINGLE', prev, 42+len(x), 1, f"Name: {x}", 12+len(x), "Level:")




