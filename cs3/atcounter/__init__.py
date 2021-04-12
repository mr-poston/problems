import check50

@check50.check()
def exists():
    """AtCounter.java exists"""
    check50.exists("Recur.java");

@check50.check(exists)
def class_compiles():
    """AtCounter.java compiles"""
    check50.run("javac Recur.java").exit(0)

@check50.check(class_compiles)
def test_0():
    """toString works"""
    check50.run("java Grader 0").stdout("- - -\n@ - -\n@ @ -\n", regex=False).exit(0)

@check50.check(class_compiles)
def test_1():
    """testing pattern1 (5,0) works"""
    check50.run("java Grader 1").stdout("12", regex=False).exit(0)

@check50.check(class_compiles)
def test_2():
    """testing pattern2 (0,0) works"""
    check50.run("java Grader 2").stdout("16", regex=False).exit(0)

@check50.check(class_compiles)
def test_3():
    """testing pattern3 (2,2) works"""
    check50.run("java Grader 3").stdout("8", regex=False).exit(0)

@check50.check(class_compiles)
def test_4():
    """testing pattern4 (0,2) works"""
    check50.run("java Grader 4").stdout("5", regex=False).exit(0)
