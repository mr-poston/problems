import check50

@check50.check()
def exists1():
    """Monster.java exists"""
    check50.exists("Monster.java")

@check50.check()
def exists2():
    """MonsterRunner.java exists"""
    check50.exists("MonsterRunner.java")

@check50.check()
def exists3():
    """Skeleton.java exists"""
    check50.exists("Skeleton.java")

@check50.check(exists2)
def monsterrunner_compiles():
    """MonsterRunner.java compiles"""
    check50.run("javac MonsterRunner.java").exit(0)

@check50.check(exists3)
def skeleton_compiles():
    """Skeleton.java compiles"""
    check50.run("javac Skeleton.java").exit(0)

@check50.check()
def to_string():
    """toString implemented correctly"""
    check50.run("java Grader Brad 2 Sally 7 toString").stdout("Brad 2 Sally 7", regex=False).exit(0)

@check50.check()
def get_how_big():
    """getHowBig implemented correctly"""
    check50.run("java Grader Brad 2 Sally 7 getHowBig").stdout("true", regex=False).exit(0)

@check50.check()
def get_name():
    """getName implemented correctly"""
    check50.run("java Grader Brad 2 Sally 7 getName").stdout("true", regex=False).exit(0)

@check50.check()
def is_bigger():
    """isBigger implemented correctly"""
    check50.run("java Grader Brad 2 Sally 7 isBigger").stdout("false", regex=False).exit(0)

@check50.check()
def is_smaller():
    """isSmaller implemented correctly"""
    check50.run("java Grader Brad 2 Sally 7 isSmaller").stdout("true", regex=False).exit(0)

@check50.check()
def names_the_same():
    """namesTheSame implemented correctly"""
    check50.run("java Grader Brad 2 Sally 7 namesTheSame").stdout("false", regex=False).exit(0)
