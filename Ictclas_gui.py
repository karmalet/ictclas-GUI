# =============================================================================
# ICTCLAS GUI
# Author: Minjun Park (karmalet@naver.com)
# 
# Graphic User Interface for ICTCLAS POS tagger.
# All rights belong to its owner, NLPIR-team(https://github.com/NLPIR-team).
# for personal use only.
# =============================================================================


from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import nlpir_jun, re
from nlpir_jun import detect_encoding, pos_tagging, Seg, to_byte,\
     tagprocessing, segprocessing

root = Tk()
root.title('ICTCLAS GUI')
##root.geometry('500x650+500+100')

class dummy:
    def __init__(self):
        self.wdir = '.'
        
    def open_file(self):
        fr = filedialog.askopenfilename(initialdir=self.wdir)
        self.wdir = re.findall(r'.*/', fr)[0]
        enc = detect_encoding(fr)
        # the contents that has read from the file -> Text
        with open(fr, encoding=enc) as handle:
            contents = handle.read()
        input_text.insert(1.0, contents)
        print('OPEN:{}'.format(fr))
        return
    
    def save_file(self):
        ft = filedialog.asksaveasfilename(initialdir=self.wdir)
        with open(ft, 'w', encoding = 'utf-8') as f:
            contents = output_text.get(1.0,'end')
            f.write(contents)
        print('WRITE:{}'.format(ft))
        return

def show_tagging_result():
    paragraph = input_text.get(1.0, 'end')
    tagging_result = tagprocessing(paragraph)
    tagging_result = '\n'.join(tagging_result)
    output_text.config(state='normal')
    output_text.insert('end', tagging_result)
##    output_text.bind("<Key>", lambda e: "break") # freeze output
##    output_text.config(state='disabled')

def show_segment_result():
    paragraph = input_text.get(1.0, 'end')
    seg_result = segprocessing(paragraph)
    seg_result = '\n'.join(seg_result)
    output_text.config(state='normal')
    output_text.insert('end', seg_result)
    
def clear():
##    output_text.config(state='normal')
    input_text.delete(1.0,'end')
    output_text.delete(1.0,'end')
    return

def show_choice():
    nlpir_jun.SetPOSmap(posmap.get())
    print(posmap.get())

# Creating Widgets
top_frame = ttk.Frame(root, padding =(3,3,12,12), relief="sunken")
label_1 = ttk.Label(top_frame, width = 20, text='Input text...', font = "Verdana 10 bold")
input_text = Text(top_frame)
Scrollbar_1 = Scrollbar(top_frame)

button_frame1 = Frame(root)#, background = 'red')
posbutton = Button(button_frame1, text = 'POS Tagging', relief='raised', command = show_tagging_result,\
                   font = "Verdana 10 bold")
segbutton = Button(button_frame1, text = 'Segmentation', relief='raised', command = show_segment_result,\
                   font = "Verdana 10 bold")

down_frame = ttk.Frame(root, padding =(3,3,12,12), relief="sunken")
label_2 = ttk.Label(down_frame, width = 20, text='Result', font = "Verdana 10 bold")
output_text = Text(down_frame)
Scrollbar_2 = Scrollbar(down_frame)

button_frame2 = Frame(root)#,background = 'yellow', height = 30)
dc = dummy()
openbutton = Button(button_frame2, text = 'Open...', command = dc.open_file)
savebutton = Button(button_frame2, text = 'Save As...', command = dc.save_file)
clearbutton = Button(button_frame2, text = 'Clear', command = clear)

# Layouting
top_frame.grid(column=0, row=0, sticky = (N,S,E,W))
label_1.grid(row=0, column=0, sticky='NW')
input_text.grid(row=1, column=0, sticky=(N,S,E,W), padx=(10,0), pady=(10,10))
input_text.config(yscrollcommand = Scrollbar_1.set)
Scrollbar_1.grid(row=1,column=1, sticky= (N,S,W), pady=(10,10))
Scrollbar_1.config(command=input_text.yview)

button_frame1.grid(row=1,column=0,sticky = (N,S,E,W))
posmap = IntVar()
tag_spec = [
    ('北大一级标注集', 3),
    ('北大二级标注集', 2),
    ('中科院一级标注集', 1),
    ('中科院二级标注集', 0)
    ]
for i, (txt, val) in enumerate(tag_spec):
    Radiobutton(button_frame1, text=txt, variable = posmap, \
                command=show_choice, value=val, relief='groove').pack(fill='x',expand = True,side=LEFT)
posbutton.pack(fill='x', expand=True, side=LEFT, ipadx=50, ipady=15, padx=(30,0))
segbutton.pack(fill='x', expand=True, side=LEFT, ipadx=50, ipady=15, padx=(30,0))

down_frame.grid(row=2,column=0, sticky = (N,S,E,W))
label_2.grid(row=0, column=0, sticky='NW')
output_text.grid(row=1, column=0, sticky='NWES', padx=(10,0), pady=(10,10))
output_text.config(yscrollcommand = Scrollbar_2.set)
Scrollbar_2.grid(row=1,column=3, sticky='NSW', pady=(10,10))
Scrollbar_2.config(command=output_text.yview)

button_frame2.grid(row=3,column=0, sticky = (N,S,E,W))
openbutton.pack(fill='x', side=LEFT, ipadx = 30, padx = 30, expand=True)
savebutton.pack(fill='x', side=LEFT, ipadx = 30, padx = 30, expand=True)
clearbutton.pack(fill='x', side=LEFT, ipadx = 30, padx = 30, expand=True)

# Resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
top_frame.columnconfigure(0, weight=1)
top_frame.rowconfigure(1, weight=1)
##button_frame1.columnfigure(0, weight=1)
down_frame.columnconfigure(0, weight=1)
down_frame.rowconfigure(1, weight=1)
root.mainloop()
