 
s = list(filter(None ,input("Введите данные  ").split()))
def add(some_list):
    print( float(some_list[1]) + float(some_list[2]))
def sub(some_list):
    print( float(some_list[1]) - float(some_list[2]))
    
def div(some_list):
    print( float(some_list[1]) / float(some_list[2]))
def incr(some_list):
    print( float(some_list[1]) * float(some_list[2]))
math_dict = {
    '+' : add,
    '-' : sub,
    '/' : div,
    '*' : incr
}
try:
    math_dict[s[0]](s)
except ZeroDivisionError :
    print("На ноль делить нельзя")
except KeyError:
    print('первым символом должен быть знак  отделеный пробелом -,+,/,*')    
except IndexError:
    print('Должно быть два числа и раздлены пробелом')     
except ValueError:
    print('Необходимо вводить цифры')      