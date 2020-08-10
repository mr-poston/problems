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
