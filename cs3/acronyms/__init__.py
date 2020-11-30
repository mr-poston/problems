import check50

@check50.check()
def exists1():
    """Acronyms.java exists"""
    check50.exists("Acronyms.java")

@check50.check()
def exists2():
	"""AcroRunner.java exists"""
	check50.exists("AcroRunner.java")

@check50.check(exists1)
def class_compiles():
    """Acronyms.java compiles"""
    check50.run("javac Acronynms.java").exit(0)

@check50.check()
def example1():
    """First line works"""
    check50.run("java Grader").stdout("I drove my Pick Up to Texas State Optical to get a Hard Drive. My", regex=False).exit(0)

@check50.check()
def example2():
    """Second line works"""
    check50.run("java Grader").stdout("Central Processing Unit has a virus. I sometimes Strike Out", regex=False).exit(0)

@check50.check()
def example3():
    """Third line works"""
    check50.run("java Grader").stdout("when trying to kick a Field Goal. I had 2 Runs Batted In", regex=False).exit(0)

@check50.check()
def example4():
    """Fourth line works"""
    check50.run("java Grader").stdout("at the game. I saw 2 Public Display of Affection", regex=False).exit(0)

@check50.check()
def example5():
    """Fifth line works"""
    check50.run("java Grader").stdout("infractions in the hall.", regex=False).exit(0)
