import check50

@check50.check()
def exists1():
    """MathSet.java exists"""
    check50.exists("MathSet.java")

@check50.check()
def exists2():
	"""Grader.java exists"""
	check50.exists("Grader.java")

@check50.check(exists1)
def class_compiles():
    """MathSet.java compiles"""
    check50.run("javac MathSet.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """Grader.java compiles"""
    check50.run("javac Grader.java").exit(0)

@check50.check()
def example1():
    """Example 1"""
    check50.run("java Grader \"1 2 3 4 5\" \"4 5 6 7 8\"")\
            .stdout("[1, 2, 3, 4, 5, 6, 7, 8]\n[4, 5]\n[1, 2, 3]\n[6, 7, 8]\n[1, 2, 3, 6, 7, 8]", regex=False).exit(0)

@check50.check()
def example2():
    """Example 2"""
    check50.run("java Grader \"10 11 12 13 14 15 16 17\" \"11 13 15 17 19 21 23\"")\
            .stdout("[10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 23]\n[11, 13, 15, 17]\n[10, 12, 14, 16]\n[19, 21, 23]\n[10, 12, 14, 16, 19, 21, 23]", regex=False).exit(0)

@check50.check()
def example3():
    """Example 3"""
    check50.run("java Grader \"4 5 6 7 8 76\" \"3 4 5 6 23 46 53\"")\
            .stdout("[3, 4, 5, 6, 7, 8, 23, 46, 53, 76]\n[4, 5, 6]\n[7, 8, 76]\n[3, 23, 46, 53]\n[3, 7, 8, 23, 46, 53, 76]", regex=False).exit(0)

@check50.check()
def example4():
    """Empty Sets"""
    check50.run("java Grader \"\" \"\"")\
            .stdout("[]\n[]\n[]\n[]\n[]", regex=False).exit(0)

