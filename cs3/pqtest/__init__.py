import check50

@check50.check()
def exists1():
    """PQTester.java exists"""
    check50.exists("PQTester.java")

@check50.check()
def exists2():
    """PQTesterRunner.java exists"""
    check50.exists("PQTesterRunner.java")

@check50.check(exists1)
def class_compiles():
    """PQTester.java compiles"""
    check50.run("javac PQTester.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """PQTesterRunner.java compiles"""
    check50.run("javac PQTesterRunner.java").exit(0)

@check50.check(class_compiles)
def example1():
    """Example 1"""
    check50.run("java PQTesterRunner.java")\
    .stdin("one two three four five six seven")\
    .stdout("[five, four, seven, two, one, three, six]\nfive\nfive four one seven six three two", regex=False).exit(0)

