import check50

@check50.check()
def exists1():
    """SpanishToEnglish.java exists"""
    check50.exists("SpanishToEnglish.java")

@check50.check()
def exists2():
	"""SpanRunner.java exists"""
	check50.exists("SpanRunner.java")

@check50.check(exists1)
def class_compiles():
    """SpanishToEnglish.java compiles"""
    check50.run("javac SpanishToEnglish.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """SpanRunner.java compiles"""
    check50.run("javac SpanRunner.java").exit(0)

@check50.check()
def example1():
    """putEntry method works"""
    check50.run("java Grader 1 \"ordenador computer\" \"quiero want\" \"una a\" \"virus virus\" \"yo i\"")\
            .stdout("{ordenador=computer\n quiero=want\n una=a\n virus=virus\n yo=i}", regex=False).exit(0)

@check50.check()
def example2():
    """translate method works"""
    check50.run("java Grader 2 \"ordenador computer\" \"quiero want\" \"una a\" \"virus virus\" \"yo i\"")\
            .stdout("i want a comuputer virus ", regex=False).exit(0)

