from turtle import*
#მონაცემები
width (7)
speed (50)



#კვარდატი
color ("orange") 
forward (200) 
left (90)
forward (200)
left (90)
forward (200)
left (90)
forward (200)
left (90)

#კარი
forward (75)
color ("brown")
left (90)
forward (75)
right (90)
forward (50)
right (90)
forward (75)

#სახურავი
penup ()
goto (200, 200)
pendown()

color ("brown")
begin_fill()
right (150)
forward (200)
left (120)
forward (200)
end_fill()

#მარცხენაფანჯარა
penup ()
goto (30, 100)
pendown ()
color ("cyan")
begin_fill
left (30)
left (180)
forward (40)
right (90)

forward (40)
right (90)

forward (40)
right (90)

#მარცხენაფანჯრისჩარჩო
forward (40)
width (3)
right (90)
forward (20)
right (90)
forward (40)
left (90)
forward (20)
left (90)
forward (20)
left (90)
forward (40)

#მარჯვენა ფანჯარა
penup ()
goto (170,100)
pendown ()
width (7)
right (90)
forward (40)
right (90)
forward (40)
right (90)
forward (40)
right (90)
forward (40)

#მარჯვენაფანჯრისჩარჩო

width (3)
right (90)
forward (20)
right(90)
forward (40)
right (90)
forward (20)
right(90)
forward (20)
right(90)
forward (40)


exitonclick()
