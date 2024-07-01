from tkinter import *

import teachers

win = Tk()
win.title("расписание")
win.geometry("800x700")
clr = 'grey'
clr1 = '#E0E0E0'

def ramki():
    btns[0]['text'] = ''
    btns[1]['text'] = '1-2'
    btns[2]['text'] = '1-3'
    btns[3]['text'] = '1-4'
    btns[4]['text'] = '1-6'
    btns[5]['text'] = '1-7'
    btns[6]['text'] = '1-8'
    btns[7]['text'] = '1-9'

    btns[8]['text'] = '10:00-11:40'
    btns[16]['text'] = '11:50-13:30'
    btns[24]['text'] = '13:40-15:20'
    btns[32]['text'] = '15:30-17:10'
    btns[40]['text'] = '17:00-18:35'
    btns[48]['text'] = '18:40-20:15'

def monday	():
    clear()


    btns[19]['bg'] = clr
    btns[19]['text'] = "Опарина\nАндроид"

    btns[14]['bg'] = clr
    btns[14]['text'] = "Опарина\nОАП"

    btns[13]['bg'] = clr
    btns[13]['text'] = "Макеенко\nWebDev"

    btns[21]['bg'] = clr
    btns[21]['text'] = "Макеенко\nGameDev"

    btns[27]['bg'] = clr
    btns[27]['text'] = "Батаев\nJava"

    btns[22]['bg'] = clr
    btns[22]['text'] = "Батаев\nPython"

    btns[25]['bg'] = clr
    btns[25]['text'] = "Никитин\nМем стори"

    btns[9]['bg'] = clr
    btns[9]['text'] = "Никитин\nArduino"

    btns[33]['bg'] = clr
    btns[33]['text'] = "Никитин\nArduino"

    btns[10]['bg'] = clr
    btns[10]['text'] = "Сушевич\nPixel"

    btns[18]['bg'] = clr
    btns[18]['text'] = "Сушевич\nPixel"

    btns[26]['bg'] = clr
    btns[26]['text'] = "Сушевич\nPixel"

    btns[36]['bg'] = clr
    btns[36]['text'] = "Сушевич\nСис.ад."

def tuesday():
    clear()

    btns[14]['bg'] = clr
    btns[14]['text'] = "Опарина\nApp Inventor"

    btns[22]['bg'] = clr
    btns[22]['text'] = "Опарина\nApp Inventor"

    btns[27]['bg'] = clr
    btns[27]['text'] = "Макеенко\nGameDev"

    btns[35]['bg'] = clr
    btns[35]['text'] = "Макеенко\nGameDev"

    btns[45]['bg'] = clr
    btns[45]['text'] = "Черкасов\nScratch"

    btns[55]['bg'] = clr
    btns[55]['text'] = "Черкасов\nWeDo"

    btns[37]['bg'] = clr
    btns[37]['text'] = "Батаев\nC#"

    btns[18]['bg'] = clr
    btns[18]['text'] = "Михадюк\nНейросети"

    btns[9]['bg'] = clr
    btns[9]['text'] = "Сушевич\nPixel"

    btns[17]['bg'] = clr
    btns[17]['text'] = "Сушевич\nPixel"

    btns[25]['bg'] = clr
    btns[25]['text'] = "Сушевич\nPixel"

    btns[10]['bg'] = clr
    btns[10]['text'] = "Колесина\nЮП"

    btns[42]['bg'] = clr
    btns[42]['text'] = "Детина\nЮП"

def wednesday():
    clear()

    btns[13]['bg'] = clr
    btns[13]['text'] = "Опарина\nАндроид"

    btns[22]['bg'] = clr
    btns[22]['text'] = "Опарина\nАндроид"

    btns[18]['bg'] = clr
    btns[18]['text'] = "Юрис\nДизайн"

    btns[27]['bg'] = clr
    btns[27]['text'] = "Батаев\nJava"

    btns[36]['bg'] = clr
    btns[36]['text'] = "Батаев\nC++"

    btns[14]['bg'] = clr
    btns[14]['text'] = "Батаев\nPython"

    btns[12]['bg'] = clr
    btns[12]['text'] = "Никитин\nArduino"

    btns[20]['bg'] = clr
    btns[20]['text'] = "Никитин\nArduino"

    btns[29]['bg'] = clr
    btns[29]['text'] = "Никитин\nМем стори"

    btns[20]['bg'] = clr
    btns[20]['text'] = "Никитин\nArduino"

    btns[33]['bg'] = clr
    btns[33]['text'] = "Никитин\nЭГ"

    btns[41]['bg'] = clr
    btns[41]['text'] = "Никитин\nЭГ"

    btns[10]['bg'] = clr
    btns[10]['text'] = "Сушевич\nPixel"

    btns[17]['bg'] = clr
    btns[17]['text'] = "Сушевич\nPixel"

    btns[26]['bg'] = clr
    btns[26]['text'] = "Сушевич\nPixel"

    btns[39]['bg'] = clr
    btns[39]['text'] = "Ходоскин\nЮФ"

    btns[47]['bg'] = clr
    btns[47]['text'] = "Ходоскин\nЮФ"

    btns[15]['bg'] = clr
    btns[15]['text'] = "Черненкова\nМоделирование"

def thursday():
    clear()

    btns[22]['bg'] = clr
    btns[22]['text'] = "Опарина\nОАП"

    btns[18]['bg'] = clr
    btns[18]['text'] = "Юрис\nДизайн"

    btns[26]['bg'] = clr
    btns[26]['text'] = "Юрис\nЮИ"

    btns[13]['bg'] = clr
    btns[13]['text'] = "Макеенко\nWebDev"

    btns[27]['bg'] = clr
    btns[27]['text'] = "Макеенко\nWebDev"

    btns[35]['bg'] = clr
    btns[35]['text'] = "Макеенко\nWebDev"

    btns[19]['bg'] = clr
    btns[19]['text'] = "Макеенко\nGameDev"

    btns[14]['bg'] = clr
    btns[14]['text'] = "Черкасов\nEV3"

    btns[30]['bg'] = clr
    btns[30]['text'] = "Батаев\nPython"

    btns[34]['bg'] = clr
    btns[34]['text'] = "Михадюк\nJava"

    btns[44]['bg'] = clr
    btns[44]['text'] = "Мартынова\nРадиокон."

    btns[52]['bg'] = clr
    btns[52]['text'] = "Мартынова\nРадиокон."

    btns[9]['bg'] = clr
    btns[9]['text'] = "Сушевич\nPixel"

    btns[47]['bg'] = clr
    btns[47]['text'] = "Ходоскин\nЮФ"

    btns[10]['bg'] = clr
    btns[10]['text'] = "Детина\nPascal"

    btns[17]['bg'] = clr
    btns[17]['text'] = "Сушевич\nEV3"

def friday():
    clear()

    btns[13]['bg'] = clr
    btns[13]['text'] = "Макеенко\nWebDev"

    btns[27]['bg'] = clr
    btns[27]['text'] = "Макеенко\nWebDev"

    btns[19]['bg'] = clr
    btns[19]['text'] = "Макеенко\nWebDev"

    btns[22]['bg'] = clr
    btns[22]['text'] = "Батаев\nPython"

    btns[30]['bg'] = clr
    btns[30]['text'] = "Батаев\nPython"

    btns[21]['bg'] = clr
    btns[21]['text'] = "Лёвкина\nGameDev"

    btns[34]['bg'] = clr
    btns[34]['text'] = "Михадюк\nJava"

    btns[36]['bg'] = clr
    btns[36]['text'] = "Дроздов\nЭлектроника"

    btns[44]['bg'] = clr
    btns[44]['text'] = "Дроздов\nЭлектроника"

    btns[23]['bg'] = clr
    btns[23]['text'] = "Колесина\nматем"

    btns[31]['bg'] = clr
    btns[31]['text'] = "Колесина\nматем"

    btns[39]['bg'] = clr
    btns[39]['text'] = "Колесина\nматем"

    btns[10]['bg'] = clr
    btns[10]['text'] = "Колесина\nЮП"

    btns[42]['bg'] = clr
    btns[42]['text'] = "Детина\nЮП"

def saturday():
    for i in range(0,128):
        btns1[i].grid()
    for i in range(0,128):
        btns1[i]['text'] = ''
        btns1[i]['bg'] = 'SystemButtonFace'
    weekends()


    btns1[26]['bg'] = clr
    btns1[26]['text'] = "Юрис\nДизайн"

    btns1[34]['bg'] = clr
    btns1[34]['text'] = "Юрис\nДизайн"

    btns1[58]['bg'] = clr
    btns1[58]['text'] = "Юрис\nЦИ"

    btns1[66]['bg'] = clr
    btns1[66]['text'] = "Юрис\nЦИ"

    btns1[74]['bg'] = clr
    btns1[74]['text'] = "Юрис\nЦИ"

    btns1[74]['bg'] = clr
    btns1[74]['text'] = "Новик\nДизайн"

    btns1[82]['bg'] = clr
    btns1[82]['text'] = "Новик\nДизайн"

    btns1[90]['bg'] = clr
    btns1[90]['text'] = "Новик\nДизайн"

    btns1[98]['bg'] = clr
    btns1[98]['text'] = "Новик\nДизайн"

    btns1[106]['bg'] = clr
    btns1[106]['text'] = "Новик\nДизайн"

    btns1[14]['bg'] = clr
    btns1[14]['text'] = "Черкасов\nWeDo"

    btns1[22]['bg'] = clr
    btns1[22]['text'] = "Черкасов\nWeDo"

    btns1[30]['bg'] = clr
    btns1[30]['text'] = "Черкасов\nWeDo"

    btns1[38]['bg'] = clr
    btns1[38]['text'] = "Черкасов\nWeDo"

    btns1[46]['bg'] = clr
    btns1[46]['text'] = "Черкасов\nWeDo"

    btns1[54]['bg'] = clr
    btns1[54]['text'] = "Черкасов\nEV3"

    btns1[62]['bg'] = clr
    btns1[62]['text'] = "Черкасов\nEV3"

    btns1[70]['bg'] = clr
    btns1[70]['text'] = "Черкасов\nEV3"

    btns1[78]['bg'] = clr
    btns1[78]['text'] = "Черкасов\nEV3"

    btns1[86]['bg'] = clr
    btns1[86]['text'] = "Черкасов\nEV3"

    btns1[94]['bg'] = clr
    btns1[94]['text'] = "Черкасов\nEV3"

    btns1[51]['bg'] = clr
    btns1[51]['text'] = "Лёвкина\nCAD"

    btns1[59]['bg'] = clr
    btns1[59]['text'] = "Лёвкина\nCAD"

    btns1[67]['bg'] = clr
    btns1[67]['text'] = "Лёвкина\nCAD"

    btns1[37]['bg'] = clr
    btns1[37]['text'] = "Лёвкина\nGameDev"

    btns1[45]['bg'] = clr
    btns1[45]['text'] = "Лёвкина\nGameDev"

    btns1[81]['bg'] = clr
    btns1[81]['text'] = "Михадюк\nUX/UI"

    btns1[89]['bg'] = clr
    btns1[89]['text'] = "Михадюк\nUX/UI"

    btns1[97]['bg'] = clr
    btns1[97]['text'] = "Михадюк\nUX/UI"

    btns1[36]['bg'] = clr
    btns1[36]['text'] = "Мартынова\nРадиокон."

    btns1[44]['bg'] = clr
    btns1[44]['text'] = "Мартынова\nРадиокон."

    btns1[52]['bg'] = clr
    btns1[52]['text'] = "Мартынова\nРадиокон."

    btns1[108]['bg'] = clr
    btns1[108]['text'] = "Мартынова\nРадиокон."

    btns1[116]['bg'] = clr
    btns1[116]['text'] = "Мартынова\nРадиокон."

    btns1[124]['bg'] = clr
    btns1[124]['text'] = "Мартынова\nРадиокон."

    btns1[23]['bg'] = clr
    btns1[23]['text'] = "Дроздов\nКулибин град"

    btns1[31]['bg'] = clr
    btns1[31]['text'] = "Дроздов\nКулибин град"

    btns1[39]['bg'] = clr
    btns[39]['text'] = "Дроздов\nКулибин град"

    btns1[84]['bg'] = clr
    btns1[84]['text'] = "Дроздов\nЭлектроника"

    btns1[92]['bg'] = clr
    btns1[92]['text'] = "Дроздов\nЭлектроника"

    btns1[100]['bg'] = clr
    btns1[100]['text'] = "Дроздов\nЭлектроника"

    btns1[35]['bg'] = clr
    btns1[35]['text'] = "Ходоскин\nЮФ"

    btns1[43]['bg'] = clr
    btns1[43]['text'] = "Ходоскин\nЮФ"

    btns1[51]['bg'] = 'red'
    btns1[51]['text'] += "/Ходоскин\nЮФ"

    btns1[75]['bg'] = clr
    btns1[75]['text'] = "Ходоскин\nЮФ"

    btns1[83]['bg'] = clr
    btns1[83]['text'] = "Ходоскин\nЮФ"

    btns1[59]['bg'] = 'red'
    btns1[59]['text'] += "/Ходоскин\nЮФ"

    btns1[67]['bg'] = 'red'
    btns1[67]['text'] += "/Ходоскин\nЮФ"

    btns1[47]['bg'] = clr
    btns1[47]['text'] = "Горленко\nангл."

    btns1[55]['bg'] = clr
    btns1[55]['text'] = "Горленко\nангл."

    btns1[63]['bg'] = clr
    btns1[63]['text'] = "Горленко\nангл."

    btns1[39]['bg'] = 'SystemButtonFace'

def sunday():
    for i in range(0,128):
        btns1[i]['text'] = ''
        btns1[i]['bg'] = 'SystemButtonFace'
    weekends()

    btns1[49]['bg'] = clr
    btns1[49]['text'] = "Андреев\nScratch"

    btns1[57]['bg'] = clr
    btns1[57]['text'] = "Андреев\nScratch"

    btns1[81]['bg'] = clr
    btns1[81]['text'] = "Андреев\nScratch"

    btns1[89]['bg'] = clr
    btns1[89]['text'] = "Андреев\nScratch"

    btns1[21]['bg'] = clr
    btns1[21]['text'] = "Андреев\nScratch"

    btns1[29]['bg'] = clr
    btns1[29]['text'] = "Андреев\nScratch"

    btns1[37]['bg'] = clr
    btns1[37]['text'] = "Андреев\nScratch"

    btns1[45]['bg'] = clr
    btns1[45]['text'] = "Андреев\nScratch"

    btns1[68]['bg'] = clr
    btns1[68]['text'] = "Андреев\nScratch"

    btns1[76]['bg'] = clr
    btns1[76]['text'] = "Андреев\nScratch"

    btns1[30]['bg'] = clr
    btns1[30]['text'] = "Черкасов\nWeDo"

    btns1[22]['bg'] = clr
    btns1[22]['text'] = "Черкасов\nWeDo"

    btns1[102]['bg'] = clr
    btns1[102]['text'] = "Черкасов\nWeDo"

    btns1[110]['bg'] = clr
    btns1[110]['text'] = "Черкасов\nWeDo"

    btns1[30]['bg'] = clr
    btns1[30]['text'] = "Черкасов\nEV3"

    btns1[38]['bg'] = clr
    btns1[38]['text'] = "Черкасов\nEV3"

    btns1[46]['bg'] = clr
    btns1[46]['text'] = "Черкасов\nEV3"

    btns1[54]['bg'] = clr
    btns1[54]['text'] = "Черкасов\nEV3"

    btns1[62]['bg'] = clr
    btns1[62]['text'] = "Черкасов\nEV3"

    btns1[70]['bg'] = clr
    btns1[70]['text'] = "Черкасов\nEV3"

    btns1[78]['bg'] = clr
    btns1[78]['text'] = "Черкасов\nEV3"

    btns1[86]['bg'] = clr
    btns1[86]['text'] = "Черкасов\nEV3"

    btns1[94]['bg'] = clr
    btns1[94]['text'] = "Черкасов\nEV3"

    btns1[82]['bg'] = clr
    btns1[82]['text'] = "Батаев\nC++"

    btns1[90]['bg'] = clr
    btns1[90]['text'] = "Батаев\nC++/C#"

    btns1[98]['bg'] = clr
    btns1[98]['text'] = "Батаев\nC#"

    btns1[17]['bg'] = clr
    btns1[17]['text'] = "Батаев\nConstract"

    btns1[25]['bg'] = clr
    btns1[25]['text'] = "Батаев\nConstract"

    btns1[36]['bg'] = clr
    btns1[36]['text'] = "Батаев\nConstract"

    btns1[44]['bg'] = clr
    btns1[44]['text'] = "Батаев\nConstract"

    btns1[52]['bg'] = clr
    btns1[52]['text'] = "Батаев\nConstract"

    btns1[60]['bg'] = clr
    btns1[60]['text'] = "Батаев\nConstract"

    btns1[69]['bg'] = clr
    btns1[69]['text'] = "Зайцев\nМоделирование"

    btns1[77]['bg'] = clr
    btns1[77]['text'] = "Зайцев\nМоделирование"

    btns1[85]['bg'] = clr
    btns1[85]['text'] = "Зайцев\nМоделирование"

    btns1[93]['bg'] = clr
    btns1[93]['text'] = "Зайцев\nМоделирование"

    btns1[101]['bg'] = clr
    btns1[101]['text'] = "Зайцев\nМоделирование"

    btns1[109]['bg'] = clr
    btns1[109]['text'] = "Зайцев\nМоделирование"

    btns1[53]['bg'] = clr
    btns1[53]['text'] = "Лёвкина\nGameDev"

    btns1[61]['bg'] = clr
    btns1[61]['text'] = "Лёвкина\nGameDev"

    btns1[39]['bg'] = clr
    btns1[39]['text'] = "Колесина\nТочка роста"

    btns1[47]['bg'] = clr
    btns1[47]['text'] = "Колесина\nТочка роста"

    btns1[58]['bg'] = clr
    btns1[58]['text'] = "Детина\nPascal"

    btns1[66]['bg'] = clr
    btns1[66]['text'] = "Детина\nPascal"

    btns1[74]['bg'] = clr
    btns1[74]['text'] = "Детина\nPascal"

    btns1[26]['bg'] = clr
    btns1[26]['text'] = "Детина\nКГ"

    btns1[34]['bg'] = clr
    btns1[34]['text'] = "Детина\nКГ"

    btns1[42]['bg'] = clr
    btns1[42]['text'] = "Детина\nКГ"

    btns1[50]['bg'] = clr
    btns1[50]['text'] = "Детина\nКГ"

    btns1[58]['bg'] = clr
    btns1[58]['text'] = "Детина\nКГ"

def clear():
    for i in range(0,128):
        btns1[i].grid_remove()
    lbl2.place(x = 2100,y = 2100)
    for i in range(0,56):
        btns[i]['text'] = ''
        btns[i]['bg'] = 'SystemButtonFace'
    ramki()

def weekends():
    lbl2.place(x=650, y=300)
    for i in range(0,128):
        btns1.append(Button(win, text = '', width = 10, height = 2))
        btns1[i].bind("<Button-1>", weekends_info)

    for i in range(0,16):
        for g in range(0,8):
            btns1[i*8+g].grid(row = i, column = g)
    btns1[0]['text'] = ''
    btns1[1]['text'] = '1-2'
    btns1[2]['text'] = '1-3'
    btns1[3]['text'] = '1-4'
    btns1[4]['text'] = '1-6'
    btns1[5]['text'] = '1-7'
    btns1[6]['text'] = '1-8'
    btns1[7]['text'] = '1-9'

    btns1[8]['text'] = '8:30-9:15'
    btns1[16]['text'] = '9:20-9:45'
    btns1[24]['text'] = '9:50-11:05'
    btns1[32]['text'] = '11:10-11:45'
    btns1[40]['text'] = '11:50-12:35'
    btns1[48]['text'] = '12:40-13:25'
    btns1[56]['text'] = '13:30-14:15'
    btns1[64]['text'] = '14:20-15:05'
    btns1[72]['text'] = '15:10-15:55'
    btns1[80]['text'] = '16:00-16:45'
    btns1[88]['text'] = '16:50-17:55'
    btns1[96]['text'] = '17:40-18:25'
    btns1[104]['text'] = '18:30-19:15'
    btns1[112]['text'] = '19:20-20:05'
    btns1[120]['text'] = '20:10-20:55'
def info(event):
    time = 0
    if btns.index(event.widget)<=15:
        time =btns[8]['text']
    elif btns.index(event.widget)<=23:
        time =btns[16]['text']
    elif btns.index(event.widget)<=31:
        time =btns[24]['text']
    elif btns.index(event.widget)<=39:
        time =btns[32]['text']
    elif btns.index(event.widget)<=47:
        time =btns[40]['text']
    elif btns.index(event.widget)<=55:
        time =btns[48]['text']

    num = btns.index(event.widget) % 8

    if btns[btns.index(event.widget)]['text'] == '':
        lbl1["text"] = ''
    elif btns[btns.index(event.widget)]['text'] == btns[num]['text'] or btns[btns.index(event.widget)]['text'] == time:
        lbl1["text"] = ''
    else:
        lbl1["text"] = str(time) + '\n' + str(event.widget['text']) + '\n' + str(btns[num]['text'])
def weekends_info(event):
    time = 0
    if btns1.index(event.widget)<=15:
        time =btns1[8]['text']
    elif btns1.index(event.widget)<=23:
        time =btns1[16]['text']
    elif btns1.index(event.widget)<=31:
        time =btns1[24]['text']
    elif btns1.index(event.widget)<=39:
        time =btns1[32]['text']
    elif btns1.index(event.widget)<=47:
        time = btns1[40]['text']
    elif btns1.index(event.widget)<=55:
        time =btns1[48]['text']
    elif btns1.index(event.widget)<=23:
        time =btns1[56]['text']
    elif btns1.index(event.widget)<=71:
        time =btns1[64]['text']
    elif btns1.index(event.widget)<=79:
        time =btns1[72]['text']
    elif btns1.index(event.widget)<=87:
        time =btns1[80]['text']
    elif btns1.index(event.widget)<=95:
        time =btns1[88]['text']
    elif btns1.index(event.widget)<=103:
        time =btns1[96]['text']
    elif btns1.index(event.widget)<=111:
        time =btns1[104]['text']
    elif btns1.index(event.widget)<=119:
        time =btns1[112]['text']
    elif btns1.index(event.widget)<=127:
        time =btns1[120]['text']

    num = btns1.index(event.widget) % 8

    if btns1[btns1.index(event.widget)]['text'] == '':
        lbl2["text"] = ''
    elif btns1[btns1.index(event.widget)]['text'] == btns1[num]['text'] or btns1[btns1.index(event.widget)]['text'] == time:
        lbl2["text"] = ''
    else:
        lbl2["text"] = str(time) + '\n' + str(event.widget['text']) + '\n' + str(btns1[num]['text'])

btns = []
btns1 = []

for i in range(0,56):
    btns.append(Button(win, text ='', width = 10, height = 2))
    btns[i].bind("<Button-1>",info)

for i in range(0,7):
    for g in range(0,8):
        btns[i*8+g].grid(row = i, column = g)

d = IntVar()
rd1 = Radiobutton(win, text = 'понедельник',value = 1,variable = d, command = monday , height = 2).place(x = 650, y = 0)
rd2 = Radiobutton(win, text = 'вторник',value = 2,variable = d, command = tuesday , height = 2).place(x = 650, y = 30)
rd3 = Radiobutton(win, text = 'среда',value = 3,variable = d, command = wednesday , height = 2).place(x = 650, y = 60)
rd4 = Radiobutton(win, text = 'четверг',value = 4,variable = d, command = thursday , height = 2).place(x = 650, y = 90)
rd5 = Radiobutton(win, text = 'пятница',value = 5,variable = d, command = friday , height = 2).place(x = 650, y = 120)
rd6 = Radiobutton(win, text = 'субота',value = 6,variable = d, command = saturday , height = 2).place(x = 650, y = 150)
rd7 = Radiobutton(win, text = 'воскресенье',value = 7,variable = d, command = sunday , height = 2).place(x = 650, y = 180)

btn_teachers = Button(win, text = 'педагоги', width = 10, height = 2, command = teachers.plan).place(x = 650, y = 210)

lbl1 = Label(win, text = '', width = 30, height = 5, relief = 'raised',anchor = 'nw')
lbl1.place(x=0, y=300)
lbl2 = Label(win, text = '', width = 20, height = 10, relief = 'raised',anchor = 'nw')
lbl2.place(x=650, y=300)

weekends()
clear()
ramki()
win.mainloop()