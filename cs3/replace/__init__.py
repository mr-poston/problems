import check50

@check50.check()
def exists():
    """IteratorReplacer.java and IteratorReplacerRunner.java exist"""
    check50.exists("IteratorReplacer.java", "IteratorReplacerRunner.java")

@check50.check(exists)
def replacer_compiles():
    """IteratorReplacer.java compiles"""
    check50.run("javac IteratorReplacer.java").exit(0)

@check50.check(exists)
def runner_compiles():
    """IteratorReplacerRunner.java compiles"""
    check50.run("javac IteratorReplacerRunner.java").exit(0)

@check50.check(exists)
def example1():
    """Example #1"""
    check50.run("java IRTest \"a b c a b c\" \"a\" \"+\"").stdout("[+, b, c, +, b, c]", regex=False).exit(0)

@check50.check(exists)
def example2():
    """Example #2"""
    check50.run("java IRTest \"a b c d e f g h i j x x x x\" \"x\" \"7\"").stdout("[a, b, c, d, e, f, g, h, i, j, 7, 7, 7, 7]", regex=False).exit(0)

@check50.check(exists)
def example3():
    """Example #3"""
    check50.run("java IRTest \"1 2 3 4 5 6 a b c a b c\" \"b\" \"#\"").stdout("[1, 2, 3, 4, 5, 6, a, #, c, a, #, c]", regex=False).exit(0)

@check50.check(exists)
def empty_list():
    """Handles empty list"""
    check50.run("java IRTest \"\" \"\" \"\"").stdout("[]", regex=False).exit(0)

@check50.check(exists)
def uses_list_iterator():
    """Uses ListIterator"""
    f = open("IteratorReplacer.java", "r")
    contents = f.read()
    if contents.find(".listIterator()") == -1:
        raise check50.Failure("You must use a ListIterator")
