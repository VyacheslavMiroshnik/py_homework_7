 
s = list(filter(None ,input("Введите данные  ").split()))
def add(some_list):
    print( float(some_list[1]) + float(some_list[2]))
def sub(some_list):
    print( float(some_list[1]) - float(some_list[2]))
    
def div(some_list):
    print( float(some_list[1]) / float(some_list[2]))
def incr(some_list):
    print( float(some_list[1]) * float(some_list[2]))
def neg_numbers(some_list):
    neg = False
    for value in some_list[1:]:
        if float(value) < 0 :
            neg = True
    if neg:
        print("Допупскаются только 2 положительных числа")        
    else:
        math_dict[s[0]](s)
           

math_dict = {
    '+' : add,
    '-' : sub,
    '/' : div,
    '*' : incr
}
assert(s[0] in math_dict),"Нет такой операции"

try:
    neg_numbers(s)
except ZeroDivisionError :
    print("На ноль делить нельзя")
except KeyError:
    print('первым символом должен быть знак  отделеный пробелом -,+,/,*')    
except IndexError:
    print('Должно быть два числа и раздлены пробелом')     
except ValueError:
    print('Необходимо вводить цифры')      