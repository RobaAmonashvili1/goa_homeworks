print('დავანება N1')
age = int(input('რამდენი წლის ხარ :'))
num = 0 
while age > num: 
    print('გილოცავ შენ გახდი' + ' ' + str(num) + ' ' + 'წლის')
    num = num + 1
    while num == 8:
         print('გილოცავ შენ  გახდი' + ' ' +  str(num) + ' ' + 'წლის'  + ' ' + 'და შემოუერთდი GOA-ს')
         num = num + 1




print('დავალება N2')
for i in range(1,101,2):
    print(i)
