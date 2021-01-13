class flight():
    def __init__(self,inputname, inputcap):
        self.name = inputname
        self.cap = int(inputcap)
        self.passengers = []

    def add(self, fname):
        if self.cap != 0:
            self.passengers.append(fname)
            self.cap = self.cap - 1
            print('The passenger successfully added to the plane')
        else:
            print('There is no capacity in the plane')
# name = 'name'
# x352 = flight(352, 3)
# while True:
#     name = input('Enter the name of the passenger or type quit ')
#     if name == 'quit':
#         break
#     x352.add(name)
#
# print(f"The flight has {x352.cap} available seat")