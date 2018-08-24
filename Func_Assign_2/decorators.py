from datetime import datetime

def not_during_the_night(func):
    def wrapper(*args):
        if 7 <= datetime.now().hour < 10:
            func(*args)
        elif 10<= datetime.now().hour<19:
            print('work')
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

@not_during_the_night
def say_whee(name):

    print("Whee!" + name)


say_whee('Morning')