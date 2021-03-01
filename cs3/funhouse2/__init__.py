import check50

@check50.check()
def exists1():
    """ListFunHouse.java exists"""
    check50.exists("ListFunHouse.java");

@check50.check(exists1)
def class_compiles():
    """ListFunHouse.java compiles"""
    check50.run("javac ListFunHouse.java").exit(0)

@check50.check(class_compiles)
def test_to_string():
    """toString works correctly"""
    check50.run("java Grader print").stdout("over up -a-2-1 2.1 34 at on go ", regex=False).exit(0)

@check50.check(class_compiles)
def test_node_count():
    """nodeCount works correctly"""
    check50.run("java Grader nodeCount").stdout("8", regex=False).exit(0)

@check50.check(class_compiles)
def test_double_first():
    """doubleFirst works correctly"""
    check50.run("java Grader doubleFirst").stdout("over over up -a-2-1 2.1 34 at on go ", regex=False).exit(0)

@check50.check(class_compiles)
def test_double_last():
    """doubleLast works correctly"""
    check50.run("java Grader doubleLast").stdout("over up -a-2-1 2.1 34 at on go go ", regex=False).exit(0)

@check50.check(class_compiles)
def test_remove_xth_node():
    """removeXthNode works correctly"""
    check50.run("java Grader removeX").stdout("over -a-2-1 34 on", regex=False).exit(0)

@check50.check(class_compiles)
def test_set_xth_node():
    """setXthNode works correctly"""
    check50.run("java Grader setX").stdout("over one -a-2-1 one 34 one on one ", regex=False).exit(0)
