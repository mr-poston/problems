import check50

@check50.check()
def exists1():
    """Postfix.java exists"""
    check50.exists("Postfix.java")

@check50.check()
def exists2():
    """Grader.java exists"""
    check50.exists("Grader.java")

@check50.check(exists1)
def class_compiles():
    """Postfix.java compiles"""
    check50.run("javac Postfix.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """Grader.java compiles"""
    check50.run("javac Grader.java").exit(0)

@check50.check(class_compiles)
def example1():
    """Example 1"""
    check50.run("java Grader 1").stdout("2 7 + 1 2 + + = 12.0", regex=False).exit(0)

@check50.check(class_compiles)
def example2():
    """Example 2"""
    check50.run("java Grader 1").stdout("1 2 3 4 + + + = 10.0", regex=False).exit(0)

@check50.check(class_compiles)
def example3():
    """Example 3"""
    check50.run("java Grader 1").stdout("9 3 * 8 / 4 + = 7.375", regex=False).exit(0)

@check50.check(class_compiles)
def example4():
    """Example 4"""
    check50.run("java Grader 1").stdout("3 3 + 7 * 9 2 / + = 46.5", regex=False).exit(0)

@check50.check(class_compiles)
def example5():
    """Example 5"""
    check50.run("java Grader 1").stdout("9 3 / 2 * 7 9 * + 4 - = 65.0", regex=False).exit(0)

@check50.check(class_compiles)
def example6():
    """Example 6"""
    check50.run("java Grader 1").stdout("5 5 + 2 * 4 / 9 + = 14.0", regex=False).exit(0)

