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

@check50.check(exists1)
def automobile_is_abstract():
    """Automobile is abstract"""
    f = open("Automobile.java", "r")
    contents = f.read()
    if contents.find("public abstract class Automobile") == -1:
        raise check50.Failure("Automobile must be abstract")

@check50.check(exists2)
def aircraft_implements_vehicle():
    """Aircraft implements Vehicle"""
    f = open("Aircraft.java", "r")
    contents = f.read()
    if contents.find("class Aircraft implements Vehicle") == -1:
        raise check50.Failure("Aircraft must implement Vehicle")

@check50.check(exists2)
def aircraft_is_abstract():
    """Aircraft is abstract"""
    f = open("Aircraft.java", "r")
    contents = f.read()
    if contents.find("public abstract class Aircraft") == -1:
        raise check50.Failure("Aircraft must be abstract")

@check50.check(exists3)
def car_extends_automobile():
    """Car extends Automobile"""
    f = open("Car.java", "r")
    contents = f.read()
    if contents.find("public class Car extends Automobile") == -1:
        raise check50.Failure("Car must extend Automobile")

@check50.check(exists4)
def truck_extends_automobile():
    """Truck extends Automobile"""
    f = open("Truck.java", "r")
    contents = f.read()
    if contents.find("public class Truck extends Automobile") == -1:
        raise check50.Failure("Truck must extend Automobile")

@check50.check(exists5)
def airplane_extends_aircraft():
    """Airplane extends Aircraft"""
    f = open("Airplane.java", "r")
    contents = f.read()
    if contents.find("public class Airplane extends Aircraft") == -1:
        raise check50.Failure("Airplane must extend Aircraft")

@check50.check(exists6)
def helicopter_extends_aircraft():
    """Helicopter extends Aircraft"""
    f = open("Helicopter.java", "r")
    contents = f.read()
    if contents.find("extends Aircraft") == -1:
        raise check50.Failure("Helicopter must extend Aircraft")

@check50.check(exists6)
def helicopter_implements_leaseable():
    """Helicopter implements Leaseable"""
    f = open("Helicopter.java", "r")
    contents = f.read()
    if contents.find("implements Leaseable") == -1:
        raise check50.Failure("Helicopter must implement Leaseable")

