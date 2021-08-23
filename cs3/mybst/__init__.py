import check50

@check50.check()
def exists():
    """MyBST.java exists"""
    check50.exists("MyBST.java");

@check50.check(exists)
def class_compiles():
    """MyBST.java compiles"""
    check50.run("javac MyBST.java").exit(0)

@check50.check(class_compiles)
def test_0():
    """insert and inOrder work"""
    check50.run("java Grader inOrder").stdout("1 2 3 5 6 9", regex=False).exit(0)

@check50.check(class_compiles)
def test_1():
    """contains works"""
    check50.run("java Grader contains").stdout("true", regex=False).exit(0)

@check50.check(class_compiles)
def test_2():
    """deleting a node with no children works"""
    check50.run("java Grader delete0").stdout("true", regex=False).exit(0)

@check50.check(class_compiles)
def test_3():
    """deleting a node with 1 child works"""
    check50.run("java Grader delete1").stdout("true", regex=False).exit(0)

@check50.check(class_compiles)
def test_4():
    """deleting a node with 2 children works"""
    check50.run("java Grader delete2").stdout("true", regex=False).exit(0)

@check50.check(class_compiles)
def test_5():
    """attempting to delete a node that is not in the tree works"""
    check50.run("java Grader deleteNo").stdout("false", regex=False).exit(0)

@check50.check(class_compiles)
def test_6():
    """getMax works"""
    check50.run("java Grader getMax").stdout("9", regex=False).exit(0)

@check50.check(class_compiles)
def test_7():
    """getMin works"""
    check50.run("java Grader getMin").stdout("1", regex=False).exit(0)

@check50.check(class_compiles)
def test_8():
    """print works"""
    check50.run("java Grader print").stdout("        1\n    2\n        3\n5\n    6\n        9", regex=False).exit(0)
