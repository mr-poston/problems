import check50

@check50.check()
def exists1():
    """Relatives.java exists"""
    check50.exists("Relatives.java")

@check50.check()
def exists2():
	"""RelativesRunner.java exists"""
	check50.exists("RelativesRunner.java")

@check50.check(exists1)
def class_compiles():
    """Relatives.java compiles"""
    check50.run("javac Relatives.java").exit(0)

@check50.check()
def example1():
    """Works for Almas"""
    check50.run("java Grader Almas").stdout("[Brian]", regex=False).exit(0)

@check50.check()
def example2():
    """Works for Bob"""
    check50.run("java Grader Bob").stdout("[John, Tom]", regex=False).exit(0)

@check50.check()
def example3():
    """Works for Dot"""
    check50.run("java Grader Dot").stdout("[Chuck, Fred, Jason, Tom]", regex=False).exit(0)

@check50.check()
def example4():
    """Works for Elton"""
    check50.run("java Grader Elton").stdout("[Linh]", regex=False).exit(0)

@check50.check()
def example5():
    """Works for Fred"""
    check50.run("java Grader Fred").stdout("[Alice, James]", regex=False).exit(0)

@check50.check()
def example6():
    """Works for Jim"""
    check50.run("java Grader Jim").stdout("[Sally, Tammy, Tom]", regex=False).exit(0)

@check50.check()
def example2():
    """Works for Timmy"""
    check50.run("java Grader Timmy").stdout("[Amanda]", regex=False).exit(0)
