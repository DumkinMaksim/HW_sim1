# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


print('Enter day is number->',end=" ")
innumber=int(input())

if 0<innumber<7 :
    if innumber<6 :
        print ('work day(YES)')
    if innumber>=6 :
        print (' not work day(NO)')
else :
    print('Error incorrect input,try again')