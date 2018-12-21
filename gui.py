#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Dec 21, 2018 07:13:03 PM CET  platform: Windows NT

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    gui_support.set_Tk_var()
    top = Module_drag_and_drop (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Module_drag_and_drop(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    gui_support.set_Tk_var()
    top = Module_drag_and_drop (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Module_drag_and_drop():
    global w
    w.destroy()
    w = None

class Module_drag_and_drop:
    current = None
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        top.geometry("800x725+20+0")
        top.title("Module drag and drop")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.038, rely=0.05, height=33, width=81)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=gui_support.select_files)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Open Files''')

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.475, rely=0.025, relheight=0.956
                , relwidth=0.506)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=405)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.0, rely=0.007, relheight=0.98, relwidth=0.968)

        self.Message1.configure(anchor=NW)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''NAMING SCHEME:
_ is used as separator never use _ outside of separating elements.

groupname_type_nr-in-group

groupname:
Can be anything as long as it does not contain separators.

type:
Type of component (see list below for possibilities)

nr:
Nr. of component in group.

OPTIONS:
Include 'left' or 'right' in the group name if you potentially want your group to be mirrored.
Include 'nogroup' no group will be assigned. This MUST be done for ship wide shields otherwise the shield will shield the components in the group only.

Examples:
left-top-bat-1_lturret_2
let-nogroup_lshield_1

INJECTION AND MIRRORING:
Mirroring can be turned off and on in general or for each file or individually. Mirroring will be done over the left/right side.

Injection is a feature were you can inject your connections into an excising ship file.
Injection can be turned off and on in general or for each file or individually. When injecting is on user will be prompted what file to inject into.
All new connections will be injected below the last connection in the selected file.''')
        self.Message1.configure(width=392)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.038, rely=0.013, height=26, width=189)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Select Files to be processed''')

        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.038, rely=0.1, relheight=0.306, relwidth=0.431)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#d9d9d9")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")
        self.Frame3.configure(width=345)

        self.file_list_box = Listbox(self.Frame3, selectmode=EXTENDED)
        self.file_list_box.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

        self.file_list_box.configure(background="white")
        self.file_list_box.configure(disabledforeground="#a3a3a3")
        self.file_list_box.configure(font="TkFixedFont")
        self.file_list_box.configure(foreground="#000000")
        self.file_list_box.configure(highlightbackground="#d9d9d9")
        self.file_list_box.configure(highlightcolor="black")
        self.file_list_box.configure(selectbackground="#c4c4c4")
        self.file_list_box.configure(selectforeground="black")
        self.file_list_box.configure(width=345)
        self.file_list_box.configure(listvariable=gui_support.file_list)
        self.file_list_box.bind('<<ListboxSelect>>', self.onselect)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.038, rely=0.413, relheight=0.181
                , relwidth=0.256)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=205)

        self.mirror_on = Button(self.Frame2)
        self.mirror_on.place(relx=0.098, rely=0.276, height=33, width=76)
        self.mirror_on.configure(activebackground="#d9d9d9")
        self.mirror_on.configure(activeforeground="#000000")
        self.mirror_on.configure(background="#d9d9d9")
        self.mirror_on.configure(command=gui_support.mirror_on)
        self.mirror_on.configure(disabledforeground="#a3a3a3")
        self.mirror_on.configure(foreground="#000000")
        self.mirror_on.configure(highlightbackground="#d9d9d9")
        self.mirror_on.configure(highlightcolor="black")
        self.mirror_on.configure(pady="0")
        self.mirror_on.configure(text='''Mirror On''')

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.049, rely=0.069, height=26, width=182)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''On selected files''')
        self.Label3.configure(width=182)

        self.mirror_off = Button(self.Frame2)
        self.mirror_off.place(relx=0.537, rely=0.276, height=33, width=78)
        self.mirror_off.configure(activebackground="#d9d9d9")
        self.mirror_off.configure(activeforeground="#000000")
        self.mirror_off.configure(background="#d9d9d9")
        self.mirror_off.configure(command=gui_support.mirror_off)
        self.mirror_off.configure(disabledforeground="#a3a3a3")
        self.mirror_off.configure(foreground="#000000")
        self.mirror_off.configure(highlightbackground="#d9d9d9")
        self.mirror_off.configure(highlightcolor="black")
        self.mirror_off.configure(pady="0")
        self.mirror_off.configure(text='''Mirror Off''')

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.098, rely=0.621, height=33, width=76)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(command=gui_support.inject_on)
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Inject On''')
        self.Button5.configure(width=76)

        self.Button6 = Button(self.Frame2)
        self.Button6.place(relx=0.537, rely=0.621, height=33, width=76)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(command=gui_support.inject_off)
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Inject Off''')
        self.Button6.configure(width=76)

        self.Frame4 = Frame(top)
        self.Frame4.place(relx=0.038, rely=0.6, relheight=0.181, relwidth=0.256)
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(background="#d9d9d9")
        self.Frame4.configure(width=205)

        self.Label3_2 = Label(self.Frame4)
        self.Label3_2.place(relx=0.049, rely=0.069, height=26, width=182)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#d9d9d9")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(foreground="#000000")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''On all files''')
        self.Label3_2.configure(width=182)

        self.Button4 = Button(self.Frame4)
        self.Button4.place(relx=0.537, rely=0.276, height=33, width=76)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(command=gui_support.all_mirror_off)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Mirror Off''')
        self.Button4.configure(width=76)

        self.Button4_3 = Button(self.Frame4)
        self.Button4_3.place(relx=0.098, rely=0.276, height=33, width=76)
        self.Button4_3.configure(activebackground="#d9d9d9")
        self.Button4_3.configure(activeforeground="#000000")
        self.Button4_3.configure(background="#d9d9d9")
        self.Button4_3.configure(command=gui_support.all_mirror_on)
        self.Button4_3.configure(disabledforeground="#a3a3a3")
        self.Button4_3.configure(foreground="#000000")
        self.Button4_3.configure(highlightbackground="#d9d9d9")
        self.Button4_3.configure(highlightcolor="black")
        self.Button4_3.configure(pady="0")
        self.Button4_3.configure(text='''Mirror On''')

        self.Button7 = Button(self.Frame4)
        self.Button7.place(relx=0.098, rely=0.621, height=33, width=76)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(command=gui_support.all_inject_on)
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Inject On''')
        self.Button7.configure(width=76)

        self.Button7_4 = Button(self.Frame4)
        self.Button7_4.place(relx=0.537, rely=0.621, height=33, width=76)
        self.Button7_4.configure(activebackground="#d9d9d9")
        self.Button7_4.configure(activeforeground="#000000")
        self.Button7_4.configure(background="#d9d9d9")
        self.Button7_4.configure(command=gui_support.all_inject_off)
        self.Button7_4.configure(disabledforeground="#a3a3a3")
        self.Button7_4.configure(foreground="#000000")
        self.Button7_4.configure(highlightbackground="#d9d9d9")
        self.Button7_4.configure(highlightcolor="black")
        self.Button7_4.configure(pady="0")
        self.Button7_4.configure(text='''Inject Off''')

        self.Button4 = Button(top)
        self.Button4.place(relx=0.038, rely=0.8, height=143, width=206)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(command=gui_support.start_processing)
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Start''')
        self.Button4.configure(width=206)
        self.current = None

    def onselect(self, evt):
        now = self.file_list_box.curselection()
        if now != self.current:
            gui_support.update_from_selection(now)
            self.current = now
            
if __name__ == '__main__':
    vp_start_gui()