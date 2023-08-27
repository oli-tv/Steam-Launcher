# importing needed modules
import os
import customtkinter
from CTkMessagebox import CTkMessagebox

customtkinter.set_default_color_theme('green')

app = customtkinter.CTk()
app.title('Add Game')
app.geometry('280x280')
app.iconbitmap('icon.ico')
app.resizable(width=False, height=False)

frame = customtkinter.CTkFrame(master=app)
frame.pack(fill='both', expand=True)


title = customtkinter.CTkLabel(master=frame, text='Add Game', justify=customtkinter.CENTER, font=('Arial', 32))
title.pack(pady=10, padx=10)

# widgets for name
label_name = customtkinter.CTkLabel(master=frame, text='Game Name', justify=customtkinter.CENTER, font=('Arial', 18))
label_name.pack(pady=1, padx=10)
input_name = customtkinter.CTkTextbox(master=frame, width=200, height=30)
input_name.pack(pady=1, padx=10)

# widgets for ID
label_id = customtkinter.CTkLabel(master=frame, text='GameID', justify=customtkinter.CENTER, font=('Arial', 18))
label_id.pack(pady=1, padx=10)
input_id = customtkinter.CTkTextbox(master=frame, width=200, height=30)
input_id.pack(pady=1, padx=10)

# button function
def add():
    # input collecting
    GameName = input_name.get('0.0', 'end')
    GameName = GameName.strip()
    input_name.delete('0.0', 'end')
    GameID = input_id.get('0.0', 'end')
    GameID = GameID.strip()
    input_id.delete('0.0', 'end')

    # checking if one of variables is empty
    if GameName == "" or GameID == "":
        # showing error
        CTkMessagebox(title='Error', message='One of variables is empty', icon='warning', font=('Arial', 18))
    else:
        # creating directory
        os.mkdir(GameName)

        # copying code from def.txt to ini file
        codeFile = open('def.txt', 'r')
        iniFile = open(os.path.join(GameName, str(GameID)+'.ini'), 'w')
        iniFile.write(codeFile.read().format(GameID))
        codeFile.close()
        iniFile.close()
        CTkMessagebox(title='Operation completed', message='Game is added', icon='check', font=('Arial', 18))

# widget for button
add = customtkinter.CTkButton(master=frame, width=200, height=30, command=add, text='Add', font=('Arial', 15))
add.pack(pady=30, padx=10)

# showing entire GUI
app.mainloop()