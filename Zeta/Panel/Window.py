import Zeta

from tkinter import *
from .Toplevel2 import Toplevel2

class Primary(Toplevel2):
    def __init__(self, draggable=False, border='mono', color=7, color2='', mode='basic', style='even', title='Title', safemode=False, *args, **kwargs):
        Toplevel2.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        self.color2 = color2
        self.neon = Zeta.Color.Neon(color=color, color2=color2).hex
        self.hue = Zeta.Color.Neon(color=color, color2=color2).hue
        self.tint = Zeta.Color.Neon(color=color, color2=color2).tint
        self.raw = Zeta.Color.Neon(color=color, color2=color2).raw
        if draggable: self.bind_rightclick()

        if border=='mono': from .Frame.Mono import MonoFrame as ColorFrame
        elif border=='corner': from .Frame.Corner import CornerFrame as ColorFrame
        elif border=='gradient': from .Frame.Gradient import GradientFrame as ColorFrame
        gradient_frame = ColorFrame(self, color=color, color2=color2)
        gradient_frame.pack(side="top", fill="both", expand=True)

        if mode=='basic': from .Decoration import Basic as ControlFrame
        if mode!='border':
            control_frame = ControlFrame(gradient_frame, color=color, color2=color2, title=title, safemode=safemode)
            control_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        # if mode=='border': Frame.__init__(self, gradient_frame, *args, **kwargs)
        # else: Frame.__init__(self, control_frame, *args, **kwargs)
        if mode=='border': self.frame = Frame(gradient_frame)
        else: self.frame = Frame(control_frame)
        self.frame['background'] = hue
        self.frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

class Fallback(Toplevel2):
    def __init__(self, draggable=False, color=7, color2='', mode='basic', title='Title', *args, **kwargs):
        Toplevel2.__init__(self, *args, **kwargs)
        self.overrideredirect(True)
        self.color2 = color2
        self.neon = Zeta.Color.Neon(color=color, color2=color2).hex
        self.hue = Zeta.Color.Neon(color=color, color2=color2).hue
        # self['background'] = self.hue
        if draggable: self.bind_rightclick()

        frame1 = Frame(self)
        frame1.pack(side="top", fill="both", expand=True, ipadx=1, ipady=1)
        #frame1['highlightbackground'] = neon
        #frame1['highlightthickness'] = 1
        frame1['background'] = self.neon

        if mode=='basic': from .Decoration import Basic as ControlFrame
        if mode!='border':
            control_frame = ControlFrame(frame1, color=color, color2=color2, title=title)
            control_frame.pack(side="top", fill="both", expand=True, padx=1, pady=1)

        if mode=='border': self.frame = Frame(frame1)
        else: self.frame = Frame(control_frame)
        self.frame['background'] = self.hue
        self.frame.pack(side="top", fill="both", expand=True, ipadx=3, ipady=3, padx=1, pady=1)

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        frame1 = Panel(color2='green', mode='basic', border='corner', title='Sample app')

        b1 = Button(frame1, text="Close",command=self.destroy)
        t1 = Text(frame1, width=40, height=10)
        b1.pack(side="top")
        t1.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    app=SampleApp()
    app.mainloop()