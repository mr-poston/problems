import check50

@check50.check()
def exists():
  """IteratorRemover.java and IteratorRemoverRunner.java exist"""
  check50.exists("IteratorRemover.java", "IteratorRemoverRunner.java")
  
@check50.check(exists)
def check0():
  """IteratorRemover.java compiles"""
  check50.run("javac IteratorRemover.java").exit(0)
  
@check50.check(exists)
def check1():
  """IteratorRemoverRunner.java compiles"""
  check50.run("javac IteratorRemoverRunner.java").exit(0)
  
@check50.check(exists)
def check2():
  """"Example #1"""
  check50.run("java IRTest \"a b c a b c a\" \"a\"").stdout("[b, c, b, c]").exit(0)

@check50.check(exists)
def check3():
  """Example #2"""
  check50.run("java IRTest \"a b c d e f g h i j x x x x\" \"x\"").stdout("[a, b, c, d, e, f, g, h, i, j]").exit(0)
