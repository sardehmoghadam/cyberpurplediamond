import random
class guess:
    def __init__(self, x):
        self.x = random.randint(1, 100)

    def guess(x):
        while True:
            y = int(input('Enter a number '))
            if x > y:
                print('The expected number is bigger')
            elif x < y:
                print('The expected number is smaller')
            else:
                print('The number you entered is True')
                break


