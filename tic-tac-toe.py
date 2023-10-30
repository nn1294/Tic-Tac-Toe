from tkinter import *

root = Tk()  # Initialize the main window
root.iconbitmap('tic tac toe.ico')  # Set the window icon
root.title('Tic-Tac-Toe')  # Set the window title
root.resizable(False, False)  # Make the window non-resizable

# Variables to keep track of game state
click = True  # Boolean variable to toggle between X and O
count = 0  # Counter to track the number of moves

# Variables for each button in the game grid
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

xPhoto = PhotoImage(file='cross.png')  # Load X image
oPhoto = PhotoImage(file='happy.png')  # Load O image

# Function to create the game grid (buttons)
def start():
    # Create and place buttons for the Tic-Tac-Toe grid
    button1 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#ccfff7', textvariable=btn1)
    button1.grid(row=0, column=0)

    button2 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#ccfff7', textvariable=btn2)
    button2.grid(row=0, column=1)

    button3 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#ccfff7', textvariable=btn3)
    button3.grid(row=0, column=2)

    button4 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#99ffee', textvariable=btn4)
    button4.grid(row=1, column=0)

    button5 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#99ffee', textvariable=btn5)
    button5.grid(row=1, column=1)

    button6 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#99ffee', textvariable=btn6)
    button6.grid(row=1, column=2)

    button7 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#66ffe6', textvariable=btn7)
    button7.grid(row=2, column=0)

    button8 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#66ffe6', textvariable=btn8)
    button8.grid(row=2, column=1)

    button9 = Button(root, height=9, width=19, bd=.5, relief='sunken', bg='#66ffe6', textvariable=btn9)
    button9.grid(row=2, column=2)

start()  # Call the function to create the grid

root.mainloop()  # Start the main event loop for the application
