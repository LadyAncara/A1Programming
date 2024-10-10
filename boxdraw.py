from enum import Enum

cap = Enum, ['TOP', 'BOTTOM', 'MIDDLE', 'SINGLE']
previous = ''


def drawbox(boxcap: cap, x: int, y: int, cont: str, *div):
    # This code is kinda a nightmare but what its doing is generating a top section, a mid section and a mid section with thext that will be displayed at the top line
    boxend = ''.join(('┏', ''.join(map(lambda i: i * x, '━')), '┓'))
    boxtxt = ''.join((f'┃{cont}', ''.join(map(lambda i: i * (x - len(cont)), ' ')), '┃'))
    boxmid = ''.join(('┃', ''.join(map(lambda i: i * x, ' ')), '┃'))

    if len(div) > 0:
        for i in range(int(len(div) / 2)):
            # Lets you add sections in the div peram with the format of: `section-start-int, name-string' repeating
            boxend = boxend[:div[i * 2]] + "┳" + boxend[div[i * 2] + 1:]
            boxtxt = boxtxt[:div[i * 2]] + "┃" + div[i * 2 + 1] + boxtxt[div[i * 2] + len(div[i * 2 + 1]) + 1:]
            boxmid = boxmid[:div[i * 2]] + "┃" + boxmid[div[i * 2] + 1:]

    def printmid():
        for i in range(y):
            if i == 0:
                print(boxtxt)
            else:
                print(boxmid)

    # Dont need to generate a bottom section, edit the top depending on case
    match boxcap:
        case 'SINGLE':
            print(boxend)
            printmid()
            print(boxend.replace('┏', '┗').replace('┓', '┛').replace('┳', '┻'))
        case 'TOP':
            print(boxend)
            printmid()
        case 'MIDDLE':

            printmid()
        case 'BOTTOM':
            printmid()
            print(boxend.replace('┏', '┗').replace('┓', '┛').replace('┳', '┻'))

    previous = (boxcap, x, y, div)
