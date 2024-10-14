from boxdraw import drawbox

x = "Lilith"
y = "Witch"
drawbox('TOP', 42+len(x), 2, f"Name: {x}", 30+len(x), "Level:")
drawbox('MIDDLE', 42+len(x), 2, f"Class: {y}", 12+len(x), "Archytype")
drawbox('BOTTOM', 42+len(x), 2, f"Name: {x}", 12+len(x), "Level:")
drawbox('SINGLE', 42+len(x), 2, f"Name: {x}", 12+len(x), "Level:")




