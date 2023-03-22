import keyboard
import tkinter as tk
from tkinter import RAISED, FLAT


class App(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.alph = ["s","d","r","_","down","w","a","enter","esc", "up"]
        self.up = tk.Label(self, text ='↑', bg='white', relief=RAISED, font=(15), width=6)
        self.down = tk.Label(self, text ='↓', bg='white', relief=RAISED, font=(15), width=6)
        self.w = tk.Label(self, text ='W', bg='white', relief=RAISED, font=(15), width=6)
        self.a = tk.Label(self, text ='A', bg='white', relief=RAISED, font=(15), width=6)
        self.s = tk.Label(self, text ='S', bg='white', relief=RAISED, font=(15), width=6)
        self.d = tk.Label(self, text ='D', bg='white', relief=RAISED, font=(15), width=6)
        self.r = tk.Label(self, text ='R', bg='white', relief=RAISED, font=(15), width=6)
        self.enter = tk.Label(self, text ='ENTR', bg='white', relief=RAISED, font=(15), width=6)
        self.right_esc = tk.Label(self, text ='ESC', bg='white', relief=RAISED, font=(15), width=6)
        self._ = tk.Label(self, text=' ', bg='white', relief=RAISED, font=(15), width=6)
        self.pack()
        self.labels = {'w':self.w, 'a':self.a, 's':self.s, 'd':self.d, 'r':self.r, '_':self._, 'up':self.up,'down':self.down,'enter':self.enter, 'esc':self.right_esc}

        self.all_labels()
        
        self.togetherness()

    def keyboard_states(self):
        key_stroke = keyboard.read_event()
        if key_stroke.name in self.alph:
            return key_stroke.name, key_stroke.event_type
        else:
            pass

    def all_labels(self):
        piss = 0
        pissy = 1
        for i in self.alph:
            self.labels[i].grid(row=pissy, column=piss)
            if piss >= 4:
                piss = 0
                pissy = 0
            else:
                piss = piss + 1
    
    def togetherness(self):
        states = self.keyboard_states()
        if states != None:
            pp = states[0]
            if pp in self.alph:
                if states[1] == 'down':
                    self.labels[pp].configure(relief=FLAT)
                    #print(pp,"down")
                elif states[1] == 'up':
                    self.labels[pp].config(relief=RAISED)
                    #print(pp,"up")
        else:
            pass
        self.after(1, self.togetherness)
            

root = tk.Tk()
myapp = App(root)
root.title("Keyboard-Overlay")
root.mainloop()