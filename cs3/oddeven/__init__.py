import check50

@check50.check()
def exists1():
    """OddEvenSets.java exists"""
    check50.exists("OddEvenSets.java")

@check50.check()
def exists2():
	"""OddRunner.java exists"""
	check50.exists("OddRunner.java")

@check50.check(exists1)
def class_compiles():
    """OddEvenSets.java compiles"""
    check50.run("javac OddEvenSets.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """OddRunner.java compiles"""
    check50.run("javac OddRunner.java").exit(0)

@check50.check(exists1)
def example1():
    """Example #1"""
    check50.run("java OddRunner")\
		.stdout("ODDS : [1, 5, 9]\nEVENS : [4, 6, 8, 12]\n\n" +
		"ODDS : [3, 5, 7, 17, 29]\nEVENS : [4, 6, 56, 72]\n\n" +
		"ODDS : [3]\nEVENS : [2, 6, 12, 28]\n\n" +
		"ODDS : []\nEVENS : [4]\n\n" +
		"ODDS : [1]\nEVENS : []\n\n" +
		"ODDS : [1, 3, 5, 7, 9]\nEVENS : [2, 4, 6, 8]\n\n", regex=False).exit(0)