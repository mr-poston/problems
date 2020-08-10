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
    """CardTestOne.java exists"""
    check50.exists("CardTestOne.java")

@check50.check(exists1)
def card_compiles():
    """Card.java compiles"""
    check50.run("javac Card.java").exit(0)

@check50.check(exists2)
def blackjackcard_compiles():
    """BlackJackCard.java compiles"""
    check50.run("javac BlackJackCard.java").exit(0)

@check50.check(exists3)
def cardtestone_compiles():
    """CardTestOne.java compiles"""
    check50.run("javac CardTestOne.java").exit(0)

@check50.check()
def blank_card():
    """Blank card produces a value of 0"""
    check50.run("java Grader").stdout("ZERO of  | value = 0", regex=False).exit(0)

@check50.check()
def ace_diamonds():
    """Ace of Diamonds is correct"""
    check50.run("java Grader \"1 DIAMONDS\"").stdout("ACE of DIMONDS | value = 11", regex=False).exit(0)

@check50.check()
def four_clubs():
    """Four of Clubs is correct"""
    check50.run("java Grader \"4 CLUBS\"").stdout("FOUR of CLUBS | value = 4", regex=False).exit(0)

@check50.check()
def queen_spades():
    """Queen of Spades is correct"""
    check50.run("java Grader \"12 SPADES\"").stdout("QUEEN of SPADES | value = 10", regex=False).exit(0)

@check50.check()
def queen_hearts():
    """Queen of HEARTS is correct"""
    check50.run("java Grader \"12 HEARTS\"").stdout("QUEEN of HEARTS | value = 10", regex=False).exit(0)

@check50.check()
def nine_spades():
    """Nine of SPADES is correct"""
    check50.run("java Grader \"9 SPADES\"").stdout("NINE of SPADES | value = 9", regex=False).exit(0)

