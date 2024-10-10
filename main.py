from boxdraw import drawbox

x = "Lilith"
y = "Witch"
drawbox('TOP', False, 42+len(x), 2, f"Name: {x}", 30+len(x), "Level:")
drawbox('MIDDLE', False, 42+len(x), 2, f"Class: {y}", 12+len(x), "Archytype")
drawbox('BOTTOM', True, 42+len(x), 2, f"Name: {x}", 12+len(x), "Level:")
drawbox('SINGLE', True, 42+len(x), 2, f"Name: {x}", 12+len(x), "Level:")




