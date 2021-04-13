chocolate_bars = 18
people = 5
whole_bars = chocolate_bars // people
print("Whole chocolate bars each = {}".format(whole_bars))
extra_squares = whole_bars % 7
print("Extra squares each = {}".format(extra_squares))
left_over = whole_bars - extra_squares
print("Squares left over = {}".format(left_over))

