from unittest import TestCase

from babysitter_calculator import babysitter_calculator

# The babysitter:

# starts no earlier than 5:00PM
# leaves no later than 4:00AM
# only babysits for one family per night
# gets paid for full hours (no fractional hours)
# should be prevented from mistakes when entering times (e.g. end time before start time, or outside of allowable work hours)
# The job:

# Pays different rates for each family (based on bedtimes, kids and pets, etc...)
# Family A pays $15 per hour before 11pm, and $20 per hour the rest of the night
# Family B pays $12 per hour before 10pm, $8 between 10 and 12, and $16 the rest of the night
# Family C pays $21 per hour before 9pm, then $15 the rest of the night
# The time ranges are the same as the babysitter (5pm through 4am)
# Deliverable:

# Calculate total pay, based on babysitter start and end time, and a family.
FAMILY = {'A': {'first': 15, 'second': 20, 'break': 11}, 'B': '', 'C': ''}


class BabysitterCalculatorTests(TestCase):


    def test_(self):
        start = '5:00 PM'
        end = '4:00 AM'
        wage = babysitter_calculator(FAMILY['A'], start, end)
        self.assertEqual(wage, 190)


