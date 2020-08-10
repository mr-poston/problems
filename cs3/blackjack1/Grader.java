/****************************************
 * DO NOT DELETE OR CHANGE THIS FILE!!! *
 ****************************************/
import static java.lang.System.*;

public class Grader {
    public static void main(String[] args) {
        if (args.length == 0) {
            Card card = new BlackJackCard();
            out.println(card);
        } else if (args.length == 2) {
            Card card = new BlackJackCard(Integer.parseInt(args[0]), args[1]);
            out.println(card);
        } else if (args.length == 1 && args[0].equals("equals")) {
            Card one = new BlackJackCard();
            Card two = new BlackJackCard(1, "DIAMONDS");
            Card three = new BlackJackCard(4, "CLUBS");
            Card four  = new BlackJackCard(12, "SPADES");
            Card five = new BlackJackCard(12, "HEARTS");
            Card six = new BlackJackCard(9, "SPADES");
            out.println(one.equals(two));
            out.println(one.equals(one));
            out.println(four.equals(five));
            out.println(three.equals(four));
        } else if (args.length == 1 && args[0].equals("toString")) {
            Card c = new BlackJackCard(13, "CLUBS");
            out.println(c);
        }
    }
}
