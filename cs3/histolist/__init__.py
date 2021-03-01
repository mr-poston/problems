import check50

@check50.check()
def exists1():
    """HistoList.java exists"""
    check50.exists("HistoList.java");

@check50.check(exists1)
def class_compiles():
    """HistoList.java compiles"""
    check50.run("javac HistoList.java").exit(0)

@check50.check(class_compiles)
def test_to_string():
    """toString works correctly"""
    check50.run("java Grader toString").stdout("E - 1\tS - 2\tV - 1\tB - 1\tA - 7\t", regex=False).exit(0)

@check50.check(class_compiles)
def test_add_letter():
    """addLetter works correctly"""
    check50.run("java Grader addLetter").stdout("Z - 1\t", regex=False).exit(0)

@check50.check(class_compiles)
def test_index_of():
    """indexOf works correctly"""
    check50.run("java Grader indexOf").stdout("3", regex=False).exit(0)

@check50.check(class_compiles)
def test_node_at():
    """nodeAt works correctly"""
    check50.run("java Grader nodeAt").stdout("true", regex=False).exit(0)