import check50

@check50.check()
def exists1():
    """Automobile.java exists"""
    check50.exists("Automobile.java")

@check50.check()
def exists2():
    """Aircraft.java exists"""
    check50.exists("Aircraft.java")

@check50.check()
def exists3():
    """Car.java exists"""
    check50.exists("Car.java")

@check50.check()
def exists4():
    """Truck.java exists"""
    check50.exists("Truck.java")

@check50.check()
def exists5():
    """Airplane.java exists"""
    check50.exists("Airplane.java")

@check50.check()
def exists6():
    """Helicopter.java exists"""
    check50.exists("Helicopter.java")

@check50.check(exists1)
def automobile_compiles():
    """Automobile.java compiles"""
    check50.run("javac Automobile.java").exit(0)

@check50.check(exists2)
def aircraft_compiles():
    """Aircraft.java compiles"""
    check50.run("javac Aircraft.java").exit(0)

@check50.check(exists3)
def car_compiles():
    """Car.java compiles"""
    check50.run("javac Car.java").exit(0)

@check50.check(exists4)
def truck_compiles():
    """Truck.java compiles"""
    check50.run("javac Truck.java").exit(0)

@check50.check(exists5)
def airplane_compiles():
    """Airplane.java compiles"""
    check50.run("javac Airplane.java").exit(0)

@check50.check(exists6)
def helicopter_compiles():
    """Helicopter.java compiles"""
    check50.run("javac Helicopter.java").exit(0)

@check50.check(exists1)
def automobile_implements_vehicle():
    """Automobile implements Vehicle"""
    f = open("Automobile.java", "r")
    contents = f.read()
    if contents.find("class Automobile implements Vehicle") == -1:
        raise check50.Failure("Automobile must implement Vehicle")

