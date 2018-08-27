from tkinter import *
import random
import math

#Screen Resolution Variables
Screen_X = 600
Screen_Y = 600

#Generates Map
def Gen_Map():
    #Takes data from Entry boxes
    ro = int(rows.get())
    co = int(cols.get())
    md = int(m_d.get())

    #Error checks for invalid Entries
    if(ro <= 1) or (co <= 1):
        print("The Grid must contain at least 2 rows and 2 columns.")

    elif(md > math.sqrt(ro**2 + co**2)):
        print("Minimum Distance exceeds maximum grid size. Try lowering the minimum distance.")

    #Found valid Entries
    else:
        for j in range(0, ro):
            for i in range(0,co):
                canvas.create_rectangle(j * Screen_X / ro, i * Screen_Y / co, Screen_X / ro + j * Screen_X / ro, Screen_Y / co + i * Screen_Y / co, fill='#fff')

        goal_x = random.randint(0, ro-1)
        goal_y = random.randint(0, co-1)

        sp_x = random.randint(0, ro-1)
        sp_y = random.randint(0, co-1)

        #ensures distance is greater than or equal to the min dist
        while(math.sqrt((goal_x - sp_x)**2 + (goal_y - sp_y)**2) <= md):
            goal_x = random.randint(0,ro-1)
            goal_y = random.randint(0,co-1)

            sp_x = random.randint(0,ro-1)
            sp_y = random.randint(0,co-1)

        canvas.create_oval(sp_x * Screen_X / ro, sp_y * Screen_Y / co, Screen_X / ro + sp_x * Screen_X / ro, Screen_Y / co + sp_y * Screen_Y / co, fill='green2')
        canvas.create_oval(goal_x * Screen_X / ro, goal_y * Screen_Y / co, Screen_X / ro + goal_x * Screen_X / ro,
                           Screen_Y / co + goal_y * Screen_Y / co, fill='red2')

        print("The Starting Position is: " + str(sp_x) + ", " + str(sp_y))
        print("The Goal is: " + str(goal_x) + ", " + str(goal_y))
        print("The Distance is: " + str(int(math.sqrt((goal_x - sp_x)**2 + (goal_y - sp_y)**2))))


root = Tk()

#Buttons Frame
topFrame = Frame(root)
topFrame.pack()

#Create Map
Button_Map = Button(topFrame, text="Generate Map", command=Gen_Map)
label1 = Label(topFrame, text="Rows:")
label2 = Label(topFrame, text="Columns:")
label3 = Label(topFrame, text="Minimum Distance: ")
rows = Entry(topFrame)
cols = Entry(topFrame)
m_d = Entry(topFrame)

Button_Map.grid(row=0)
label1.grid(row=0, column=1)
rows.grid(row=0, column=2)
label2.grid(row=0, column=3)
cols.grid(row=0, column=4)
label3.grid(row=0, column=5)
m_d.grid(row=0, column=6)

#Create Ant
Button_Ant = Button(topFrame, text="Create Ant")
Button_Ant.grid(row=1, column=0)

#Canvas Frame
cFrame = Frame(root)
cFrame.pack()

canvas = Canvas(cFrame, width=Screen_X, height=Screen_Y)
canvas.pack()

root.mainloop()