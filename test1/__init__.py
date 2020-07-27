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
  """"a b c a b c a   a -> [b, c, b, c]"""
  check50.run("java IRTest").stdout("[b, c, b, c]\n").exit(0)
