import check50

@check50.check()
def exists1():
    """IntQueue.java exists"""
    check50.exists("IntQueue.java")

@check50.check()
def exists2():
    """IntQueueRunner.java exists"""
    check50.exists("IntQueueRunner.java")

@check50.check(exists1)
def class_compiles():
    """IntQueue.java compiles"""
    check50.run("javac IntQueue.java").exit(0)

@check50.check(exists2)
def runner_compiles():
    """IntQueueRunner.java compiles"""
    check50.run("javac IntQueueRunner.java").exit(0)

@check50.check(runner_compiles)
def example1():
    """Sample output looks good"""
    check50.run("java IntQueueRunner").stdout("[5, 7, 9]\nfalse\n5\n7\n7\n9\ntrue\n[]\n-2147483648", regex=False).exit(0)

