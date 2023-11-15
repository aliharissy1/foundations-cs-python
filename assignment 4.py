cities = ["Beirut", "Hazmieh", "Baabda", "Aley", "Antellias", "Jounieh", "Byblos", "Khalde", "Saida", "Nabatieh"]

transport = {
    "Ahmad": [],
    "Hussein": [],
    "Ashraf": [],
}


def addCity(city):
    cities.append(city)

def addDriver(driver):
    transport.update({driver: []})

def addRoute(driver, city, index):
    if index == 0:
        transport[driver].insert(0, city)
    elif index == -1:
        transport[driver].append(city)
    else:
        transport[driver].insert(index, city)

def removeCity(driver, city):
    transport[driver].remove(city)

def deliverability(city):
    available_drivers = []
    for key, value in transport.items():
        if city in value:
            available_drivers.append(key)
    return available_drivers

def mainMenu():
    while True:
        print("1. add a city\n2. add a driver \n3. add a city to the route of a driver \n4. Remove a city from a driver’s route \n5. check the deliverability of a package\n6. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Please enter a number between 1 and 6:")
            continue

        while choice < 0 or choice > 6:
            try:
                choice = int(input("Please enter a number between 1 and 6: "))
            except:
                print("Please enter a number between 1 and 6:")

        if choice == 1:
            try:
                newCity = input("Enter the name of the city you want to add: ").capitalize()
                while newCity in (cities):
                    print(newCity,"already exists in this list")
                    newCity = input("Enter the name of non-existing city you want to add: ").capitalize()
                addCity(newCity)
                print(cities)
            except:
                print("An error occurred")

        elif choice == 2:
            try:
                newDriver = input("Enter the name of the driver you want to add: ").capitalize()
                addDriver(newDriver)
                print(transport)
            except:
                print("An error occurred")

        elif choice == 3:
            try:
                driver = input("Enter the name of the driver: ").capitalize()
                while driver not in transport:
                    driver = input("Enter the name of an available driver: ").capitalize()
                city = input("Enter the name of the city: ").capitalize()
                while city not in cities:
                    city = input("Enter the name of an available city: ").capitalize()
                index = int(input("Enter the index of the city: "))
                for key, value in transport.items():
                    if key == driver:
                        if city in value:
                            print(driver, "already has this city in his route")
                        else:
                            addRoute(driver, city, index)
                print(transport)
            except:
                print("An error occurred")

        elif choice == 4:
            try:
                driver = input("Enter the name of the driver: ").capitalize()
                while driver not in transport:
                    driver = input("Enter the name of an available driver: ").capitalize()
                city = input("Enter the name of the city: ").capitalize()
                while city not in cities:
                    city = input("Enter the name of an available city: ").capitalize()
                for key, value in transport.items():
                    if key == driver:
                        if city not in value:
                            print(driver, "doesn't have this city in his route")
                        else:
                            removeCity(driver, city)
                print(transport)
            except:
                print("An error occurred")

        elif choice == 5:
            try:
                city = input("Enter the name of the city: ").capitalize()
                while city not in cities:
                    city = input("Enter the name of an available city: ").capitalize()
                driver_list = deliverability(city)
                print(driver_list)
            except:
                print("An error occurred")

        elif choice == 6:
            break

mainMenu()
