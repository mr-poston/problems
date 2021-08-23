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
    """BlackJack.java exists"""
    check50.exists("BlackJack.java")

@check50.check(exists6)
def dealer_compiles():
    """BlackJack.java compiles"""
    check50.run("javac BlackJack.java").exit(0)

@check50.check()
def shuffle_check():
    """Shuffles the deck"""
    f = open("BlackJack.java", "r")
    contents = f.read()
    if contents.find(".shuffle();") == -1:
        raise check50.Failure("Did you shuffle the deck?");

@check50.check()
def deal_check():
    """Deals the cards"""
    f = open("BlackJack.java", "r")
    contents = f.read()
    if contents.find(".addCardToHand(") == -1:
        raise check50.Failure("Did you deal any cards?");

@check50.check()
def hit_check():
    """Asks if players want to hit"""
    f = open("BlackJack.java", "r")
    contents = f.read()
    if contents.find(".hit()") == -1:
        raise check50.Failure("Did you give both the player and the dealer an option to hit?");

@check50.check()
def arraylist_check():
    """All players are stored in an ArrayList"""
    f = open("BlackJack.java", "r")
    contents = f.read()
    if contents.find("ArrayList<Player>") == -1:
        raise check50.Failure("Are all of the players (including the dealer) stored in an ArrayList?");
