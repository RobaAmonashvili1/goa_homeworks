print('დავალებაN1')
from turtle import *
width(7)
def კვადრატის_დახაზვა():
    for i in range(4):
        color('blue')
        forward(200)
        left(90)

კვადრატის_დახაზვა()


penup()
goto(200,200)
pendown()


def სახურავია_დახაზვა():
    color('red')
    left(135)
    forward(150)
    penup()
    goto(0,200)
    pendown()
    right(87)
    forward(145)
სახურავია_დახაზვა()

def კარების_დახაზვა():
    penup()
    goto(75,0)
    pendown()
    left(43)
    forward(75)
    right(90)
    forward(50)
    right(90)
    forward(75)

კარების_დახაზვა()
exitonclick()



print('დავალებაN2')
გვერდი1 = int(input("კვადრატის პირველი გვერდი : "))
გვერდი2 = int(input("კვადრატის მეორე გვერდი: "))
კვადრატის_პერიმეტრი = ((გვერდი1 + გვერდი2) * 2)
print(კვადრატის_პერიმეტრი)



print('დავალებN3')
გვერდი1 = int(input("პირველი გვერდის სიგრძე: "))
გვერდი2 = int(input("მეორე გვერდის სიგრძე: "))
გვერდი3 = int(input("მესამე გვერდდდის სიგრძე: "))
პერიმეტრი = (გვერდი1 + გვერდი2 + გვერდი3)
print(პერიმეტრი)