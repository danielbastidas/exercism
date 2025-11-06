package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	var value int
    switch card {
        case "ace":
    		value = 11    	
        case "two":
        	value = 2
        case "three":
        	value = 3
        case "four":
        	value = 4
        case "five":
        	value = 5
        case "six":
        	value = 6
        case "seven":
        	value = 7
        case "eight":
        	value = 8
        case "nine":
        	value = 9
        case "ten":
        	value = 10
        case "jack":
        	value = 10
        case "queen":
        	value = 10
        case "king":
        	value = 10
        default:
        	value = 0
    }

    return value
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	var handValue int = ParseCard(card1) + ParseCard(card2)
    var dealerValue int = ParseCard(dealerCard)
    var play string
    switch {
    	case card1 == "ace" && card2 == "ace":
        	play = "P"
        case handValue == 21 && dealerValue < 10:
        	play = "W"
        case handValue == 21 && dealerValue >= 10:
        	play = "S"
        case handValue >= 17 && handValue <= 20:
        	play = "S"
        case handValue >= 12 && handValue <= 16 && dealerValue < 7:
        	play = "S"
        case handValue >= 12 && handValue <= 16 && dealerValue >= 7:
        	play = "H"
        case handValue <= 11:
        	play = "H"
    }

    return play
}
