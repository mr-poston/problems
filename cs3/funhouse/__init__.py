import check50

@check50.check()
def exists1():
    """ListFunHouse.java exists"""
    check50.exists("ListFunHouse.java");

@check50.check(exists1)
def class_compiles():
    """ListFunHouse.java compiles"""
    check50.run("javac ListFunHouse.java")

@check50.check(class_compiles)
def test_print():
    """print works correctly"""
    check50.run("java Grader print").stdout("go on at 34 2.1 -a-2-1 up over ", regex=False).exit(0)

@check50.check(class_compiles)
def test_node_count():
    """nodeCount works correctly"""
    check50.run("java Grader nodeCount").stdout("8", regex=False).exit(0)

@check50.check(class_compiles)
def test_double_first():
    """doubleFirst works correctly"""
    check50.run("java Grader doubleFirst").stdout("go go on at 34 2.1 -a-2-1 up over ", regex=False).exit(0)

@check50.check(class_compiles)
def test_double_last():
    """doubleLast works correctly"""
    check50.run("java Grader doubleLast").stdout("go on at 34 2.1 -a-2-1 up over over ", regex=False).exit(0)

@check50.check(class_compiles)
def test_remove_xth_node():
    """removeXthNode works correctly"""
    check50.run("java Grader removeX").stdout("go at 2.1 up ", regex=False).exit(0)

@check50.check(class_compiles)
def test_set_xth_node():
    """setXthNode works correctly"""
    check50.run("java Grader setX").stdout("go one at one 2.1 one up one ", regex=False).exit(0)
