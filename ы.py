import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import copy
from PyQt5 import QtGui

font = QtGui.QFont()
font.setUnderline(True)
font1 = QtGui.QFont()
font1.setUnderline(False)

def pr(p):
    for i in p:
        print(*i)
        
def trans_whole():
    global pole
    pole = list(map(list, zip(*pole)))
        
def change_row():
    global pole
    a = random.randint(0, 2)
    s = [0, 1, 2]
    random.shuffle(s)
    p1 = a*3 + s[0]
    p2 = a*3 + s[1]
    q = pole[p1]
    pole[p1] = pole[p2]
    pole[p2] = q
    
def change_col():
    global pole
    trans_whole()
    change_row()
    trans_whole()
    
def rows():
    global pole
    s = [0, 1, 2]
    random.shuffle(s)  
    p1 = [pole[s[0]*3], pole[s[0]*3 + 1], pole[s[0]*3 + 2]]
    p2 = [pole[s[1]*3], pole[s[1]*3 + 1], pole[s[1]*3 + 2]]
    pole[s[0]*3] = p2[0]
    pole[s[0]*3 + 1] = p2[1]
    pole[s[0]*3 + 2] = p2[2]
    pole[s[1]*3] = p1[0]
    pole[s[1]*3 + 1] = p1[1]
    pole[s[1]*3 + 2] = p1[2]    
    
def cols():
    global pole
    trans_whole()
    rows()
    trans_whole()    
    
        
def aa():
    global pole, S
    pole = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]]
    for i in range(30):
        operation = random.randint(0, 4)
        if operation == 0:
            trans_whole()
        if operation == 1:
            change_row()
        if operation == 2:
            change_col()
        if operation == 3:
            rows()
        if operation == 4 :
            cols()
    S = copy.deepcopy(pole)
    pr(S)
    print()

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled2.ui',self)
        self.game = False
        self.level = 0
        self.level3.clicked.connect(self.click3)
        self.level2.clicked.connect(self.click2)
        self.level1.clicked.connect(self.click1)
        self.zanovo.clicked.connect(self.restart)
        self.reshenie.clicked.connect(self.resheniie)
        self.check.clicked.connect(self.checker)
        
    def checker(self):
        global S
        if self.game:
            if (self.p1.toPlainText()==str(S[0][0]) and self.p41.toPlainText()==str(S[4][4]) and
                self.p2.toPlainText()==str(S[0][1]) and self.p42.toPlainText()==str(S[4][5]) and
                self.p3.toPlainText()==str(S[0][2]) and self.p43.toPlainText()==str(S[4][6]) and
                self.p4.toPlainText()==str(S[0][3]) and self.p44.toPlainText()==str(S[4][7]) and
                self.p5.toPlainText()==str(S[0][4]) and self.p45.toPlainText()==str(S[4][8]) and
                self.p6.toPlainText()==str(S[0][5]) and self.p46.toPlainText()==str(S[5][0]) and
                self.p7.toPlainText()==str(S[0][6]) and self.p47.toPlainText()==str(S[5][1]) and
                self.p8.toPlainText()==str(S[0][7]) and self.p48.toPlainText()==str(S[5][2]) and
                self.p9.toPlainText()==str(S[0][8]) and self.p49.toPlainText()==str(S[5][3]) and
                self.p10.toPlainText()==str(S[1][0]) and self.p50.toPlainText()==str(S[5][4]) and
                self.p11.toPlainText()==str(S[1][1]) and self.p51.toPlainText()==str(S[5][5]) and
                self.p12.toPlainText()==str(S[1][2]) and self.p52.toPlainText()==str(S[5][6]) and
                self.p13.toPlainText()==str(S[1][3]) and self.p53.toPlainText()==str(S[5][7]) and
                self.p14.toPlainText()==str(S[1][4]) and self.p54.toPlainText()==str(S[5][8]) and
                self.p15.toPlainText()==str(S[1][5]) and self.p55.toPlainText()==str(S[6][0]) and
                self.p16.toPlainText()==str(S[1][6]) and self.p56.toPlainText()==str(S[6][1]) and
                self.p17.toPlainText()==str(S[1][7]) and self.p57.toPlainText()==str(S[6][2]) and
                self.p18.toPlainText()==str(S[1][8]) and self.p58.toPlainText()==str(S[6][3]) and
                self.p19.toPlainText()==str(S[2][0]) and self.p59.toPlainText()==str(S[6][4]) and
                self.p20.toPlainText()==str(S[2][1]) and self.p60.toPlainText()==str(S[6][5]) and
                self.p21.toPlainText()==str(S[2][2]) and self.p61.toPlainText()==str(S[6][6]) and
                self.p22.toPlainText()==str(S[2][3]) and self.p62.toPlainText()==str(S[6][7]) and
                self.p23.toPlainText()==str(S[2][4]) and self.p63.toPlainText()==str(S[6][8]) and
                self.p24.toPlainText()==str(S[2][5]) and self.p64.toPlainText()==str(S[7][0]) and
                self.p25.toPlainText()==str(S[2][6]) and self.p65.toPlainText()==str(S[7][1]) and
                self.p26.toPlainText()==str(S[2][7]) and self.p66.toPlainText()==str(S[7][2]) and
                self.p27.toPlainText()==str(S[2][8]) and self.p67.toPlainText()==str(S[7][3]) and
                self.p28.toPlainText()==str(S[3][0]) and self.p68.toPlainText()==str(S[7][4]) and
                self.p29.toPlainText()==str(S[3][1]) and self.p69.toPlainText()==str(S[7][5]) and
                self.p30.toPlainText()==str(S[3][2]) and self.p70.toPlainText()==str(S[7][6]) and
                self.p31.toPlainText()==str(S[3][3]) and self.p71.toPlainText()==str(S[7][7]) and
                self.p32.toPlainText()==str(S[3][4]) and self.p72.toPlainText()==str(S[7][8]) and
                self.p33.toPlainText()==str(S[3][5]) and self.p73.toPlainText()==str(S[8][0]) and
                self.p34.toPlainText()==str(S[3][6]) and self.p74.toPlainText()==str(S[8][1]) and
                self.p35.toPlainText()==str(S[3][7]) and self.p75.toPlainText()==str(S[8][2]) and
                self.p36.toPlainText()==str(S[3][8]) and self.p76.toPlainText()==str(S[8][3]) and
                self.p37.toPlainText()==str(S[4][0]) and self.p77.toPlainText()==str(S[8][4]) and
                self.p38.toPlainText()==str(S[4][1]) and self.p78.toPlainText()==str(S[8][5]) and
                self.p39.toPlainText()==str(S[4][2]) and self.p79.toPlainText()==str(S[8][6]) and
                self.p40.toPlainText()==str(S[4][3]) and self.p80.toPlainText()==str(S[8][7]) and
                self.p81.toPlainText()==str(S[8][8])):
                self.lbl.setText('Молодец. Всё правильно')
            else:
                self.lbl.setText('Что-то не так')
        
    def resheniie(self):
        global S
        if self.game:
            self.lbl.setText('')
            self.p1.setPlainText(str(S[0][0])); self.p1.setReadOnly(True)
            self.p2.setPlainText(str(S[0][1])); self.p2.setReadOnly(True)
            self.p3.setPlainText(str(S[0][2])); self.p3.setReadOnly(True)
            self.p4.setPlainText(str(S[0][3])); self.p4.setReadOnly(True)
            self.p5.setPlainText(str(S[0][4])); self.p5.setReadOnly(True)
            self.p6.setPlainText(str(S[0][5])); self.p6.setReadOnly(True)
            self.p7.setPlainText(str(S[0][6])); self.p7.setReadOnly(True)
            self.p8.setPlainText(str(S[0][7])); self.p8.setReadOnly(True)
            self.p9.setPlainText(str(S[0][8])); self.p9.setReadOnly(True)
            self.p10.setPlainText(str(S[1][0])); self.p10.setReadOnly(True)
            self.p11.setPlainText(str(S[1][1])); self.p11.setReadOnly(True)
            self.p12.setPlainText(str(S[1][2])); self.p12.setReadOnly(True)
            self.p13.setPlainText(str(S[1][3])); self.p13.setReadOnly(True)
            self.p14.setPlainText(str(S[1][4])); self.p14.setReadOnly(True)
            self.p15.setPlainText(str(S[1][5])); self.p15.setReadOnly(True)
            self.p16.setPlainText(str(S[1][6])); self.p16.setReadOnly(True)
            self.p17.setPlainText(str(S[1][7])); self.p17.setReadOnly(True)
            self.p18.setPlainText(str(S[1][8])); self.p18.setReadOnly(True)
            self.p19.setPlainText(str(S[2][0])); self.p19.setReadOnly(True)
            self.p20.setPlainText(str(S[2][1])); self.p20.setReadOnly(True)
            self.p21.setPlainText(str(S[2][2])); self.p21.setReadOnly(True)
            self.p22.setPlainText(str(S[2][3])); self.p22.setReadOnly(True)
            self.p23.setPlainText(str(S[2][4])); self.p23.setReadOnly(True)
            self.p24.setPlainText(str(S[2][5])); self.p24.setReadOnly(True)
            self.p25.setPlainText(str(S[2][6])); self.p25.setReadOnly(True)
            self.p26.setPlainText(str(S[2][7])); self.p26.setReadOnly(True)
            self.p27.setPlainText(str(S[2][8])); self.p27.setReadOnly(True)
            self.p28.setPlainText(str(S[3][0])); self.p28.setReadOnly(True)
            self.p29.setPlainText(str(S[3][1])); self.p29.setReadOnly(True)
            self.p30.setPlainText(str(S[3][2])); self.p30.setReadOnly(True)
            self.p31.setPlainText(str(S[3][3])); self.p31.setReadOnly(True)
            self.p32.setPlainText(str(S[3][4])); self.p32.setReadOnly(True)
            self.p33.setPlainText(str(S[3][5])); self.p33.setReadOnly(True)
            self.p34.setPlainText(str(S[3][6])); self.p34.setReadOnly(True)
            self.p35.setPlainText(str(S[3][7])); self.p35.setReadOnly(True)
            self.p36.setPlainText(str(S[3][8])); self.p36.setReadOnly(True)
            self.p37.setPlainText(str(S[4][0])); self.p37.setReadOnly(True)
            self.p38.setPlainText(str(S[4][1])); self.p38.setReadOnly(True)
            self.p39.setPlainText(str(S[4][2])); self.p39.setReadOnly(True)
            self.p40.setPlainText(str(S[4][3])); self.p40.setReadOnly(True)
            self.p41.setPlainText(str(S[4][4])); self.p41.setReadOnly(True)
            self.p42.setPlainText(str(S[4][5])); self.p42.setReadOnly(True)
            self.p43.setPlainText(str(S[4][6])); self.p43.setReadOnly(True)
            self.p44.setPlainText(str(S[4][7])); self.p44.setReadOnly(True)
            self.p45.setPlainText(str(S[4][8])); self.p45.setReadOnly(True)
            self.p46.setPlainText(str(S[5][0])); self.p46.setReadOnly(True)
            self.p47.setPlainText(str(S[5][1])); self.p47.setReadOnly(True)
            self.p48.setPlainText(str(S[5][2])); self.p48.setReadOnly(True)
            self.p49.setPlainText(str(S[5][3])); self.p49.setReadOnly(True)
            self.p50.setPlainText(str(S[5][4])); self.p50.setReadOnly(True)
            self.p51.setPlainText(str(S[5][5])); self.p51.setReadOnly(True)
            self.p52.setPlainText(str(S[5][6])); self.p52.setReadOnly(True)
            self.p53.setPlainText(str(S[5][7])); self.p53.setReadOnly(True)
            self.p54.setPlainText(str(S[5][8])); self.p54.setReadOnly(True)
            self.p55.setPlainText(str(S[6][0])); self.p55.setReadOnly(True)
            self.p56.setPlainText(str(S[6][1])); self.p56.setReadOnly(True)
            self.p57.setPlainText(str(S[6][2])); self.p57.setReadOnly(True)
            self.p58.setPlainText(str(S[6][3])); self.p58.setReadOnly(True)
            self.p59.setPlainText(str(S[6][4])); self.p59.setReadOnly(True)
            self.p60.setPlainText(str(S[6][5])); self.p60.setReadOnly(True)
            self.p61.setPlainText(str(S[6][6])); self.p61.setReadOnly(True)
            self.p62.setPlainText(str(S[6][7])); self.p62.setReadOnly(True)
            self.p63.setPlainText(str(S[6][8])); self.p63.setReadOnly(True)
            self.p64.setPlainText(str(S[7][0])); self.p64.setReadOnly(True)
            self.p65.setPlainText(str(S[7][1])); self.p65.setReadOnly(True)
            self.p66.setPlainText(str(S[7][2])); self.p66.setReadOnly(True)
            self.p67.setPlainText(str(S[7][3])); self.p67.setReadOnly(True)
            self.p68.setPlainText(str(S[7][4])); self.p68.setReadOnly(True)
            self.p69.setPlainText(str(S[7][5])); self.p69.setReadOnly(True)
            self.p70.setPlainText(str(S[7][6])); self.p70.setReadOnly(True)
            self.p71.setPlainText(str(S[7][7])); self.p71.setReadOnly(True)
            self.p72.setPlainText(str(S[7][8])); self.p72.setReadOnly(True)
            self.p73.setPlainText(str(S[8][0])); self.p73.setReadOnly(True)
            self.p74.setPlainText(str(S[8][1])); self.p74.setReadOnly(True)
            self.p75.setPlainText(str(S[8][2])); self.p75.setReadOnly(True)
            self.p76.setPlainText(str(S[8][3])); self.p76.setReadOnly(True)
            self.p77.setPlainText(str(S[8][4])); self.p77.setReadOnly(True)
            self.p78.setPlainText(str(S[8][5])); self.p78.setReadOnly(True)
            self.p79.setPlainText(str(S[8][6])); self.p79.setReadOnly(True)
            self.p80.setPlainText(str(S[8][7])); self.p80.setReadOnly(True)
            self.p81.setPlainText(str(S[8][8])); self.p81.setReadOnly(True)
            self.game = False
        
    def restart(self):
        global S
        self.game = False
        self.level = 0
        self.lbl.setText('')
        self.p1.setPlainText(''); self.p1.setReadOnly(True)
        self.p2.setPlainText(''); self.p2.setReadOnly(True)
        self.p3.setPlainText(''); self.p3.setReadOnly(True)
        self.p4.setPlainText(''); self.p4.setReadOnly(True)
        self.p5.setPlainText(''); self.p5.setReadOnly(True)
        self.p6.setPlainText(''); self.p6.setReadOnly(True)
        self.p7.setPlainText(''); self.p7.setReadOnly(True)
        self.p8.setPlainText(''); self.p8.setReadOnly(True)
        self.p9.setPlainText(''); self.p9.setReadOnly(True)
        self.p10.setPlainText(''); self.p10.setReadOnly(True)
        self.p11.setPlainText(''); self.p11.setReadOnly(True)
        self.p12.setPlainText(''); self.p12.setReadOnly(True)
        self.p13.setPlainText(''); self.p13.setReadOnly(True)
        self.p14.setPlainText(''); self.p14.setReadOnly(True)
        self.p15.setPlainText(''); self.p15.setReadOnly(True)
        self.p16.setPlainText(''); self.p16.setReadOnly(True)
        self.p17.setPlainText(''); self.p17.setReadOnly(True)
        self.p18.setPlainText(''); self.p18.setReadOnly(True)
        self.p19.setPlainText(''); self.p19.setReadOnly(True)
        self.p20.setPlainText(''); self.p20.setReadOnly(True)
        self.p21.setPlainText(''); self.p21.setReadOnly(True)
        self.p22.setPlainText(''); self.p22.setReadOnly(True)
        self.p23.setPlainText(''); self.p23.setReadOnly(True)
        self.p24.setPlainText(''); self.p24.setReadOnly(True)
        self.p25.setPlainText(''); self.p25.setReadOnly(True)
        self.p26.setPlainText(''); self.p26.setReadOnly(True)
        self.p27.setPlainText(''); self.p27.setReadOnly(True)
        self.p28.setPlainText(''); self.p28.setReadOnly(True)
        self.p29.setPlainText(''); self.p29.setReadOnly(True)
        self.p30.setPlainText(''); self.p30.setReadOnly(True)
        self.p31.setPlainText(''); self.p31.setReadOnly(True)
        self.p32.setPlainText(''); self.p32.setReadOnly(True)
        self.p33.setPlainText(''); self.p33.setReadOnly(True)
        self.p34.setPlainText(''); self.p34.setReadOnly(True)
        self.p35.setPlainText(''); self.p35.setReadOnly(True)
        self.p36.setPlainText(''); self.p36.setReadOnly(True)
        self.p37.setPlainText(''); self.p37.setReadOnly(True)
        self.p38.setPlainText(''); self.p38.setReadOnly(True)
        self.p39.setPlainText(''); self.p39.setReadOnly(True)
        self.p40.setPlainText(''); self.p40.setReadOnly(True)
        self.p41.setPlainText(''); self.p41.setReadOnly(True)
        self.p42.setPlainText(''); self.p42.setReadOnly(True)
        self.p43.setPlainText(''); self.p43.setReadOnly(True)
        self.p44.setPlainText(''); self.p44.setReadOnly(True)
        self.p45.setPlainText(''); self.p45.setReadOnly(True)
        self.p46.setPlainText(''); self.p46.setReadOnly(True)
        self.p47.setPlainText(''); self.p47.setReadOnly(True)
        self.p48.setPlainText(''); self.p48.setReadOnly(True)
        self.p49.setPlainText(''); self.p49.setReadOnly(True)
        self.p50.setPlainText(''); self.p50.setReadOnly(True)
        self.p51.setPlainText(''); self.p51.setReadOnly(True)
        self.p52.setPlainText(''); self.p52.setReadOnly(True)
        self.p53.setPlainText(''); self.p53.setReadOnly(True)
        self.p54.setPlainText(''); self.p54.setReadOnly(True)
        self.p55.setPlainText(''); self.p55.setReadOnly(True)
        self.p56.setPlainText(''); self.p56.setReadOnly(True)
        self.p57.setPlainText(''); self.p57.setReadOnly(True)
        self.p58.setPlainText(''); self.p58.setReadOnly(True)
        self.p59.setPlainText(''); self.p59.setReadOnly(True)
        self.p60.setPlainText(''); self.p60.setReadOnly(True)
        self.p61.setPlainText(''); self.p61.setReadOnly(True)
        self.p62.setPlainText(''); self.p62.setReadOnly(True)
        self.p63.setPlainText(''); self.p63.setReadOnly(True)
        self.p64.setPlainText(''); self.p64.setReadOnly(True)
        self.p65.setPlainText(''); self.p65.setReadOnly(True)
        self.p66.setPlainText(''); self.p66.setReadOnly(True)
        self.p67.setPlainText(''); self.p67.setReadOnly(True)
        self.p68.setPlainText(''); self.p68.setReadOnly(True)
        self.p69.setPlainText(''); self.p69.setReadOnly(True)
        self.p70.setPlainText(''); self.p70.setReadOnly(True)
        self.p71.setPlainText(''); self.p71.setReadOnly(True)
        self.p72.setPlainText(''); self.p72.setReadOnly(True)
        self.p73.setPlainText(''); self.p73.setReadOnly(True)
        self.p74.setPlainText(''); self.p74.setReadOnly(True)
        self.p75.setPlainText(''); self.p75.setReadOnly(True)
        self.p76.setPlainText(''); self.p76.setReadOnly(True)
        self.p77.setPlainText(''); self.p77.setReadOnly(True)
        self.p78.setPlainText(''); self.p78.setReadOnly(True)
        self.p79.setPlainText(''); self.p79.setReadOnly(True)
        self.p80.setPlainText(''); self.p80.setReadOnly(True)
        self.p81.setPlainText(''); self.p81.setReadOnly(True)            
        
    def click1(self):
        global pole, font
        if not self.game:
            self.level = 1
            self.game = True
            aa()
            self.lbl.setText('')
            self.p1.setReadOnly(False); self.p28.setReadOnly(False); self.p55.setReadOnly(False)
            self.p29.setReadOnly(False); self.p59.setReadOnly(False)
            self.p3.setReadOnly(False); self.p31.setReadOnly(False); self.p60.setReadOnly(False)
            self.p5.setReadOnly(False); self.p33.setReadOnly(False); self.p61.setReadOnly(False)
            self.p7.setReadOnly(False); self.p34.setReadOnly(False); self.p62.setReadOnly(False)
            self.p9.setReadOnly(False); self.p36.setReadOnly(False); self.p64.setReadOnly(False)
            self.p13.setReadOnly(False); self.p39.setReadOnly(False); self.p65.setReadOnly(False)
            self.p14.setReadOnly(False); self.p41.setReadOnly(False); self.p66.setReadOnly(False)
            self.p16.setReadOnly(False); self.p67.setReadOnly(False)
            self.p17.setReadOnly(False); self.p43.setReadOnly(False); self.p69.setReadOnly(False)
            self.p45.setReadOnly(False); self.p71.setReadOnly(False)
            self.p20.setReadOnly(False); self.p47.setReadOnly(False)
            self.p21.setReadOnly(False); self.p48.setReadOnly(False); self.p74.setReadOnly(False)
            self.p22.setReadOnly(False); self.p49.setReadOnly(False); self.p76.setReadOnly(False)
            self.p23.setReadOnly(False); self.p51.setReadOnly(False); self.p77.setReadOnly(False)
            self.p27.setReadOnly(False); self.p53.setReadOnly(False); self.p80.setReadOnly(False)     
            self.p81.setReadOnly(False)
            self.p1.setFont(font1); self.p28.setFont(font1); self.p55.setFont(font1)
            self.p29.setFont(font1); self.p59.setFont(font1)
            self.p3.setFont(font1); self.p31.setFont(font1); self.p60.setFont(font1)
            self.p5.setFont(font1); self.p33.setFont(font1); self.p61.setFont(font1)
            self.p7.setFont(font1); self.p34.setFont(font1); self.p62.setFont(font1)
            self.p9.setFont(font1); self.p36.setFont(font1); self.p64.setFont(font1)
            self.p13.setFont(font1); self.p39.setFont(font1); self.p65.setFont(font1)
            self.p14.setFont(font1); self.p41.setFont(font1); self.p66.setFont(font1)
            self.p16.setFont(font1); self.p67.setFont(font1)
            self.p17.setFont(font1); self.p43.setFont(font1); self.p69.setFont(font1)
            self.p45.setFont(font1); self.p71.setFont(font1)
            self.p20.setFont(font1); self.p47.setFont(font1)
            self.p21.setFont(font1); self.p48.setFont(font1); self.p74.setFont(font1)
            self.p22.setFont(font1); self.p49.setFont(font1); self.p76.setFont(font1)
            self.p23.setFont(font1); self.p51.setFont(font1); self.p77.setFont(font1)
            self.p27.setFont(font1); self.p53.setFont(font1); self.p80.setFont(font1)     
            self.p81.setFont(font1)   
            self.p6.setPlainText(str(pole[0][5])); self.p6.setReadOnly(True); self.p6.setFont(font)
            self.p4.setPlainText(str(pole[0][3])); self.p4.setReadOnly(True); self.p4.setFont(font)
            self.p8.setPlainText(str(pole[0][7])); self.p8.setReadOnly(True); self.p8.setFont(font)
            self.p10.setPlainText(str(pole[1][0])); self.p10.setReadOnly(True); self.p10.setFont(font)
            self.p11.setPlainText(str(pole[1][1])); self.p11.setReadOnly(True); self.p11.setFont(font)
            self.p12.setPlainText(str(pole[1][2])); self.p12.setReadOnly(True); self.p12.setFont(font)
            self.p15.setPlainText(str(pole[1][5])); self.p15.setReadOnly(True); self.p15.setFont(font)
            self.p19.setPlainText(str(pole[2][0])); self.p19.setReadOnly(True); self.p19.setFont(font)
            self.p24.setPlainText(str(pole[2][5])); self.p24.setReadOnly(True); self.p24.setFont(font)
            self.p25.setPlainText(str(pole[2][6])); self.p25.setReadOnly(True); self.p25.setFont(font)
            self.p26.setPlainText(str(pole[2][7])); self.p26.setReadOnly(True); self.p26.setFont(font)
            self.p30.setPlainText(str(pole[3][2])); self.p30.setReadOnly(True); self.p30.setFont(font)
            self.p32.setPlainText(str(pole[3][4])); self.p32.setReadOnly(True); self.p32.setFont(font)
            self.p35.setPlainText(str(pole[3][7])); self.p35.setReadOnly(True); self.p35.setFont(font)
            self.p37.setPlainText(str(pole[4][0])); self.p37.setReadOnly(True); self.p37.setFont(font)
            self.p38.setPlainText(str(pole[4][1])); self.p38.setReadOnly(True); self.p38.setFont(font)
            self.p40.setPlainText(str(pole[4][3])); self.p40.setReadOnly(True); self.p40.setFont(font)
            self.p44.setPlainText(str(pole[4][7])); self.p44.setReadOnly(True); self.p44.setFont(font)          
            self.p46.setPlainText(str(pole[5][0])); self.p46.setReadOnly(True); self.p46.setFont(font)
            self.p50.setPlainText(str(pole[5][4])); self.p50.setReadOnly(True); self.p50.setFont(font)
            self.p52.setPlainText(str(pole[5][6])); self.p52.setReadOnly(True); self.p52.setFont(font)
            self.p54.setPlainText(str(pole[5][8])); self.p54.setReadOnly(True); self.p54.setFont(font)
            self.p56.setPlainText(str(pole[6][1])); self.p56.setReadOnly(True); self.p56.setFont(font)
            self.p57.setPlainText(str(pole[6][2])); self.p57.setReadOnly(True); self.p57.setFont(font)
            self.p58.setPlainText(str(pole[6][3])); self.p58.setReadOnly(True); self.p58.setFont(font)
            self.p63.setPlainText(str(pole[6][8])); self.p63.setReadOnly(True); self.p63.setFont(font)
            self.p68.setPlainText(str(pole[7][4])); self.p68.setReadOnly(True); self.p68.setFont(font)
            self.p70.setPlainText(str(pole[7][6])); self.p70.setReadOnly(True); self.p70.setFont(font)
            self.p72.setPlainText(str(pole[7][8])); self.p72.setReadOnly(True); self.p72.setFont(font)
            self.p75.setPlainText(str(pole[8][2])); self.p75.setReadOnly(True); self.p75.setFont(font)
            self.p78.setPlainText(str(pole[8][5])); self.p78.setReadOnly(True); self.p78.setFont(font)
            self.p79.setPlainText(str(pole[8][6])); self.p79.setReadOnly(True); self.p79.setFont(font)
            self.p73.setPlainText(str(pole[8][0])); self.p73.setReadOnly(True); self.p73.setFont(font)
            self.p2.setPlainText(str(pole[0][1])); self.p2.setReadOnly(True); self.p2.setFont(font)
            self.p18.setPlainText(str(pole[1][8])); self.p18.setReadOnly(True); self.p18.setFont(font)
            self.p42.setPlainText(str(pole[4][5])); self.p42.setReadOnly(True); self.p42.setFont(font)
        
    def click2(self):
        global pole
        if not self.game:
            self.level = 2
            self.game = True
            aa()
            self.lbl.setText('')
            self.p2.setReadOnly(False); self.p23.setReadOnly(False); self.p44.setReadOnly(False)
            self.p4.setReadOnly(False); self.p24.setReadOnly(False)
            self.p5.setReadOnly(False); self.p26.setReadOnly(False); self.p47.setReadOnly(False)
            self.p7.setReadOnly(False); self.p27.setReadOnly(False); self.p48.setReadOnly(False)
            self.p8.setReadOnly(False); self.p28.setReadOnly(False); self.p49.setReadOnly(False)
            self.p10.setReadOnly(False); self.p30.setReadOnly(False); self.p51.setReadOnly(False)
            self.p11.setReadOnly(False); self.p33.setReadOnly(False); self.p53.setReadOnly(False)
            self.p12.setReadOnly(False); self.p34.setReadOnly(False)
            self.p14.setReadOnly(False); self.p36.setReadOnly(False); self.p56.setReadOnly(False)
            self.p16.setReadOnly(False); self.p37.setReadOnly(False); self.p59.setReadOnly(False)
            self.p17.setReadOnly(False); self.p39.setReadOnly(False); self.p60.setReadOnly(False)
            self.p40.setReadOnly(False); self.p61.setReadOnly(False)
            self.p20.setReadOnly(False); self.p41.setReadOnly(False); self.p62.setReadOnly(False)
            self.p63.setReadOnly(False); self.p67.setReadOnly(False); self.p71.setReadOnly(False)
            self.p64.setReadOnly(False); self.p68.setReadOnly(False); self.p72.setReadOnly(False)
            self.p65.setReadOnly(False); self.p70.setReadOnly(False); self.p73.setReadOnly(False)
            self.p75.setReadOnly(False); self.p79.setReadOnly(False)
            self.p76.setReadOnly(False); self.p78.setReadOnly(False)
            self.p2.setFont(font1); self.p23.setFont(font1); self.p44.setFont(font1)
            self.p4.setFont(font1); self.p24.setFont(font1)
            self.p5.setFont(font1); self.p26.setFont(font1); self.p47.setFont(font1)
            self.p7.setFont(font1); self.p27.setFont(font1); self.p48.setFont(font1)
            self.p8.setFont(font1); self.p28.setFont(font1); self.p49.setFont(font1)
            self.p10.setFont(font1); self.p30.setFont(font1); self.p51.setFont(font1)
            self.p11.setFont(font1); self.p33.setFont(font1); self.p53.setFont(font1)
            self.p12.setFont(font1); self.p34.setFont(font1)
            self.p14.setFont(font1); self.p36.setFont(font1); self.p56.setFont(font1)
            self.p16.setFont(font1); self.p37.setFont(font1); self.p59.setFont(font1)
            self.p17.setFont(font1); self.p39.setFont(font1); self.p60.setFont(font1)
            self.p40.setFont(font1); self.p61.setFont(font1)
            self.p20.setFont(font1); self.p41.setFont(font1); self.p62.setFont(font1)
            self.p63.setFont(font1); self.p67.setFont(font1); self.p71.setFont(font1)
            self.p64.setFont(font1); self.p68.setFont(font1); self.p72.setFont(font1)
            self.p65.setFont(font1); self.p70.setFont(font1); self.p73.setFont(font1)
            self.p75.setFont(font1); self.p79.setFont(font1)
            self.p76.setFont(font1); self.p78.setFont(font1)
            self.p1.setPlainText(str(pole[0][0])); self.p1.setReadOnly(True); self.p1.setFont(font)
            self.p3.setPlainText(str(pole[0][2])); self.p3.setReadOnly(True); self.p3.setFont(font)
            self.p6.setPlainText(str(pole[0][5])); self.p6.setReadOnly(True); self.p6.setFont(font)
            self.p9.setPlainText(str(pole[0][8])); self.p9.setReadOnly(True); self.p9.setFont(font)
            self.p13.setPlainText(str(pole[1][3])); self.p13.setReadOnly(True); self.p13.setFont(font)
            self.p15.setPlainText(str(pole[1][5])); self.p15.setReadOnly(True); self.p15.setFont(font)
            self.p18.setPlainText(str(pole[1][8])); self.p18.setReadOnly(True); self.p18.setFont(font)
            self.p21.setPlainText(str(pole[2][2])); self.p21.setReadOnly(True); self.p21.setFont(font)
            self.p22.setPlainText(str(pole[2][3])); self.p22.setReadOnly(True); self.p22.setFont(font)
            self.p25.setPlainText(str(pole[2][6])); self.p25.setReadOnly(True); self.p25.setFont(font)
            self.p29.setPlainText(str(pole[3][1])); self.p29.setReadOnly(True); self.p29.setFont(font)
            self.p31.setPlainText(str(pole[3][3])); self.p31.setReadOnly(True); self.p31.setFont(font)
            self.p32.setPlainText(str(pole[3][4])); self.p32.setReadOnly(True); self.p32.setFont(font)
            self.p35.setPlainText(str(pole[3][7])); self.p35.setReadOnly(True); self.p35.setFont(font)
            self.p38.setPlainText(str(pole[4][1])); self.p38.setReadOnly(True); self.p38.setFont(font)
            self.p42.setPlainText(str(pole[4][5])); self.p42.setReadOnly(True); self.p42.setFont(font)
            self.p43.setPlainText(str(pole[4][6])); self.p43.setReadOnly(True); self.p43.setFont(font)
            self.p46.setPlainText(str(pole[5][0])); self.p46.setReadOnly(True); self.p46.setFont(font)
            self.p50.setPlainText(str(pole[5][4])); self.p50.setReadOnly(True); self.p50.setFont(font)
            self.p52.setPlainText(str(pole[5][6])); self.p52.setReadOnly(True); self.p52.setFont(font)
            self.p55.setPlainText(str(pole[6][0])); self.p55.setReadOnly(True); self.p55.setFont(font)
            self.p57.setPlainText(str(pole[6][2])); self.p57.setReadOnly(True); self.p57.setFont(font)
            self.p58.setPlainText(str(pole[6][3])); self.p58.setReadOnly(True); self.p58.setFont(font)
            self.p66.setPlainText(str(pole[7][2])); self.p66.setReadOnly(True); self.p66.setFont(font)
            self.p68.setPlainText(str(pole[7][4])); self.p68.setReadOnly(True); self.p68.setFont(font)
            self.p69.setPlainText(str(pole[7][5])); self.p69.setReadOnly(True); self.p69.setFont(font)
            self.p71.setPlainText(str(pole[7][7])); self.p71.setReadOnly(True); self.p71.setFont(font)
            self.p74.setPlainText(str(pole[8][1])); self.p74.setReadOnly(True); self.p74.setFont(font)
            self.p80.setPlainText(str(pole[8][7])); self.p80.setReadOnly(True); self.p80.setFont(font)
            self.p81.setPlainText(str(pole[8][8])); self.p81.setReadOnly(True); self.p81.setFont(font)
            self.p19.setPlainText(str(pole[2][0])); self.p19.setReadOnly(True); self.p19.setFont(font)
            self.p45.setPlainText(str(pole[4][8])); self.p45.setReadOnly(True); self.p45.setFont(font)
            self.p54.setPlainText(str(pole[5][8])); self.p54.setReadOnly(True); self.p54.setFont(font)
            self.p77.setPlainText(str(pole[8][4])); self.p77.setReadOnly(True); self.p77.setFont(font)
        
    def click3(self):
        global pole
        if not self.game:
            self.level = 3
            self.game = True
            aa()
            self.lbl.setText('')
            self.p2.setReadOnly(False); self.p20.setReadOnly(False); self.p35.setReadOnly(False)
            self.p3.setReadOnly(False); self.p22.setReadOnly(False); self.p36.setReadOnly(False)
            self.p5.setReadOnly(False); self.p24.setReadOnly(False); self.p37.setReadOnly(False)
            self.p6.setReadOnly(False); self.p25.setReadOnly(False); self.p38.setReadOnly(False)
            self.p8.setReadOnly(False); self.p26.setReadOnly(False); self.p40.setReadOnly(False)
            self.p9.setReadOnly(False); self.p27.setReadOnly(False); self.p41.setReadOnly(False)
            self.p10.setReadOnly(False); self.p28.setReadOnly(False); self.p42.setReadOnly(False)
            self.p12.setReadOnly(False); self.p30.setReadOnly(False); self.p44.setReadOnly(False)
            self.p13.setReadOnly(False)
            self.p15.setReadOnly(False); self.p32.setReadOnly(False); self.p47.setReadOnly(False)
            self.p16.setReadOnly(False); self.p51.setReadOnly(False)
            self.p52.setReadOnly(False); self.p59.setReadOnly(False); self.p65.setReadOnly(False)
            self.p53.setReadOnly(False); self.p60.setReadOnly(False); self.p66.setReadOnly(False)
            self.p54.setReadOnly(False); self.p61.setReadOnly(False); self.p68.setReadOnly(False)
            self.p57.setReadOnly(False); self.p63.setReadOnly(False); self.p70.setReadOnly(False)
            self.p58.setReadOnly(False); self.p64.setReadOnly(False); self.p71.setReadOnly(False)
            self.p73.setReadOnly(False); self.p79.setReadOnly(False)
            self.p75.setReadOnly(False); self.p81.setReadOnly(False)
            self.p77.setReadOnly(False)
            self.p78.setReadOnly(False)
            self.p2.setFont(font1); self.p20.setFont(font1); self.p35.setFont(font1)
            self.p3.setFont(font1); self.p22.setFont(font1); self.p36.setFont(font1)
            self.p5.setFont(font1); self.p24.setFont(font1); self.p37.setFont(font1)
            self.p6.setFont(font1); self.p25.setFont(font1); self.p38.setFont(font1)
            self.p8.setFont(font1); self.p26.setFont(font1); self.p40.setFont(font1)
            self.p9.setFont(font1); self.p27.setFont(font1); self.p41.setFont(font1)
            self.p10.setFont(font1); self.p28.setFont(font1); self.p42.setFont(font1)
            self.p12.setFont(font1); self.p30.setFont(font1); self.p44.setFont(font1)
            self.p13.setFont(font1)
            self.p15.setFont(font1); self.p32.setFont(font1); self.p47.setFont(font1)
            self.p16.setFont(font1); self.p51.setFont(font1)
            self.p52.setFont(font1); self.p59.setFont(font1); self.p65.setFont(font1)
            self.p53.setFont(font1); self.p60.setFont(font1); self.p66.setFont(font1)
            self.p54.setFont(font1); self.p61.setFont(font1); self.p68.setFont(font1)
            self.p57.setFont(font1); self.p63.setFont(font1); self.p70.setFont(font1)
            self.p58.setFont(font1); self.p64.setFont(font1); self.p71.setFont(font1)
            self.p73.setFont(font1); self.p79.setFont(font1)
            self.p75.setFont(font1); self.p81.setFont(font1)
            self.p77.setFont(font1)
            self.p78.setFont(font1)
            self.p1.setPlainText(str(pole[0][0])); self.p1.setReadOnly(True); self.p1.setFont(font)
            self.p4.setPlainText(str(pole[0][3])); self.p4.setReadOnly(True); self.p4.setFont(font)
            self.p7.setPlainText(str(pole[0][6])); self.p7.setReadOnly(True); self.p7.setFont(font)
            self.p11.setPlainText(str(pole[1][1])); self.p11.setReadOnly(True); self.p11.setFont(font)
            self.p14.setPlainText(str(pole[1][4])); self.p14.setReadOnly(True); self.p14.setFont(font)
            self.p17.setPlainText(str(pole[1][7])); self.p17.setReadOnly(True); self.p17.setFont(font)
            self.p18.setPlainText(str(pole[1][8])); self.p18.setReadOnly(True); self.p18.setFont(font)
            self.p19.setPlainText(str(pole[2][0])); self.p19.setReadOnly(True); self.p19.setFont(font)
            self.p21.setPlainText(str(pole[2][2])); self.p21.setReadOnly(True); self.p21.setFont(font)
            self.p23.setPlainText(str(pole[2][4])); self.p23.setReadOnly(True); self.p23.setFont(font)
            self.p29.setPlainText(str(pole[3][1])); self.p29.setReadOnly(True); self.p29.setFont(font)
            self.p34.setPlainText(str(pole[3][6])); self.p34.setReadOnly(True); self.p34.setFont(font)
            self.p39.setPlainText(str(pole[4][2])); self.p39.setReadOnly(True); self.p39.setFont(font)
            self.p43.setPlainText(str(pole[4][6])); self.p43.setReadOnly(True); self.p43.setFont(font)
            self.p45.setPlainText(str(pole[4][8])); self.p45.setReadOnly(True); self.p45.setFont(font)
            self.p48.setPlainText(str(pole[5][2])); self.p48.setReadOnly(True); self.p48.setFont(font)
            self.p49.setPlainText(str(pole[5][3])); self.p49.setReadOnly(True); self.p49.setFont(font)
            self.p50.setPlainText(str(pole[5][4])); self.p50.setReadOnly(True); self.p50.setFont(font)
            self.p55.setPlainText(str(pole[6][0])); self.p55.setReadOnly(True); self.p55.setFont(font)
            self.p56.setPlainText(str(pole[6][1])); self.p56.setReadOnly(True); self.p56.setFont(font)
            self.p62.setPlainText(str(pole[6][7])); self.p62.setReadOnly(True); self.p62.setFont(font)
            self.p67.setPlainText(str(pole[7][3])); self.p67.setReadOnly(True); self.p67.setFont(font)
            self.p69.setPlainText(str(pole[7][5])); self.p69.setReadOnly(True); self.p69.setFont(font)
            self.p72.setPlainText(str(pole[7][8])); self.p72.setReadOnly(True); self.p72.setFont(font)
            self.p74.setPlainText(str(pole[8][1])); self.p74.setReadOnly(True); self.p74.setFont(font)
            self.p76.setPlainText(str(pole[8][3])); self.p76.setReadOnly(True); self.p76.setFont(font)
            self.p80.setPlainText(str(pole[8][7])); self.p80.setReadOnly(True); self.p80.setFont(font)
            self.p31.setPlainText(str(pole[3][3])); self.p31.setReadOnly(True); self.p31.setFont(font)
            self.p33.setPlainText(str(pole[3][5])); self.p33.setReadOnly(True); self.p33.setFont(font)
            self.p46.setPlainText(str(pole[5][0])); self.p46.setReadOnly(True); self.p46.setFont(font)

S = []
pole = []
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())



