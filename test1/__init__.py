import check50

@check50.check()
def exists():
  """IteratorRemover.java and IteratorRemoverRunner.java exist"""
  check50.exists("IteratorRemover.java", "IteratorRemoverRunner.java")
  
@check50.check(exists)
def check1():
  """"a b c a b c a   a -> [b, c, b, c]"""
  check50.run("java IteratorRemoverRunner").stdout("[b, c, b, c]").exit(0)
