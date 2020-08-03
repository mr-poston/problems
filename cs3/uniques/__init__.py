import check50

@check50.check()
def exists():
    """UniquesDupes.java and DupRunner.java exist"""
    check50.exists("UniquesDupes.java", "DupRunner.java")

@check50.check(exists)
def class_compiles():
    """UniquesDupes.java compiles"""
    check50.run("javac UniquesDupes.java").exit(0)

@check50.check(exists)
def runner_compiles():
    """DupRunner.java compiles"""
    check50.run("javac DupRunner.java").exit(0)

@check50.check(exists)
def example1():
    """Example #1"""
		out1 = "a b c d e f g h a b c d e f g h i j k"
		out2 = "[a, b, c, d, e, f, g, h, i, j, k]"
		out3 = "[a, b, c, d, e, f, g, h]"
    check50.run("java Grader \"a b c d e f g h a b c d e f g h i j k\"").stdout("a b c d e f g h a b c d e f g h i j k\n[a, b, c, d, e, f, g, h, i, j, k]\n[a, b, c, d, e, f, g, h]", regex=False).exit(0)

@check50.check(exists)
def example2():
		"""Example #2"""
		out1 = "one two three one two three six seven one two"
		out2 = "[one, seven, six, three, two]"
		out3 = "[one, three, two]"
		check50.run("java Grader \"one two three one two three six seven one two\"").stdout("one two three one two three six seven one two\n[one, seven, six, three, two]\n[one, three, two]", regex=False).exit(0)
		