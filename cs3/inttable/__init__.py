import check50

@check50.check()
def exists1():
    """Number.java exists"""
    check50.exists("Number.java");

@check50.check()
def exists2():
    """HashTable.java exists"""
    check50.exists("HashTable.java");

@check50.check(exists1)
def class1_compiles():
    """Number.java compiles"""
    check50.run("javac Number.java").exit(0)

@check50.check(exists2)
def class2_compiles():
    """HashTable.java compiles"""
    check50.run("javac HashTable.java").exit(0)

@check50.check(class1_compiles)
def test_hash_code():
    """Number's hashCode method works"""
    check50.run("java Grader numberHash").stdout("4", regex=False).exit(0)

@check50.check(class1_compiles)
def test_hash_code():
    """Number's equals method works"""
    check50.run("java Grader numberEquals").stdout("truefalse", regex=False).exit(0)

@check50.check(class2_compiles)
def test_hash_code():
    """HashTables's add method works"""
    check50.run("java Grader add").stdout("[11]", regex=False).exit(0)