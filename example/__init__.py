import check50 # import the check50 module

@check50.check() # tag the function below as check50 check
def exists(): # the name of the check
    """description""" # this is what you will see when running check50
    check50.exists("hello.py") # the actual check

@check50.check(exists) # only run this check id the exists check has passed
def hello_world():
    """hello world"""
    check50.run("python3 hello.py").stdout("[Hh]ello, world!", regex=True).exit(0)
