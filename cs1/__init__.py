import check50

@check50.check()
def Test_has_three_names():
    """Test has three names"""
    check50.run("python3 main.py").stdin("3", prompt=True) \
    .stdin("John", prompt=True) \
    .stdin("David", prompt=True) \
    .stdin("Poston", prompt=True) \
    .stdout("First name: John\nMiddle names: ['David']\nLast name: Poston\n", regex=False).exit()
    
@check50.check()
def Test_has_two_names():
    """Test has two names"""
    check50.run("python3 main.py").stdin("2", prompt=True) \
    .stdin("Marie", prompt=True) \
    .stdin("Antoinette", prompt=True) \
    .stdout("First name: Marie\nMiddle names: []\nLast name: Antionette\n", regex=False).exit()
    
@check50.check()
def Test_has_six_names():
    """Test has three names"""
    check50.run("python3 main.py").stdin("6", prompt=True) \
    .stdin("Catherine", prompt=True) \
    .stdin("the", prompt=True) \
    .stdin("Great", prompt=True) \
    .stdin("Empress", prompt=True) \
    .stdin("of", prompt=True) \
    .stdin("Russia", prompt=True) \
    .stdout("First name: Catherine\nMiddle names: ['the', 'Great', 'Empress', 'of']\nLast name: Russia\n", regex=False).exit()
