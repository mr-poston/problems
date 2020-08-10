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
    """DeckTestOne.java exists"""
    check50.exists("DeckTestOne.java")

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

@check50.check(exists3)
def decktestone_compiles():
    """DeckTestOne.java compiles"""
    check50.run("javac DeckTestOne.java").exit(0)

@check50.check()
def blank_card():
    """Deck class seems to function correctly"""
    output = check50.run("java Grader").stdout()
    if output != "0\n52\n51\n44\n52":
        raise check50.Failure("Hmmm... something is not right with Deck")
