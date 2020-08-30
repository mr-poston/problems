import check50

@check50.check()
def exists1():
    """Card.java exists"""
    check50.exists("Card.java")

@check50.check()
def exists2():
    """BlackJackCard.java exists"""
    check50.exists("BlackJackCard.java")

@check50.check()
def exists3():
    """Deck.java exists"""
    check50.exists("Deck.java")

@check50.check()
def exists4():
    """Player.java exists"""
    check50.exists("Player.java")

@check50.check()
def exists5():
    """PlayerTestOne.java exists"""
    check50.exists("PlayerTestOne.java")

@check50.check(exists1)
def card_compiles():
    """Card.java compiles"""
    check50.run("javac Card.java").exit(0)

@check50.check(exists2)
def blackjackcard_compiles():
    """BlackJackCard.java compiles"""
    check50.run("javac BlackJackCard.java").exit(0)

@check50.check(exists3)
def deck_compiles():
    """Deck.java compiles"""
    check50.run("javac Deck.java").exit(0)

@check50.check(exists4)
def decktestone_compiles():
    """Player.java compiles"""
    check50.run("javac Player.java").exit(0)

@check50.check(exists5)
def decktestone_compiles():
    """PlayerTestOne.java compiles"""
    check50.run("javac PlayerTestOne.java").exit(0)

@check50.check()
def add_to_hand():
    """addCardToHand and getHandValue function correctly"""
    check50.run("java Grader \"0\"").stdout("921", regex=False).exit(0)

@check50.check()
def get_win():
    """getWinCount and the 1 argument constructor function correctly"""
    check50.run("java Grader \"1\"").stdout("42", regex=False).exit(0)

@check50.check()
def set_win():
    """setWinCount and getWinCount function correctly"""
    check50.run("java Grader \"2\"").stdout("12", regex=False).exit(0)

@check50.check()
def add_to_hand():
    """getHandValue functions correctly"""
    check50.run("java Grader \"3\"").stdout("0", regex=False).exit(0)

