import check50

@check50.check()
def Test_has_three_names():
    """Test has three names"""
    check50.run("python3 main.py").stdin("3", prompt=True) \
    .stdin("John", prompt=True) \
    .stdin("David", prompt=True) \
    .stdin("Poston", prompt=True) \
    .stdout("First name: John\nMiddle names: ['David']\nLast name: Poston\n", regex=False).exit()
