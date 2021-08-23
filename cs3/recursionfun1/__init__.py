import check50

@check50.check()
def exists():
    """Recur.java exists"""
    check50.exists("Recur.java");

@check50.check(exists)
def class_compiles():
    """Recur.java compiles"""
    check50.run("javac Recur.java").exit(0)

@check50.check(class_compiles)
def test_1():
    """numEars works"""
    check50.run("java Grader 1").stdout("6", regex=False).exit(0)

@check50.check(class_compiles)
def test_2():
    """countdown works"""
    check50.run("java Grader 2").stdout("5, 4, 3, 2, 1, blastoff!", regex=False).exit(0)

@check50.check(class_compiles)
def test_3():
    """factorial works"""
    check50.run("java Grader 3").stdout("120", regex=False).exit(0)

@check50.check(class_compiles)
def test_4():
    """cheerlead works"""
    check50.run("java Grader 4").stdout("Go Team! Go Team! Go Team! ", regex=False).exit(0)

@check50.check(class_compiles)
def test_5():
    """pow works"""
    check50.run("java Grader 5").stdout("8", regex=False).exit(0)

@check50.check(class_compiles)
def test_6():
    """fibo works"""
    check50.run("java Grader 6").stdout("21", regex=False).exit(0)

@check50.check(class_compiles)
def test_7():
    """pattern works"""
    check50.run("java Grader 7").stdout("16, 11, 6, 1, -4\n10, 5, 0, -5", regex=False).exit(0)

@check50.check(class_compiles)
def test_8():
    """countNumA works"""
    check50.run("java Grader 8").stdout("3", regex=False).exit(0)

@check50.check(class_compiles)
def test_9():
    """printAtoBbyC works"""
    check50.run("java Grader 9").stdout("10 15 20 25 30", regex=False).exit(0)

@check50.check(class_compiles)
def test_10():
    """countOdds works"""
    check50.run("java Grader 10").stdout("3", regex=False).exit(0)

@check50.check(class_compiles)
def test_11():
    """sumDigits works"""
    check50.run("java Grader 11").stdout("11", regex=False).exit(0)