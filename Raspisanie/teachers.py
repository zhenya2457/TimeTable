from tkinter import *
from tkinter import ttk
btns_t = []
btns1_t = []

def ramki():
    btns_t[0]['text'] = ''
    btns_t[1]['text'] = 'ПН'
    btns_t[2]['text'] = 'ВТ'
    btns_t[3]['text'] = 'СР'
    btns_t[4]['text'] = 'ЧТ'
    btns_t[5]['text'] = 'ПТ'
    btns_t[6]['text'] = 'СБ'
    btns_t[7]['text'] = 'ВС'

    btns_t[8]['text'] = '10:00-11:40'
    btns_t[16]['text'] = '11:50-13:30'
    btns_t[24]['text'] = '13:40-15:20'
    btns_t[32]['text'] = '15:30-17:10'
    btns_t[40]['text'] = '17:00-18:35'
    btns_t[48]['text'] = '18:40-20:15'


t = True
def plan():
    win_t = Tk()
    win_t.title("педагоги")
    win_t.geometry("800x700")
    clr = 'grey'
    global t
    global btns_t
    global btns1_t
    def clear():
        for i in range(0, 128):
            btns1_t[i].grid_remove()
        for i in range(0, 56):
            btns_t[i]['text'] = ''
            btns_t[i]['bg'] = 'SystemButtonFace'

    def qqq():
        for i in range(0, 128):
            btns1_t.append(Button(win_t, text='', width=11, height=2))
        for i in range(0, 16):
            for g in range(0, 8):
                btns1_t[i * 8 + g].grid(row=i, column=g)
        btns1_t[0]['text'] = ''
        btns1_t[1]['text'] = 'ПН'
        btns1_t[2]['text'] = 'ВТ'
        btns1_t[3]['text'] = 'СР'
        btns1_t[4]['text'] = 'ЧТ'
        btns1_t[5]['text'] = 'ПТ'
        btns1_t[6]['text'] = 'СБ'
        btns1_t[7]['text'] = 'ВС'

        btns1_t[8]['text'] = '8:30-9:45'
        btns1_t[16]['text'] = '9:30-10:45'
        btns1_t[24]['text'] = '9:50-11:05'
        btns1_t[32]['text'] = '10:00-11:40'
        btns1_t[40]['text'] = '10:50-12:25'
        btns1_t[48]['text'] = '11:10-12:25'
        btns1_t[56]['text'] = '12:30-14:05'
        btns1_t[64]['text'] = '13:00-14:35'
        btns1_t[72]['text'] = '14:25-16:00'
        btns1_t[80]['text'] = '14:40-16:15'
        btns1_t[88]['text'] = '16:20-17:55'
        btns1_t[96]['text'] = '16:10-17:45'
        btns1_t[104]['text'] = '17:00-18:35'
        btns1_t[112]['text'] = '17:50-19:05'
        btns1_t[120]['text'] = '18:40-20:15'




    def oparina():
        clear()
        ramki()
        btns_t[17]['bg'] = clr
        btns_t[17]['text'] = '1-4\nАндроид'
        btns_t[10]['bg'] = clr
        btns_t[10]['text'] = '1-8\nApp Inventor'
        btns_t[18]['bg'] = clr
        btns_t[18]['text'] = '1-8\nApp Inventor'
        btns_t[11]['bg'] = clr
        btns_t[11]['text'] = '1-7\nApp Inventor'
        btns_t[19]['bg'] = clr
        btns_t[19]['text'] = '1-8\nApp Inventor'
        btns_t[18]['bg'] = clr
        btns_t[18]['text'] = '1-8\nАндроид'
        btns_t[9]['bg'] = clr
        btns_t[9]['text'] = '1-8\nОАП'
        btns_t[20]['bg'] = clr
        btns_t[20]['text'] = '1-8\nОАП'

    def andreev():
        clear()
        ramki()
        btns_t[8]['text'] = '9:20-10:55'
        btns_t[16]['text'] = '11:00-12:35'
        btns_t[24]['text'] = '12:40-14:15'
        btns_t[32]['text'] = '14:20-15:55'
        btns_t[40]['text'] = '16:20-17:55'
        btns_t[15]['bg'] = clr
        btns_t[15]['text'] = '1-7\nScratch'
        btns_t[23]['bg'] = clr
        btns_t[23]['text'] = '1-7\nScratch'
        btns_t[31]['bg'] = clr
        btns_t[31]['text'] = '1-2\nScratch'
        btns_t[39]['bg'] = clr
        btns_t[39]['text'] = '1-6\nScratch'
        btns_t[47]['bg'] = clr
        btns_t[47]['text'] = '1-2\nScratch'

    def uris():
        clear()
        ramki()

        btns_t[8]['text'] = '10:10-11:45'
        btns_t[24]['text'] = '12:05-13:40'
        btns_t[32]['text'] = '13:40-15:20'
        btns_t[40]['text'] = '14:00-15:35'
        btns_t[19]['bg'] = clr
        btns_t[19]['text'] = '1-3\nДизайн'
        btns_t[20]['bg'] = clr
        btns_t[20]['text'] = '1-3\nДизайн'
        btns_t[14]['bg'] = clr
        btns_t[14]['text'] = '1-3\nДизайн'
        btns_t[31]['bg'] = clr
        btns_t[31]['text'] = '1-3\nДизайн'
        btns_t[36]['bg'] = clr
        btns_t[36]['text'] = '1-3\nЮИ'
        btns_t[46]['bg'] = clr
        btns_t[46]['text'] = '1-3\nЦИ'

    def novik():
        clear()
        ramki()
        btns_t[32]['text'] = '15:40-16:25'
        btns_t[40]['text'] = '17:20-18:55'
        btns_t[38]['bg'] = clr
        btns_t[38]['text'] = '1-3\nДизайн'
        btns_t[46]['bg'] = clr
        btns_t[46]['text'] = '1-3\nДизайн'

    def makeenko():
        clear()
        ramki()
        btns_t[9]['bg'] = clr
        btns_t[9]['text'] = '1-7\nWebDev'
        btns_t[12]['bg'] = clr
        btns_t[12]['text'] = '1-7\nWebDev'
        btns_t[13]['bg'] = clr
        btns_t[13]['text'] = '1-7\nWebDev'
        btns_t[21]['bg'] = clr
        btns_t[21]['text'] = '1-4\nWebDev'
        btns_t[29]['bg'] = clr
        btns_t[29]['text'] = '1-4\nWebDev'
        btns_t[28]['bg'] = clr
        btns_t[28]['text'] = '1-4\nWebDev'
        btns_t[36]['bg'] = clr
        btns_t[36]['text'] = '1-4\nWebDev'
        btns_t[17]['bg'] = clr
        btns_t[17]['text'] = '1-7\nGameDev'
        btns_t[26]['bg'] = clr
        btns_t[26]['text'] = '1-4\nGameDev'
        btns_t[34]['bg'] = clr
        btns_t[34]['text'] = '1-4\nGameDev'

    def cherkasov():
        for i in range(0, 128):
            btns1_t[i].grid()
        for i in range(0, 128):
            btns1_t[i]['text'] = i
            btns1_t[i]['bg'] = 'SystemButtonFace'
        qqq()

        btns1_t[14]['bg'] = clr
        btns1_t[14]['text'] = '1-8\nWeDo'
        btns1_t[30]['bg'] = clr
        btns1_t[30]['text'] = '1-8\nWeDo'
        btns1_t[54]['bg'] = clr
        btns1_t[54]['text'] = '1-8\nWeDo'
        btns1_t[23]['bg'] = clr
        btns1_t[23]['text'] = '1-8\nWeDo'
        btns1_t[119]['bg'] = clr
        btns1_t[119]['text'] = '1-8\nWeDo'
        btns1_t[70]['bg'] = clr
        btns1_t[70]['text'] = '1-8\nEV3'
        btns1_t[86]['bg'] = clr
        btns1_t[86]['text'] = '1-8\nEV3'
        btns1_t[94]['bg'] = clr
        btns1_t[94]['text'] = '1-8\nEV3'
        btns1_t[63]['bg'] = clr
        btns1_t[63]['text'] = '1-8\nEV3'
        btns1_t[79]['bg'] = clr
        btns1_t[79]['text'] = '1-8\nEV3'
        btns1_t[103]['bg'] = clr
        btns1_t[103]['text'] = '1-8\nEV3'
        btns1_t[47]['bg'] = clr
        btns1_t[47]['text'] = '1-8\nEV3'
        btns1_t[106]['bg'] = clr
        btns1_t[106]['text'] = '1-7\nScratch'
        btns1_t[36]['bg'] = clr
        btns1_t[36]['text'] = '1-8\nEV3'
        btns1_t[122]['bg'] = clr
        btns1_t[122]['text'] = '1-9\nWeDo'

    def bataev():
        for i in range(0, 128):
            btns1_t[i].grid()
        for i in range(0, 128):
            btns1_t[i]['text'] = i
            btns1_t[i]['bg'] = 'SystemButtonFace'
        qqq()
        btns1_t[8]['text'] = '9:20-10:55'
        btns1_t[16]['text'] = '10:00-11:40'
        btns1_t[24]['text'] = '11:00-12:35'
        btns1_t[32]['text'] = '11:50-13:30'
        btns1_t[40]['text'] = '12:40-14:15'
        btns1_t[48]['text'] = '13:40-15:20'
        btns1_t[56]['text'] = '15:30-17:10'
        btns1_t[64]['text'] = '15:40-17:15'
        btns1_t[72]['text'] = '17:20-18:55'
        btns1_t[80]['text'] = ''
        btns1_t[88]['text'] = ''
        btns1_t[96]['text'] = ''
        btns1_t[104]['text'] = ''
        btns1_t[112]['text'] = ''
        btns1_t[120]['text'] = ''
        for i in range(80, 128):
            btns1_t[i].grid_remove()

        btns1_t[49]['bg'] = clr
        btns1_t[49]['text'] = '1-4\nJava'
        btns1_t[51]['bg'] = clr
        btns1_t[51]['text'] = '1-4\nJava'
        btns1_t[59]['bg'] = clr
        btns1_t[59]['text'] = '1-6\nC++'
        btns1_t[71]['bg'] = clr
        btns1_t[71]['text'] = '1-3\nC++'
        btns1_t[58]['bg'] = clr
        btns1_t[58]['text'] = '1-7\nC#'
        btns1_t[79]['bg'] = clr
        btns1_t[79]['text'] = '1-3\nC#'
        btns1_t[33]['bg'] = clr
        btns1_t[33]['text'] = '1-8\nPython'
        btns1_t[19]['bg'] = clr
        btns1_t[19]['text'] = '1-8\nPython'
        btns1_t[52]['bg'] = clr
        btns1_t[52]['text'] = '1-8\nPython'
        btns1_t[37]['bg'] = clr
        btns1_t[37]['text'] = '1-8\nPython'
        btns1_t[45]['bg'] = clr
        btns1_t[45]['text'] = '1-8\nPython'
        btns1_t[15]['bg'] = clr
        btns1_t[15]['text'] = '1-2\nConstract'
        btns1_t[31]['bg'] = clr
        btns1_t[31]['text'] = '1-6\nConstract'
        btns1_t[47]['bg'] = clr
        btns1_t[47]['text'] = '1-6\nConstract'

    def zaitcev():
        clear()
        ramki()
        btns_t[24]['text'] = '14:10-16:35'
        btns_t[40]['text'] = '16:45-19:10'
        btns_t[31]['bg'] = clr
        btns_t[31]['text'] = '1-7\nМоделирование'
        btns_t[47]['bg'] = clr
        btns_t[47]['text'] = '1-7\nМоделирование'

    def levkina():
        clear()
        ramki()
        btns_t[8]['text'] = '11:00-12:35'
        btns_t[24]['text'] = '12:40-14:15'
        btns_t[32]['text'] = '12:55-14:30'

        btns_t[21]['bg'] = clr
        btns_t[21]['text'] = '1-7\nGameDev'
        btns_t[38]['bg'] = clr
        btns_t[38]['text'] = '1-4\nCAD'
        btns_t[15]['bg'] = clr
        btns_t[15]['text'] = '1-7\nGameDev'
        btns_t[31]['bg'] = clr
        btns_t[31]['text'] = '1-7\nGameDev'

    def mihaduk():
        clear()
        ramki()
        btns_t[40]['text'] = '16:50-18:25'

        btns_t[46]['bg'] = clr
        btns_t[46]['text'] = '1-2\nUX/UI'
        btns_t[36]['bg'] = clr
        btns_t[36]['text'] = '1-3\nJava'
        btns_t[37]['bg'] = clr
        btns_t[37]['text'] = '1-3\nJava'
        btns_t[18]['bg'] = clr
        btns_t[18]['text'] = '1-3\nНейросети'

    def martinova():
        clear()
        ramki()

        btns_t[16]['text'] = '11:00-13:25'
        btns_t[40]['text'] = '17:00-19:25'
        btns_t[48]['text'] = '18:30-20:55'

        btns_t[44]['bg'] = clr
        btns_t[44]['text'] = '1-6\nРадиокон.'
        btns_t[22]['bg'] = clr
        btns_t[22]['text'] = '1-6\nРадиокон.'
        btns_t[54]['bg'] = clr
        btns_t[54]['text'] = '1-6\nРадиокон.'

    def drozdov():
        clear()
        ramki()

        btns_t[8]['text'] = '9:00-10:15'
        btns_t[16]['text'] = '10:20-11:35'
        btns_t[32]['text'] = '15:30-18:05'
        btns_t[40]['text'] = '16:00-18:25'

        btns_t[15]['bg'] = clr
        btns_t[15]['text'] = '1-9\nКулибин'
        btns_t[23]['bg'] = clr
        btns_t[23]['text'] = '1-9\nКулибин'
        btns_t[47]['bg'] = clr
        btns_t[47]['text'] = '1-6\nЭлектроника'
        btns_t[38]['bg'] = clr
        btns_t[38]['text'] = '1-6\nЭлектроника'

    def nikitin():
        clear()
        ramki()

        btns_t[40]['text'] = '17:15-18:55'

        btns_t[25]['bg'] = clr
        btns_t[25]['text'] = '1-2\nМем стори'
        btns_t[27]['bg'] = clr
        btns_t[27]['text'] = '1-7\nМем стори'
        btns_t[9]['bg'] = clr
        btns_t[9]['text'] = '1-2\nArduino'
        btns_t[11]['bg'] = clr
        btns_t[11]['text'] = '1-2\nArduino'
        btns_t[17]['bg'] = clr
        btns_t[17]['text'] = '1-2\nArduino'
        btns_t[19]['bg'] = clr
        btns_t[19]['text'] = '1-6\nArduino'
        btns_t[33]['bg'] = clr
        btns_t[33]['text'] = '1-6\nArduino'
        btns_t[35]['bg'] = clr
        btns_t[35]['text'] = '1-2\nЭлектроград'
        btns_t[43]['bg'] = clr
        btns_t[43]['text'] = '1-2\nЭлектроград'

    def sushevich():
        clear()
        ramki()

        btns_t[24]['text'] = '13:25-15:00'

        btns_t[9]['bg'] = clr
        btns_t[9]['text'] = '1-3\nPixel'
        btns_t[10]['bg'] = clr
        btns_t[10]['text'] = '1-2\nPixel'
        btns_t[11]['bg'] = clr
        btns_t[11]['text'] = '1-3\nPixel'
        btns_t[12]['bg'] = clr
        btns_t[12]['text'] = '1-2\nPixel'
        btns_t[17]['bg'] = clr
        btns_t[17]['text'] = '1-3\nPixel'
        btns_t[18]['bg'] = clr
        btns_t[18]['text'] = '1-2\nPixel'
        btns_t[19]['bg'] = clr
        btns_t[19]['text'] = '1-2\nPixel'
        btns_t[25]['bg'] = clr
        btns_t[25]['text'] = '1-3\nPixel'
        btns_t[26]['bg'] = clr
        btns_t[26]['text'] = '1-2\nPixel'
        btns_t[27]['bg'] = clr
        btns_t[27]['text'] = '1-3\nPixel'
        btns_t[14]['bg'] = clr
        btns_t[14]['text'] = 'Конференс-зал\nEV3'
        btns_t[33]['bg'] = clr
        btns_t[33]['text'] = '1-6\nСис.ад.'

    def xodoskin():
        clear()
        ramki()

        btns_t[8]['text'] = '11:40-13:15'
        btns_t[16]['text'] = '13:20-14:55'
        btns_t[24]['text'] = '15:00-16:35'
        btns_t[32]['text'] = '15:20-16:55'
        btns_t[40]['text'] = '17:00-18:40'

        btns_t[35]['bg'] = clr
        btns_t[35]['text'] = '1-9\nЮФ'
        btns_t[43]['bg'] = clr
        btns_t[43]['text'] = '1-9\nЮФ'
        btns_t[44]['bg'] = clr
        btns_t[44]['text'] = '1-9\nЮФ'
        btns_t[14]['bg'] = clr
        btns_t[14]['text'] = '1-4\nЮФ'
        btns_t[22]['bg'] = clr
        btns_t[22]['text'] = '1-4\nЮФ'
        btns_t[30]['bg'] = clr
        btns_t[30]['text'] = '1-4\nЮФ'

    def kolesina():
        clear()
        ramki()

        btns_t[16]['text'] = '11:00-12:15'
        btns_t[24]['text'] = '11:50-13:30'
        btns_t[32]['text'] = '13:40-15:20'
        btns_t[40]['text'] = '15:30-17:10'
        btns_t[48]['text'] = '18:40-20:15'

        btns_t[29]['bg'] = clr
        btns_t[29]['text'] = '1-9\nМатем.'
        btns_t[37]['bg'] = clr
        btns_t[37]['text'] = '1-9\nМатем.'
        btns_t[45]['bg'] = clr
        btns_t[45]['text'] = '1-9\nМатем.'
        btns_t[23]['bg'] = clr
        btns_t[23]['text'] = '1-9\nТочка роста'
        btns_t[10]['bg'] = clr
        btns_t[10]['text'] = '1-3\nЮП'
        btns_t[13]['bg'] = clr
        btns_t[13]['text'] = '1-3\nЮП'

    def gorlenko():
        clear()
        ramki()

        btns_t[16]['text'] = '11:40-12:55'
        btns_t[24]['text'] = '13:00-14:35'

        btns_t[22]['bg'] = clr
        btns_t[22]['text'] = '1-9\nАнгл.яз.'
        btns_t[30]['bg'] = clr
        btns_t[30]['text'] = '1-9\nАнгл.яз.'

    def detina():
        clear()
        ramki()

        btns_t[16]['text'] = '10:50-12:05'
        btns_t[24]['text'] = '12:10-13:45'
        btns_t[32]['text'] = '14:00-15:35'

        btns_t[42]['bg'] = clr
        btns_t[42]['text'] = '1-3\nЮП'
        btns_t[45]['bg'] = clr
        btns_t[45]['text'] = '1-3\nЮП'
        btns_t[39]['bg'] = clr
        btns_t[39]['text'] = '1-3\nPascal'
        btns_t[12]['bg'] = clr
        btns_t[12]['text'] = '1-3\nPascal'
        btns_t[23]['bg'] = clr
        btns_t[23]['text'] = '1-3\nКГ'
        btns_t[31]['bg'] = clr
        btns_t[31]['text'] = '1-3\nКГ'

    def chernekova():
        clear()
        ramki()

        btns_t[8]['text'] = '10:30-11:50'

        btns_t[31]['bg'] = clr
        btns_t[31]['text'] = '1-9\nМоделирование'

    if t == True:
        for i in range(0, 56):
            btns_t.append(Button(win_t, text='', width=11, height=2))

        for i in range(0, 7):
            for g in range(0, 8):
                btns_t[i * 8 + g].grid(row=i, column=g)
        qqq()
        clear()
        ramki()

        def selected(event):
            selection = combobox.get()

            if selection == _teachers[0]:
                oparina()
            elif selection == _teachers[1]:
                andreev()
            elif selection == _teachers[2]:
                uris()
            elif selection == _teachers[3]:
                novik()
            elif selection == _teachers[4]:
                makeenko()
            elif selection == _teachers[5]:
                cherkasov()
            elif selection == _teachers[6]:
                bataev()
            elif selection == _teachers[7]:
                zaitcev()
            elif selection == _teachers[8]:
                levkina()
            elif selection == _teachers[9]:
                mihaduk()
            elif selection == _teachers[10]:
                martinova()
            elif selection == _teachers[11]:
                drozdov()
            elif selection == _teachers[12]:
                nikitin()
            elif selection == _teachers[13]:
                sushevich()
            elif selection == _teachers[14]:
                xodoskin()
            elif selection == _teachers[15]:
                kolesina()
            elif selection == _teachers[16]:
                gorlenko()
            elif selection == _teachers[17]:
                detina()
            elif selection == _teachers[18]:
                chernekova()

        d = IntVar()
        _teachers = ['Опарина', 'Андреев','Юрис','Новик','Макеенко','Черкасов','Батаев','Зайцев','Лёвкина','Михадюк','Мартынова','Дроздов','Никитин','Сущевич','Ходоскин','Колесина','Горленко','Детина','Чернекова',]
        combobox = ttk.Combobox(win_t, values = _teachers,state="readonly")
        combobox.place( x=650, y=300)
        combobox.bind("<<ComboboxSelected>>", selected)



        t = False

    elif t == False:
        btns_t = []
        btns1_t = []
        t == True
