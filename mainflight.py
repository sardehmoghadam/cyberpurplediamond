import flight
def main():
    flights = []
    while True:
        option = int(input(' Enter one number\n 1) Add flight \n 2) Add passenger\n 3) Show flights\n'
                           ' 4) search passenger\n 5) Quit\n'))
        if option == 1:
            flightname = input('Type the name of the flight ')
            flightcap = int(input('Enter the capacity of the flight '))
            flights.append(flight.flight(flightname, flightcap))
            print('Flight was successfully added')
        elif option == 2:
            flightname = input('Type the name of the flight ')
            pname = input('Type the name of the passeger ')
            for flight1 in flights:
                if flight1.name == flightname:
                    flight1.add(pname)
            else:
                print('Please enter the right flight number ')
        elif option == 3:
            for flight3 in flights:
                print(f"The flight name is {flight3.name} and the capacity is {flight3.cap}")
        elif option == 4:
            searchname = input('Type the name of the passenger ')
            exist = False
            for flight4 in flights:
                if searchname in flight4.passengers:
                    print(f"The flight name is {flight4.name}")
                    exist = True
            if exist == False:
                print('The passenger is not in the list')
        else:
            print('Have a good day')
            break
main()


