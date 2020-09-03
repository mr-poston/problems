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
    """Dealer.java exists"""
    check50.exists("Dealer.java")

@check50.check()
def exists6():
    """DealerTestOne.java exists"""
    check50.exists("DealerTestOne.java")

@check50.check(exists5)
def dealer_compiles():
    """Dealer.java compiles"""
    check50.run("javac Dealer.java").exit(0)

@check50.check()
def shuffle_check():
    """Shuffles the deck"""
    f = open("Dealer.java", "r")
    contents = f.read()
    if contents.find(".shuffle();") == -1:
        raise check50.Failure("You must call Deck's shuffle method");

@check50.check()
def deal_check():
    """Deals the next card from the deck"""
    f = open("Dealer.java", "r")
    contents = f.read()
    if contents.find(".nextCard();") == -1:
        raise check50.Failure("You must call Deck's nextCard method");

@check50.check()
def left_check():
    """Correctly returns the number of cards left in the deck"""
    f = open("Dealer.java", "r")
    contents = f.read()
    if contents.find(".numCardsLeft();") == -1:
        raise check50.Failure("You must ask the deck how many cards are left");

