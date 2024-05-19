from tkinter import *
import time

wd =1000
hi =40

wd_e_1 =70
hi_e_1 =500

xmove = 1   
ymove = 1
xmove_ammo =-1


def move_left(event):
    main_charcter.place(x=main_charcter.winfo_x()+20,y=main_charcter.winfo_y())
def move_right(event):
    main_charcter.place(x=main_charcter.winfo_x()-20,y=main_charcter.winfo_y())
    if main_charcter.winfo_x()<= 0:
        return main_charcter.place(x=main_charcter.winfo_x()==0,y=main_charcter.winfo_y())
def jump(event):
    main_charcter.place(x=main_charcter.winfo_x(),y=main_charcter.winfo_y()-80)
    window.after(350,down)
def down():
  
         main_charcter.place(x=main_charcter.winfo_x(), y=main_charcter.winfo_y() + 80)
         window.after(1)




window = Tk()
window.geometry("1000x1000")
window.config(bg="blue")

enemy0 =Canvas(width=wd,height=hi,bg="blue",bd=-2)
enemy0.place(x=40,y=560)
enemy0_chap = enemy0.create_oval(10,15,40,40,fill="red")
   
enemy1 = Canvas(height=hi_e_1,width=wd_e_1,bg="blue",bd=-2)
enemy1.place(x=910,y=500)
enemy1_rectangle = enemy1.create_rectangle(200,140,10,20,fill="red")
ammu_photo_left = PhotoImage(file="ammo_left (1).png")
ammu_photo_right = PhotoImage(file="ammo_right (1).png")
police_man_ammo = Canvas(height=15,width=1250,bd=-3,bg="blue")
police_man_ammo_image = police_man_ammo.create_image(1220,0,image=ammu_photo_left,anchor=NW)
police_man_ammo.place(x=0,y=170)
police_man_photo=PhotoImage(file="noun-sniper-245279 (1).png")
police_man = Label(width=35,height=60,bg="blue",image=police_man_photo,bd=-2)
police_man.place(x=1260,y=180)
police_man_1_photo=PhotoImage(file="police_man_1 (1).png")
police_man_1 = Label(width=35,height=60,bg="blue",image=police_man_1_photo,bd=-2)
police_man_1.place(x=20,y=180)

police_man_1_ammo = Label(window,width=30,height=2,bg="blue",image=ammu_photo_right)
police_man_1_ammo.place(x=20,y=180)

shield_man_1_photo=PhotoImage(file="shield_l.png")
shield_man_1 = Label(window,width=35,height=60,bg="blue",image=shield_man_1_photo)
shield_man_1.place(x=120,y=180)
shield_heal_1 = 0
shield_heal = 0
shield_man_photo=PhotoImage(file="shield_r.png")
shield_man = Label(width=35,height=60,bg="blue",image=shield_man_photo,bd=-2)
shield_man.place(x=1160,y=180)

def en0_animation():
    global xmove,ymove
    enemy0.move(enemy0_chap,xmove,0)
    x1 , y1 , x2 , y2 = enemy0.coords(enemy0_chap)
    if x1>=600 or x2<=3:
        xmove *=-1
    if y2 >=500 or y1 <=0:
        ymove *= -1
    window.after(9,en0_animation)
en0_animation()


window.bind("<d>",move_left)
window.bind("<a>",move_right)
window.bind("<space>",jump)

ammu = Label(height=15,width=50,bd=-3,bg="blue",image=ammu_photo_right) 
ammu.place(x=-1000,y=-1000)
ammu_l = Label(height=15,width=50,bd=-3,bg="blue",image=ammu_photo_left) 
ammu_l.place(x=-1000,y=-1000)
teleporte_gate_photo= PhotoImage(file='Super-herói_png-removebg-preview.png')
main_charcter_photo= PhotoImage(file='output-onlinepngtools.png')
ground_1and1_5_photo= PhotoImage(file='pngwing.com (1).png')
teleporte_gate = Label(window,width=100,height=100,bg="blue",image=teleporte_gate_photo)
teleporte_gate.place(x=1300,y=520)
main_charcter=Label(window,height=100,width=30,image=main_charcter_photo,bg="blue")
main_charcter.place(x=10,y=520)
main_charcter_heal = 100


ground_0 = Label(window,bg="green",height=10,width=300)
ground_1 = Label(window,bg="blue",image=ground_1and1_5_photo,height=150,width=700)
ground_1_5 = Label(window,bg="blue",image=ground_1and1_5_photo,height=150,width=700)
ground_1_5.place(x=700,y=250)
ground_1.place(x=0,y=250)
ground_0.place(x=0,y=600)
end_bg = Label(window,width=1000,height=1000,bg="red",text="fuckkkk_youuu")
end_bg.place(x=-10000,y=-10000)
def animation_ammo_l_police():
    global main_charcter_heal , xmove_ammo
    x1, y1 = police_man_ammo.coords(police_man_ammo_image)
    if main_charcter.winfo_y() <=170 :
        police_man_ammo.move(police_man_ammo_image, xmove_ammo, 0)
    if (main_charcter.winfo_x() == x1 ) and (main_charcter.winfo_y() == police_man_ammo.winfo_y()):
        main_charcter_heal = main_charcter_heal-20
        police_man_ammo.move(police_man_ammo_image, 1220 - x1, y1) 
    if  0 >= main_charcter_heal :
        main_charcter.place(x=10,y=520)
        main_charcter_heal =main_charcter_heal+100
    if (x1 < -10) and (x1 > -50):
        police_man_ammo.move(police_man_ammo_image, 1220 - x1, y1) 
    if (police_man.winfo_x() == -900) and  (police_man.winfo_y() == -200):
        police_man_ammo.place(x=-10000000000,y=-9000)
        
    window.after(3, animation_ammo_l_police)

animation_ammo_l_police()

def animation_ammo_r_police():
    global main_charcter_heal
    x1, y1 = police_man_ammo.coords(police_man_ammo_image)
    if main_charcter.winfo_y() <= 170:
        police_man_1_ammo.place(x=police_man_1_ammo.winfo_x()+10,y=180)
    if police_man_1_ammo.winfo_x() > 1400:
        police_man_1_ammo.place(x=20,y=180)
    if (police_man_1_ammo.winfo_x()== main_charcter.winfo_x()) and (police_man_1_ammo.winfo_y()== main_charcter.winfo_y()+10):
        main_charcter_heal = main_charcter_heal -20
        police_man_1_ammo.place(x=20,y=180)
    if main_charcter_heal ==0:
        main_charcter.place(x=0,y=520)
        police_man_1_ammo.place(x=20,y=180)
        police_man_ammo.move(police_man_ammo_image, 1220 - x1, y1) 
    window.after(30,animation_ammo_r_police)
animation_ammo_r_police()

def lol():
    if main_charcter.winfo_y()==ground_0.winfo_y():
        return main_charcter.winfo_y()==520
def damge():
    x1 , y1 , x2 , y2 = enemy0.coords(enemy0_chap)
    main_x1, main_y1, main_x2, main_y2 = main_charcter.winfo_x(), main_charcter.winfo_y(), main_charcter.winfo_x() + main_charcter.winfo_reqwidth(), main_charcter.winfo_y() + main_charcter.winfo_reqheight()

    if (main_x1 < x2 and main_x2-33 > x1) and (main_charcter.winfo_y() == 520):
        main_charcter.place(x=10, y=520)
        
    window.after(1, damge)

damge()

def en1_animation():
    global xmove, ymove
    enemy1.move(enemy1_rectangle,0,ymove)
    x1,y1,x2,y2 = enemy1.coords(enemy1_rectangle)
    if x2 >= 400 or x1 <= 3:
        xmove *= -1
    if y2 >= 300 or y1 <=0:
        ymove *= -1
    window.after(7,en1_animation)
en1_animation()


def damge_e1():
    global main_charcter_heal
    x1, y1, x2, y2 = enemy1.coords(enemy1_rectangle)
    main_x1, main_y1, main_x2, main_y2 = main_charcter.winfo_x(), main_charcter.winfo_y(), main_charcter.winfo_x() + main_charcter.winfo_reqwidth(), main_charcter.winfo_y() + main_charcter.winfo_reqheight()

    # Adjust coordinates to the window coordinate system
    enemy1_x1, enemy1_y1 = enemy1.winfo_x() + x1, enemy1.winfo_y() + y1
    enemy1_x2, enemy1_y2 = enemy1.winfo_x() + x2, enemy1.winfo_y() + y2

    # Check for x-coordinate overlap and y-coordinate overlap
    if (main_x2 >= enemy1_x1 and main_x1 <= enemy1_x2) and (main_y2 >= enemy1_y1 and main_y1 <= enemy1_y2):
        main_charcter.place(x=10, y=520)
    window.after(100, damge_e1)

damge_e1()

def teleporte():
    if main_charcter.winfo_x()  >= 1300:
        main_charcter.place(x=700,y=170)
    window.after(1,teleporte)
teleporte()

def right(event):
    ammu.place(x=main_charcter.winfo_x()+20,y=main_charcter.winfo_y()+10)
    window.after(100,animation_ammo_R_and_damge)
def animation_ammo_R_and_damge():
    global shield_heal
    ammu.place(x=ammu.winfo_x()+10,y=ammu.winfo_y())
    if (ammu.winfo_x() == police_man.winfo_x()) and (ammu.winfo_y() == police_man.winfo_y()):
        police_man.place(x=-900,y=-200)
        ammu.place(x=-900,y=-700)
    if (ammu.winfo_x() == shield_man.winfo_x()) and (ammu.winfo_y() == shield_man.winfo_y()):
        shield_heal = shield_heal+1
        ammu.place(x=-900,y=-700)
    if shield_heal == 4:
        shield_man.place(x=-900,y=-200)
    window.after(30,animation_ammo_R_and_damge) 
def left(event):
    ammu_l.place(x=main_charcter.winfo_x()-20,y=main_charcter.winfo_y()+10)
    window.after(100,animation_ammo_l_and_damge)
def animation_ammo_l_and_damge():
    global shield_heal_1
    ammu_l.place(x=ammu_l.winfo_x()-20,y=ammu_l.winfo_y())
    if (ammu_l.winfo_x() == police_man_1.winfo_x()) and (ammu_l.winfo_y()==police_man_1.winfo_y()):
        police_man_1.place(x=-9000,y=-100000)
        police_man_1_ammo.place(x=-10000,y=-100000)
    if (ammu_l.winfo_x() == shield_man_1.winfo_x()) and (ammu_l.winfo_y() == shield_man_1.winfo_y()):
        shield_heal_1 = shield_heal_1+1
        ammu_l.place(x=-900000,y=-102787)
    if shield_heal_1 == 4:
        shield_man_1.place(x=-10000000,y=-34324)
    window.after(30,animation_ammo_l_and_damge)
def heal_character_bar():
    global main_charcter_heal
    main_charcter_heal_bar = Label(window,width=30,height=2,text=(main_charcter_heal,"HP"),bg="white",bd=-4)
    main_charcter_heal_bar.place(x=0,y=710)
    if (main_charcter_heal <90) and (main_charcter_heal>69):
         main_charcter_heal_bar.config(bg="orange")
    if (main_charcter_heal <70) and (main_charcter_heal>59):
         main_charcter_heal_bar.config(bg="brown")
    if (main_charcter_heal <50) and (main_charcter_heal>10):
         main_charcter_heal_bar.config(bg="red")
         main_charcter_heal_bar.config(text=(main_charcter_heal,"HP","  warning"))
    if (police_man.winfo_y() == -200) and (police_man_1.winfo_y() == -100000):
        print("hi")
        end_bg.place(x=0,y=0)
    window.after(100,heal_character_bar)
heal_character_bar()
window.bind("<l>",right)
window.bind("<j>",left)
window.mainloop()