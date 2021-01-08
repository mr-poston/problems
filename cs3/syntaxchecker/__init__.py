import check50

@check50.check()
def exists1():
    """SyntaxChecker.java exists"""
    check50.exists("SyntaxChecker.java")

@check50.check()
def exists2():
	"""SyntaxCheckRunner.java exists"""
	check50.exists("SyntaxCheckRunner.java")

@check50.check(exists1)
def class_compiles():
    """SyntaxChecker.java compiles"""
    check50.run("javac SyntaxChecker.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """SyntaxCheckRunner.java compiles"""
    check50.run("javac SyntaxCheckRunner.java").exit(0)

@check50.check()
def example1():
    """SyntaxChecker works correctly"""
    check50.run("java SyntaxCheckRunner")\
            .stdout("(abc(*def) is incorrect.\n[{}] is correct.\n[ is incorrect.\n[{<()>}] is correct.\n{<html[value=4]*(12)>{$x}} is correct.\n[one]<two>{three}(four) is correct.\ncar(cdr(a)(b))) is incorrect.\ncar(cdr(a)(b)) is correct.", regex=False).exit(0)
