import check50

@check50.check()
def exists():
    """Maze.java exists"""
    check50.exists("Maze.java");

@check50.check(exists)
def class_compiles():
    """Maze.java compiles"""
    check50.run("javac Maze.java").exit(0)

@check50.checks(class_compiles)
def test_0():
    """Works for Maze 0"""
    check50.run("java Grader 0").stdout("exit not found", regex=False).exit(0)

@check50.checks(class_compiles)
def test_0():
    """Works for Maze 1"""
    check50.run("java Grader 1").stdout("exit found", regex=False).exit(0)

@check50.checks(class_compiles)
def test_0():
    """Works for Maze 2"""
    check50.run("java Grader 2").stdout("exit not found", regex=False).exit(0)

@check50.checks(class_compiles)
def test_0():
    """Works for Maze 3"""
    check50.run("java Grader 3").stdout("exit found", regex=False).exit(0)

@check50.checks(class_compiles)
def test_0():
    """Works for Maze 4"""
    check50.run("java Grader 4").stdout("exit found", regex=False).exit(0)

@check50.checks(class_compiles)
def test_0():
    """Works for Maze 5"""
    check50.run("java Grader 5").stdout("exit not found", regex=False).exit(0)

@check50.checks(class_compiles)
def test_0():
    """Works for Maze 6"""
    check50.run("java Grader 6").stdout("exit found", regex=False).exit(0)

@check50.checks(class_compiles)
def test_0():
    """Works for Maze 7"""
    check50.run("java Grader 7").stdout("exit not found", regex=False).exit(0)
