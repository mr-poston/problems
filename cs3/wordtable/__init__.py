import check50

@check50.check()
def exists1():
    """Word.java exists"""
    check50.exists("Word.java");

@check50.check()
def exists2():
    """HashTable.java exists"""
    check50.exists("HashTable.java");

@check50.check(exists1)
def class1_compiles():
    """Word.java compiles"""
    check50.run("javac Word.java").exit(0)

@check50.check(exists2)
def class2_compiles():
    """HashTable.java compiles"""
    check50.run("javac HashTable.java").exit(0)

@check50.check(class1_compiles)
def test_hash_code():
    """Word's hashCode method works"""
    check50.run("java Grader wordHash").stdout("8", regex=False).exit(0)

@check50.check(class1_compiles)
def test_hash_code():
    """Word's equals method works"""
    check50.run("java Grader wordEquals").stdout("truefalse", regex=False).exit(0)

@check50.check(class2_compiles)
def test_hash_code():
    """HashTables's add and toString methods work"""
    check50.run("java Grader add").stdout("HASHTABLE\n" \
                                        + "bucket 0 [onimonapia]\n" \
                                        + "bucket 1 [hootowl, a]\n" \
                                        + "bucket 2 [ferret, go]\n" \
                                        + "bucket 3 [two, dog, cat, pig, owl, run, hop]\n" \
                                        + "bucket 4 [chicken, jump]\n" \
                                        + "bucket 5 []\n" \
                                        + "bucket 6 [one, shortcut, alligator]\n" \
                                        + "bucket 7 []\n" \
                                        + "bucket 8 [goat, food]\n" \
                                        + "bucket 9 []\n", regex=False).exit(0)
