import check50

@check50.check()
def exists1():
    """Linkable.java exists"""
    check50.exists("Linkable.java");

@check50.check()
def exists2():
    """ListNode.java exists"""
    check50.exists("ListNode.java");

@check50.check()
def exists3():
    """MyLinkedList.java exists"""
    check50.exists("MyLinkedList.java");

@check50.check(exists3)
def class_compiles():
    """MyLinkedList.java compiles"""
    check50.run("javac MyLinkedList.java").exit(0)

@check50.check(class_compiles)
def test_to_string_empty():
    """no-parameter constructor and toString() work"""
    check50.run("java Grader toStringEmpty").stdout("[]", regex=False).exit(0)

@check50.check(class_compiles)
def test_to_string_one():
    """parameterized constructor and toString() work"""
    check50.run("java Grader toStringOne").stdout("[20]", regex=False).exit(0)

@check50.check(class_compiles)
def test_add():
    """one parameter add() and toString() work"""
    check50.run("java Grader add").stdout("[4, 5, 6]", regex=False).exit(0)

@check50.check(class_compiles)
def test_add():
    """indexOf() works"""
    check50.run("java Grader indexOf").stdout("2", regex=False).exit(0)

@check50.check(class_compiles)
def test_size():
    """size() works"""
    check50.run("java Grader size").stdout("3", regex=False).exit(0)

@check50.check(class_compiles)
def test_set():
    """set() work and toString() work"""
    check50.run("java Grader set").stdout("[4, 5, 100]", regex=False).exit(0)

@check50.check(class_compiles)
def test_size():
    """remove() works"""
    check50.run("java Grader remove").stdout("5", regex=False).exit(0)

@check50.check(class_compiles)
def test_add2():
    """two parameter add() and toString() work"""
    check50.run("java Grader add2").stdout("[4, 5, 50, 6]", regex=False).exit(0)
