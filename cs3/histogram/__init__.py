import check50

@check50.check()
def exists1():
    """Histogram.java exists"""
    check50.exists("Histogram.java")

@check50.check()
def exists2():
	"""HistoRunner.java exists"""
	check50.exists("HistoRunner.java")

@check50.check(exists1)
def class_compiles():
    """Histogram.java compiles"""
    check50.run("javac Histogram.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """HistoRunner.java compiles"""
    check50.run("javac HistoRunner.java").exit(0)

@check50.check()
def example1():
    """a b c d e f g h i a c d e g h i h k works"""
    check50.run("java Grader \"a b c d e f g h i a c d e g h i h k\"")\
            .stdout("char\t1---5----01---5\na\t**\nb\t*\nc\t**\nd\t**\ne\t**\nf\t*\ng\t**\nh\t***\ni\t**\nk\t*\n\n", regex=False).exit(0)

@check50.check()
def example2():
    """1 2 3 4 5 6 1 2 3 4 5 1 3 1 2 3 4 works"""
    check50.run("java Grader \"1 2 3 4 5 6 1 2 3 4 5 1 3 1 2 3 4\"")\
            .stdout("char\t1---5----01---5\n1\t****\n2\t***\n3\t****\n4\t***\n5\t**\n6\t*\n\n", regex=False).exit(0)

@check50.check()
def example2():
    """Y U I O Q W E R T Y works"""
    check50.run("java Grader \"Y U I O Q W E R T Y\"")\
            .stdout("char\t1---5----01---5\nE\t*\nI\t*\nO\t*\nQ\t*\nR\t*\nT\t*\nU\t*\nW\t*\nY\t**\n\n", regex=False).exit(0)

@check50.check()
def example2():
    """4 T # @ ^ # # # works"""
    check50.run("java Grader \"4 T # @ ^ # # #\"")\
            .stdout("char\t1---5----01---5\n#\t****\n4\t*\n@\t*\nT\t*\n^\t*\n\n", regex=False).exit(0)

