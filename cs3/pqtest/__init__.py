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
    """one two three four five six seven"""
    check50.run("java PQTesterRunner.java")\
    .stdin("one two three four five six seven")\
    .stdout("[five, four, seven, two, one, three, six]\nfive\nfive four one seven six three two", regex=False).exit(0)

@check50.check(class_compiles)
def example2():
    """1 2 3 4 5 one two three four five"""
    check50.run("java PQTesterRunner.java")\
    .stdin("1 2 3 4 5 one two three four five")\
    .stdout("[1, 2, 3, 4, 5, one, two, three, four, five]\n1\n1 2 3 4 5 five four one three two", regex=False).exit(0)

@check50.check(class_compiles)
def example3():
    """a p h j e f m c i d k l g n o b"""
    check50.run("java PQTesterRunner.java")\
    .stdin("a p h j e f m c i d k l g n o b")\
    .stdout("[a, b, f, c, d, g, m, e, i, j, k, l, h, n, o, p]\na\na b c d e f g h i j k l m n o p", regex=False).exit(0)
