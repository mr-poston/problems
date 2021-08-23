import check50

@check50.check()
def exists1():
    """StackTest.java exists"""
    check50.exists("StackTest.java")

@check50.check()
def exists2():
	"""Grader.java exists"""
	check50.exists("Grader.java")

@check50.check(exists1)
def class_compiles():
    """StackTest.java compiles"""
    check50.run("javac StackTest.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """Grader.java compiles"""
    check50.run("javac Grader.java").exit(0)

@check50.check()
def example1():
    """Example 1"""
    check50.run("java Grader 1")\
            .stdout("[a, b, c, d, e, f, g, h, i]\n\npopping all items from the stack\ni h g f e d c b a", regex=False).exit(0)

@check50.check()
def example2():
    """Example 2"""
    check50.run("java Grader 2")\
            .stdout("[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\npopping all items from the stack\n10 9 8 7 6 5 4 3 2 1", regex=False).exit(0)

@check50.check()
def example3():
    """Example 3"""
    check50.run("java Grader 3")\
            .stdout("[#, $, %, ^, *, (, ), ), _]\n\npopping all items from the stack\n_ ) ) ( * ^ % $ #", regex=False).exit(0)

@check50.check()
def example4():
    """Works with no-parameter constructor"""
    check50.run("java Grader")\
            .stdout("[]\n\npopping all items from the stack\n", regex=False).exit(0)

