import check50

@check50.check()
def exists1():
    """Automobile.java exists"""
    check50.exists("Automobile.java")

@check50.check(exists1)
def automobile_compiles():
    """Automobile.java compiles"""
    check50.run("javac Automobile.java").exit(0)

@check50.check(exists1)
def automobile_implements_vehicle():
    """Automobile implements Vehicle"""
    f = open("Automobile.java", "r")
    contents = f.read()
    if contents.find("public class Automobile implements Vehicle") == -1:
        raise check50.Failure("Automobile must implement Vehicle")

