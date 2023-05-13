def do_something(x):
    answer = 0
    array = [x, x ** 0, x // x , x % (x - 4), [x]]
    for i in range(x):
        answer += array[i]
    return answer

try:
    x = int(input())
except ValueError:
    print("Invalid input. Please enter an integer value.")
else:
    try:
        do_something(x)
    except ZeroDivisionError:
        print("bro divide number by zero 💀")
    except ValueError:
        print("Do you think that letter can be integer....")
    except IndexError:
        print("Hey, that's out of range")
    except TypeError:
        print('Invalid arguments type')
    else :
        print(f'answer is {do_something(x)}')