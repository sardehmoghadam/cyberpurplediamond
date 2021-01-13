import random
class guess:
    x = random.randint(1, 100)
    # def __int__(self):
    #     self.x = random.randint(1, 100)
    #     return self.x
    # def __init__(self):
    #     self.x = random.randint(1, 100)

    def guess():
        while True:
            y = int(input('Enter a number '))
            if x > y:
                print('The expected number is bigger')
            elif x < y:
                print('The expected number is smaller')
            else:
                print('The number you entered is True')
                break


