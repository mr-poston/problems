import check50

@check50.check()
def exists1():
    """Monster.java exists"""
    check50.exists("Monster.java")

@check50.check()
def exists2():
    """MonsterRunner.java exists"""
    check50.exists("MonsterRunner.java")

@check50.check(exists1)
def monster_compiles():
    """Monster.java compiles"""
    check50.run("javac Monster.java").exit(0)

@check50.check(exists2)
def monsterrunner_compiles():
    """MonsterRunner.java compiles"""
    check50.run("javac MonsterRunner.java").exit(0)

@check50.check()
def zero():
    """No-parameter constructor implemented correctly"""
    check50.run("java Grader 0").stdout("0 0 0", regex=False).exit(0)

@check50.check()
def one():
    """One-parameter constructor implemented correctly"""
    check50.run("java Grader 1").stdout("8 0 0", regex=False).exit(0)

@check50.check()
def two():
    """Two-parameter constructor implemented correctly"""
    check50.run("java Grader 2").stdout("9 4 0", regex=False).exit(0)

@check50.check()
def three():
    """Three-parameter constructor implemented correctly"""
    check50.run("java Grader 3").stdout("1 2 3", regex=False).exit(0)

@check50.check()
def four():
    """Setter methods implemented correctly"""
    check50.run("java Grader 4").stdout("7 6 5", regex=False).exit(0)

@check50.check()
def five():
    """clone() method implemented correctly"""
    check50.run("java Grader 5").stdout("7 6 5", regex=False).exit(0)

@check50.check()
def six():
    """compareTo method correctly returns -1"""
    check50.run("java Grader 6").stdout("-1", regex=False).exit(0)

@check50.check()
def seven():
    """compareTo method correctly returns 1"""
    check50.run("java Grader 7").stdout("1", regex=False).exit(0)

@check50.check()
def eight():
    """compareTo method correctly returns 0"""
    check50.run("java Grader 8").stdout("0", regex=False).exit(0)

