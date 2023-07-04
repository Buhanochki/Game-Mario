from tkinter import *
import time as t
import random

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
        self.sprites = []
        self.ground_up = PhotoImage(file='pic/up.png')
        self.ground_down = PhotoImage(file='pic/down.png')
        self.side_left = PhotoImage(file='pic/ls.png')
        self.side_right = PhotoImage(file='pic/rs.png')
        self.bg = [PhotoImage(file='pic/sky.png'), PhotoImage(file='pic/sky2.png'), PhotoImage(file='pic/sky3.png'), PhotoImage(file='pic/sky4.png'), PhotoImage(file='pic/sky5.png'), PhotoImage(file='pic/sky6.png')]
        self.block_sprites = []
        self.side_sprites = []
        self.data = [['0','0','0','0','0','0','0','0','0','0','0','0','0'],
                     ['0','0','0','0','0','0','0','0','0','0','0','0','0'],
                     ['0','0','0','0','0','0','0','0','0','0','0','0','0'],
                     ['0','0','0','0','0','0','0','0','0','0','0','0','0'],
                     ['0','0','0','0','0','0','0','0','0','0','0','0','0'],
                     ['0','0','0','0','0','0','0','0','0','0','0','0','0'],
                     ['u','u','u','u','u','u','u','u','u','u','u','u','u'],
                     ['g','g','g','g','g','g','g','g','g','g','g','g','g'],
                     ['g','g','g','g','g','g','g','g','g','g','g','g','g'],
                     ['g','g','g','g','g','g','g','g','g','g','g','g','g'],
                     ['g','g','g','g','g','g','g','g','g','g','g','g','g']] 
        for y in range(10):
            for x in range(13):
                print(y, x)
                if self.data[y][x] == '0':
                    self.gui.field.create_image(x * 64, y * 64, image = random.choice(self.bg), anchor='nw')
                elif self.data[y][x] == 'u':
                    self.block_sprites.append(self.gui.field.create_image(x * 64, y * 64, image = self.ground_up, anchor='nw'))

                elif self.data[y][x] =='g':
                    self.block_sprites.append(self.gui.field.create_image(x * 64, y * 64, image = self.ground_down, anchor='nw'))
                

class Hero():
    def __init__(self, gui: GUI, field: Field):
        self.gui = gui
        self.hero_movement_right = [PhotoImage(file = 'pic/walk1.png'), PhotoImage(file = 'pic/walk2.png'), PhotoImage(file = 'pic/walk3.png'), PhotoImage(file = 'pic/hero.png')]
        self.hero_movement_left = [PhotoImage(file = 'pic/walk4.png'), PhotoImage(file = 'pic/walk5.png'), PhotoImage(file = 'pic/walk6.png'), PhotoImage(file = 'pic/hero2.png')]
        self.hero_id = self.gui.field.create_image(0,0, image = self.hero_movement_right[3], anchor='nw')
        self.field = field
        self.cnt = 0
        self.vel_x = 0
        self.vel_y = 0
    def move_left(self):
        for e in range(4):
            self.gui.field.move(self.hero_id,-16, 0)
            self.gui.field.itemconfig(self.hero_id, image=self.hero_movement_left[self.cnt])
            t.sleep(0.1)
            self.gui.root.update()
            self.cnt = (self.cnt + 1) %4
    def move_right(self):
        for e in range(4):
            self.gui.field.move(self.hero_id, 16, 0)
            self.gui.field.itemconfig(self.hero_id, image=self.hero_movement_right[self.cnt])
            t.sleep(0.1)
            self.gui.root.update()
            self.cnt = (self.cnt + 1) % 4

    def move(self):
        self.gui.field.move(self.hero_id, self.vel_x, self.vel_y)
    def intersection(self):
        for sprite in self.field.block_sprites:
            if self.gui.field.coords(self.hero_id)[2] in range(self.gui.field(sprite)[2], self.gui.field(sprite)[0]) and self.gui.coords(self.hero_id)[3] in range(self.gui.field(sprite)[1], self.gui.field.coords(sprite)[3]):
                self.gui.field.move(self.hero_id, 0, -16)
        

        


        


g = GUI()
f = Field(g)
hero = Hero(g, f)
'''while 1:
    g.field.move(hero.hero_id, 0, -16)'''
g.root.mainloop()