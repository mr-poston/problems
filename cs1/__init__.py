import check50

@check50.check()
def Test_has_three_names():
    """Test has three names"""
    check50.run("python3 main.py").stdin("3\nJohn\nDavid\nPoston", prompt=True).stdout("Number of names: Name: Name: Name: First name: John\nMiddle names: ['David']\nLast name: Poston\n", regex=False).exit()
