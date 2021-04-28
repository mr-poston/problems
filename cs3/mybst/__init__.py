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
    check50.run("java BSTRunner").stdout("Original Tree >>> \
                                            1 2 3 4 6 8 9 10 15 16 20 25 \
                                            \
                                            Check whether Node with value 4 exists >>> true \
                                            \
                                            Delete Node with no children (2) >>> true \
                                            1 3 4 6 8 9 10 15 16 20 25 \
                                            \
                                            Delete Node with one child (4) >>> true \
                                            1 3 6 8 9 10 15 16 20 25 \
                                            \
                                            Delete Node with Two children (10) >>> true \
                                            1 3 6 8 9 15 16 20 25 \
                                            \
                                            Final state of tree: \
                                            1 3 6 8 9 15 16 20 25 \
                                            \
                                            Minimum value >>> 1 \
                                            \
                                            Maximum value >>> 25 \
                                            \
                                                    1 \
                                                2 \
                                                    3 \
                                            5 \
                                                6 \
                                                    9", regex=False).exit(0)
