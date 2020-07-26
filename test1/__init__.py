import check50

@check50.check()
def exists():
  """IteratorRemover.java and IteratorRemoverRunner.java exist"""
  check50.exists("IteratorRemover.java", "IteratorRemoverRunner.java")
  
@check50.check(exists)
def compiles():
  """IteratorRemover.java compiles"""
  check50.java.compile("IteratorRemover.java")
