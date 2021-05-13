import check50

@check50.check()
def exists():
    """Heap.java exists"""
    check50.exists("Heap.java");

@check50.check(exists)
def class_compiles():
    """Heap.java compiles"""
    check50.run("javac Heap.java").exit(0)

@check50.check(class_compiles)
def test_empty():
    """Check empty heap"""
    check50.run("java Grader empty").stdout("[]", regex=False).exit(0)

@check50.check(class_compiles)
def test_add():
    """Add works correctly"""
    check50.run("java Grader add").stdout("[75, 17, 10, 9, 8, 2, 7, 1, 5]", regex=False).exit(0)

@check50.check(class_compiles)
def test_remove():
    """Remove works correctly"""
    check50.run("java Grader add").stdout("[17, 9, 10, 5, 8, 2, 7, 1]", regex=False).exit(0)
