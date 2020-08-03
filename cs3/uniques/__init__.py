import check50

@check50.check()
def exists():
    """UniquesDupes.java and DupRunner.java exist"""
    check50.exists("UniquesDupes.java", "DupRunner.java")

@check50.check(exists)
def class_compiles():
    """UniquesDupes.java compiles"""
    check50.run("javac UniquesDupes.java").exit(0)

@check50.check(exists)
def runner_compiles():
    """DupRunner.java compiles"""
    check50.run("javac DupRunner.java").exit(0)

@check50.check(exists)
def example1():
    """Example #1"""
    check50.run("java Grader \"a b c d e f g h a b c d e f g h i j k\"").stdout("a b c d e f g h a b c d e f g h i j k\n[a, b, c, d, e, f, g, h, i, j, k]\n[a, b, c, d, e, f, g, h]", regex=False).exit(0)
