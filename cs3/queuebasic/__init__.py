import check50

@check50.check()
def exists1():
    """PalinList.java exists"""
    check50.exists("PalinList.java")

@check50.check()
def exists2():
    """Grader.java exists"""
    check50.exists("Grader.java")

@check50.check()
def exists3():
    """PalinListRunner.java exists"""
    check50.exists("PalinListRunner.java")

@check50.check(exists1)
def class_compiles():
    """PalinList.java compiles"""
    check50.run("javac PalinList.java").exit(0)

@check50.check(exists2)
def grader_compiles():
    """Grader.java compiles"""
    check50.run("javac Grader.java").exit(0)

@check50.check(exists3)
def runner_compiles():
    """PalinListRunner.java compiles"""
    check50.run("javac PalinListRunner.java").exit(0)

@check50.check(grader_compiles)
def example1():
    """Example 1"""
    check50.run("java Grader 1").stdout("y", regex=False).exit(0)

@check50.check(grader_compiles)
def example2():
    """Example 2"""
    check50.run("java Grader 2").stdout("n", regex=False).exit(0)

@check50.check(grader_compiles)
def example3():
    """Example 3"""
    check50.run("java Grader 3").stdout("n", regex=False).exit(0)

@check50.check(grader_compiles)
def example4():
    """Example 4"""
    check50.run("java Grader 4").stdout("y", regex=False).exit(0)

@check50.check(grader_compiles)
def example5():
    """Example 5"""
    check50.run("java Grader 5").stdout("y", regex=False).exit(0)

@check50.check(grader_compiles)
def example6():
    """Example 6"""
    check50.run("java Grader 6").stdout("n", regex=False).exit(0)

@check50.check(runner_compiles)
def runner_check():
    """PalinListRunner output is correct"""
    check50.run("java PalinListRunner").stdout("[one, two, three, two, one] is a palinlist.\n\n[1, 2, 3, 4, 5, one, two, three, four, five] is not a palinlist.\n\n[a, b, c, d, e, f, g, x, y, z, g, f, h] is not a palinlist.\n\n[racecar, is, racecar] is a palinlist.\n\n[1, 2, 3, a, b, c, c, b, a, 3, 2, 1] is a palinlist.\n\n[chicken, is, a, chicken] is not a palinlist.\n\n", regex=False).exit(0)
