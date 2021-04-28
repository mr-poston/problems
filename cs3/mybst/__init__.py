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
    """Everything looks good!"""
    check50.run("java BSTRunner").stdout("Original Tree >>>\n \
                                            1 2 3 4 6 8 9 10 15 16 20 25\n \
                                            \n \
                                            Check whether Node with value 4 exists >>> true\n \
                                            \n \
                                            Delete Node with no children (2) >>> true\n \
                                            1 3 4 6 8 9 10 15 16 20 25\n \
                                            \n \
                                            Delete Node with one child (4) >>> true\n \
                                            1 3 6 8 9 10 15 16 20 25\n \
                                            \n \
                                            Delete Node with Two children (10) >>> true\n \
                                            1 3 6 8 9 15 16 20 25\n \
                                            \n \
                                            Final state of tree:\n \
                                            1 3 6 8 9 15 16 20 25\n \
                                            \n \
                                            Minimum value >>> 1\n \
                                            \n \
                                            Maximum value >>> 25\n \
                                            \n \
                                                    1\n \
                                                2\n \
                                                    3\n \
                                            5\n \
                                                6\n \
                                                    9", regex=False).exit(0)
