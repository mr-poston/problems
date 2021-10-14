import check50

@check50.check()
def exists1():
    """MyStack.java exists"""
    check50.exists("MyStack.java")

@check50.check()
def exists2():
    """Grader.java exists"""
    check50.exists("Grader.java")

@check50.check(exists1)
def class_compiles():
    """MyStack.java compiles"""
    check50.run("javac MyStack.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """Grader.java compiles"""
    check50.run("javac Grader.java").exit(0)

@check50.check(class_compiles)
def constructors():
    """Both Constructors Work"""
    check50.run("java Grader x").exit(0)

@check50.check(constructors)
def is_empty():
    """isEmpty works for an empty stack"""
    check50.run("java Grader isEmpty").stdout("truetrue", regex=False).exit(0)

@check50.check(is_empty)
def push0():
    """push works when doubleCapacity needs to be called"""
    check50.run("java Grader push0").stdout("false1", regex=False).exit(0)

@check50.check(is_empty)
def push1():
    """push works"""
    check50.run("java Grader push1").stdout("false1", regex=False).exit(0)

@check50.check(class_compiles)
def pop0():
    """pop throws correct exception when stack is empty"""
    check50.run("java Grader pop0").stdout("ok", regex=False).exit(0)

@check50.check(class_compiles)
def pop1():
    """pop works when stack in NOT empty"""
    check50.run("java Grader pop1").stdout("7", regex=False).exit(0)
    
@check50.check(class_compiles)
def peek0():
    """peek throws correct exception when stack is empty"""
    check50.run("java Grader peek0").stdout("ok", regex=False).exit(0)

@check50.check(class_compiles)
def peek1():
    """peek works when stack in NOT empty"""
    check50.run("java Grader peek1").stdout("7", regex=False).exit(0)

@check50.check(push1)
def to_string():
    """toString works correctly"""
    check50.run("java Grader toString").stdout("1\t<----- TOP\n2\n3\n4\n5\n6", regex=False).exit(0)
