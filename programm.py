from tkinter import *
import time as t
class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1280x720')
        #self.root.resizable(False, False)

        self.field = Canvas(self.root, width=768, height=640, bg='red')
        self.field.place(x=472, y=40)

        self.code_field = Text(self.root, width=43, height=35)
        self.code_field.place(x=40, y=40)

        self.run_code_button = Button(self.root, text = 'Run Code', width=23, height = 4, command=self.code_run)
        self.run_code_button.place(x=40, y=635)
        
    def code_run(self):
        try:
            exec(self.code_field.get('1.0', END))
        except:
            print('Error')

class Field():
    def __init__(self, gui: GUI):
        self.gui = gui
        self.map = [['0' for e in range(50)] for e in range(40)]
        self.sprites = []
        self.ground_up = PhotoImage(file='pic/up.png')
        self.ground_down = PhotoImage(file='pic/down.png')

    def create_block(self, x, y):
        print(self.map)
        self.map[x][y] = 'x'
        self.sprites.append(self.gui.field.create_image(x * 16, y * 16, image=self.ground_up))

class Hero():
    def __init__(self, gui: GUI):
        self.gui = gui
        self.hero = PhotoImage(file='pic/hero.png')
        self.hero_id = self.gui.field.create_image(0,0, image = self.hero, anchor='nw')

    def move_up(self):
        for e in range(8):
            self.gui.field.move(self.hero_id, 0, -8)
            t.sleep(0.1)
            self.gui.root.update()
    def move_down(self):
        for e in range(8):
            self.gui.field.move(self.hero_id, 0, 8)
            t.sleep(0.1)
            self.gui.root.update()
    def move_left(self):
        for e in range(8):
            self.gui.field.move(self.hero_id,-8, 0)
            t.sleep(0.1)
            self.gui.root.update()
    def move_right(self):
        for e in range(8):
            self.gui.field.move(self.hero_id, 8, 0)
            t.sleep(0.1)
            self.gui.root.update()

        


        


g = GUI()
f = Field(g)
hero = Hero(g)
g.root.mainloop()