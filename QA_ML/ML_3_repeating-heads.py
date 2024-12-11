
# Probability of a given outcome: 0.5**n
# Probability I win a bet ie we get all heads = 0.5**n
# Probability I lose a given bet = 1 - 0.5**n
# Probability I lose x bets in a row: (1 - 0.5**n)**x
# Probability I win at least one of x bets: (1 - (1 - 0.5**n)**x)
# For me to at least break even:
# payout*(Probability I win at least one) > 100
# payout > 100 / (Probability I win at least one)
# payout > 100 / (1 - (1 - 0.5**n)**x)
#
# NOTE: I think the problem could be worded more clearly:
# (1) currently, it can be reasonably interpreted to mean that payouts
#     happen after every trial.
# (2) The phrase "ensure that you at least break even" implies a guaranteed
#     break-even payout, whereas what's being computed is an amount
#     that breaks-even in-expectation.


def repeating_heads(n, x):
    prob = (1-(1-0.5**n)**x)
    payout = 100/prob
    return [prob * 100, payout]
