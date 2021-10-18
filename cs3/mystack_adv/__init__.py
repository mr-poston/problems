import check50

@check50.check()
def exists1():
    """MyStack.java exists"""
    check50.exists("MyStack.java")

@check50.check(exists1)
def class_compiles():
    """Great! Your code compiles! Mr. Poston will grade it by hand"""
    check50.run("javac MyStack.java").exit(0)

