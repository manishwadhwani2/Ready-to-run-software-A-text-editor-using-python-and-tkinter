
"""

@author: manishwad
"""

import  tkinter as tk
from tkinter import ttk
from  tkinter import font
from  tkinter import colorchooser
from  tkinter import filedialog
from  tkinter import messagebox
import os
main_application  = tk.Tk()#constructor call
main_application.geometry('1200x800')#setting the geometry of the application
main_application.title('Cross Platform Text editor')#Addition of the title 
main_application.wm_iconbitmap('icon.ico')
######################################## main menu################################################################
#---------------------------------------End main menu-------------------------------------------------------------
main_menu  = tk.Menu()
#File 
File  = tk.Menu(main_menu,tearoff = False)
#File icons
new_icon = tk.PhotoImage(file ='icons2/new.png')
open_icon = tk.PhotoImage(file ='icons2/open.png')
save_icon = tk.PhotoImage(file ='icons2/save.png')
save_as_icon = tk.PhotoImage(file ='icons2/save_as.png')
exit_icon = tk.PhotoImage(file ='icons2/exit.png')
#Edit
Edit  = tk.Menu(main_menu,tearoff = False)
#Edit icons
copy_icon = tk.PhotoImage(file ='icons2/copy.png')
paste_icon = tk.PhotoImage(file ='icons2/paste.png')
cut_icon = tk.PhotoImage(file ='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file ='icons2/clear_all.png')
find_icon = tk.PhotoImage(file ='icons2/find.png')
#View
View  = tk.Menu(main_menu,tearoff = False)
#View icons
tool_bar_icon = tk.PhotoImage(file ='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file ='icons2/status_bar.png')

#Colortheme                    
ColorTheme  = tk.Menu(main_menu,tearoff = False)
#Color icons
light_default_icons = tk.PhotoImage(file ="icons2/Light_default.png")
dark_icons = tk.PhotoImage(file = "icons2/dark.png")
theme_choice =tk.StringVar() #Variable used to collect info about which theme user has choose to deploy
color_icons = (light_default_icons,dark_icons)
color_dict = {"Light Default Color":("#000000","#ffffff"),"Dark":("#c4c4c4","#2d2d2d")}

                                
 
#Cascading every thing
main_menu.add_cascade(label = "File",menu = File)
main_menu.add_cascade(label = "Edit",menu = Edit)
main_menu.add_cascade(label = "View",menu = View)
main_menu.add_cascade(label = "ColorTheme",menu = ColorTheme)


######################################## toolbar################################################################
tool_bar= ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill = tk.X)
##font_box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable =font_family,state = "readonly" )
font_box['values']=font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column =0,padx = 5)
#size_box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width = 14,textvariable = size_var,state ='readonly')
font_size['values'] =tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)
## Bold Button
bold_icon = tk.PhotoImage(file ='icons2/bold.png')
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx = 5)
## Italic Button 
italic_icon = tk.PhotoImage(file = 'icons2/italic.png')
italic_btn= ttk.Button(tool_bar,image = italic_icon)
italic_btn.grid(row=0,column=3,padx =5)
## underline Button
underline_icon = tk.PhotoImage(file = 'icons2/underline.png')
underline_btn = ttk.Button(tool_bar,image = underline_icon)
underline_btn.grid(row =0,column=4,padx = 5)
# font color button
font_color_icon = tk.PhotoImage(file = 'icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar,image = font_color_icon)
font_color_btn.grid(row=0,column=5,padx = 5)
# align left
align_left_icon = tk.PhotoImage(file  = "icons2/align_left.png")
align_left_btn = ttk.Button(tool_bar,image = align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)
#align right
align_right_icon  = tk.PhotoImage(file = "icons2/align_right.png")
align_right_btn = ttk.Button(tool_bar,image = align_right_icon)
align_right_btn.grid(row=0,column=8,padx = 5)
#align center
align_center_icon  = tk.PhotoImage(file = "icons2/align_center.png")
align_center_btn = ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx = 5)

#---------------------------------------End toolbar-------------------------------------------------------------
######################################## text editor################################################################

text_editor = tk.Text(main_application)
text_editor.config(wrap = "word",relief = tk.FLAT)
scroll_bar = tk.Scrollbar(main_application)

text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill =tk.BOTH,expand =True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
#font size and font functionality
current_font_family = "Arial"
current_font_size =12
current_bold = "normal"
current_italic = "roman"
def change_font(event = None):
    global current_font_family
    current_font_family =font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))
def change_fontSize(event = None):
    global current_font_size
    current_font_size =size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))
font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_fontSize)

#Button Funtionality
#BOLD Funtionality
def change_bold():
    text_property = tk.font.Font(font =text_editor['font'])
    global current_bold
    if text_property.actual()["weight"] == "normal":
        current_bold = "bold"
    elif text_property.actual()["weight"] == "bold":
        current_bold = "normal"
    text_editor.configure(font = (current_font_family,current_font_size,current_bold,current_italic))

bold_btn.configure(command = change_bold)
#Italic Funtionality
def change_Italic():
    text_property = tk.font.Font(font =text_editor['font'])
    global current_italic
    if text_property.actual()["slant"] == "roman":
         current_italic = "italic"

    elif text_property.actual()["slant"] =="italic" :
        current_italic = "roman"
        
    text_editor.configure(font = (current_font_family,current_font_size,current_bold,current_italic))

italic_btn.configure(command = change_Italic)
#Underline Funtionality
def change_Underline():
    text_property = tk.font.Font(font =text_editor['font'])
    if text_property.actual()["underline"] == 0:
       text_editor.configure(font = (current_font_family,current_font_size,"underline"))
    elif text_property.actual()["underline"] == 1:
        text_editor.configure(font = (current_font_family,current_font_size,"normal"))

underline_btn.configure(command = change_Underline)
#font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg = color_var[1])
font_color_btn.configure(command = change_font_color)
### align Functionality
def  align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_btn.configure(command = align_left)
def  align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
align_center_btn.configure(command = align_center)
def  align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
align_right_btn.configure(command = align_right)

text_editor.config(font=("Arial",12))
#---------------------------------------End text editor-------------------------------------------------------------

######################################## status bar################################################################
status_bar = ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)
text_changed = False
def changed(event=None):
    if text_editor.edit_modified():
        global text_changed
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text =f'Characters : {characters},Words:{words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)
    

#---------------------------------------End status bar-------------------------------------------------------------
######################################## main menu functionality################################################################
#new button funtionality
url = ""
def new_file(event = None):
    global url 
    url = ""
    text_editor.delete(1.0,tk.END)




#File Command
File.add_command(label = "New",image = new_icon,compound  = tk.LEFT,accelerator ="CTRL+N",command = new_file)
#open functionality
def open_file(event = None):
    global url
    url =filedialog.askopenfilename(initialdir =os.getcwd(),title = "Select File",filetypes = (("Text files","*.txt"),("All Files","*.*")))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return 
    main_application.title(os.path.basename(url))

    
File.add_command(label = "Open",image = open_icon,compound  = tk.LEFT,accelerator ="CTRL+O",command = open_file)
# save functionality
def save_file(event = None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,"w",encoding="utf-8") as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = "w",defaultextension='.txt',filetypes = (("Text files","*.txt"),("All Files","*.*")))
            content2 = str(text_editor.get(1.0,tk.END))
            url.write(content2)
            url.close()
    except:
        return
     
        
File.add_command(label = "Save",image = save_icon,compound  = tk.LEFT,accelerator ="CTRL+S",command = save_file)
# save as functionality 
def save_As_file(event = None):
    global url
    try:
        content = str(text_editor.get(1.0,tk.END))
        url = filedialog.asksaveasfile(mode = "w",defaultextension='.txt',filetypes = (("Text files","*.txt"),("All Files","*.*")))
        url.write(content)
        url.close()
    except:
        return
    
File.add_command(label = "Save_as",image = save_as_icon,compound  = tk.LEFT,accelerator ="CTRL+Alt+S",command = save_As_file)
# exit functionality
def exit_func(event =None):
    global url,text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel("Warning","Do you want to save the file ?")
            if mbox is True:
                if url:
                    content = str(text_editor.get(1.0,tk.END))
                    with open(url,'w',encoding  = "utf-8") as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    filedialog.asksaveasfile(mode = "w",defaultextension='.txt',filetypes = (("Text files","*.txt"),("All Files","*.*")))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

File.add_command(label = "Exit",image = exit_icon,compound  = tk.LEFT,accelerator ="CTRL+Q",command = exit_func)

#Edit Command
# Find and replace  functionality
def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word ,start_pos,stopindex = tk.END)
                if not start_pos:
                    break;
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background = 'yellow')
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title("Find")
    find_dialogue.resizable(0,0)
    #frame
    find_frame = ttk.LabelFrame(find_dialogue,text = "Find/Replace")
    find_frame.pack(pady=20)
    ##labels
    text_find_label = ttk.Label(find_frame,text="Find : ")
    text_replace_label = ttk.Label(find_frame,text = "Replace")
    #entry
    find_input = ttk.Entry(find_frame,width = 30)
    replace_input = ttk.Entry(find_frame,width = 30)
    #button
    find_button = ttk.Button(find_frame,text = 'Find',command = find)
    replace_button = ttk.Button(find_frame,text = "Replace",command = replace)
    #label grid
    text_find_label.grid(row=0,column =0,padx =4,pady = 4)
    text_replace_label.grid(row=1,column=0,padx = 4,pady=4)
    #entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    #button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)
    find_dialogue.mainloop()
    
    
                
                
                
        
Edit.add_command(label = "Copy",image = copy_icon,compound = tk.LEFT,accelerator = "CTRL+C",command = lambda:text_editor.event_generate("<Control c>"))
Edit.add_command(label = "Paste",image = paste_icon,compound = tk.LEFT,accelerator = "CTRL+V",command = lambda:text_editor.event_generate("<Control v>"))
Edit.add_command(label = "Cut",image = cut_icon,compound = tk.LEFT,accelerator = "CTRL+X",command = lambda:text_editor.event_generate("<Control x>"))
Edit.add_command(label = "Clear_All",image = clear_all_icon,compound = tk.LEFT,accelerator = "CTRL+ALT+X",command = lambda:text_editor.delete(1.0,tk.END))
Edit.add_command(label = "Find",image = find_icon,compound = tk.LEFT,accelerator = "CTRL+F",command = find_func)
#View Checkbutton
# hide funtionality
show_statusbar =tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP,fill = tk.X)
        text_editor.pack(fill = tk.BOTH,expand =True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True
        
View.add_checkbutton(label = "Tool Bar",onvalue=True,offvalue=0,variable = show_toolbar,image = tool_bar_icon,compound = tk.LEFT,command = hide_toolbar)#adding checkbutton so that I can reemove or display the toolbar
View.add_checkbutton(label = "Status Bar",onvalue = 1,offvalue =False,variable = show_statusbar,image = status_bar_icon,compound = tk.LEFT,command = hide_statusbar)#Adding Checkbutton so that I can remove or display the statusbar
#colortheme functionality
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color,bg_color =  color_tuple[0],color_tuple[1]
    text_editor.config(background = bg_color,fg = fg_color)
    
    
#Colortheme radiobutton
count  =0
for i in color_dict:
    ColorTheme.add_radiobutton(label = i,image = color_icons[count],variable = theme_choice,compound = tk.LEFT,command = change_theme) 
    count+=1








#---------------------------------------End main menu functionality-------------------------------------------------------------
main_application.config(menu = main_menu)
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_As_file)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_func)
main_application.protocol('WM_DELETE_WINDOW',exit_func)
main_application.mainloop()