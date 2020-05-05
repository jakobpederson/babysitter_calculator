from datetime import datetime


def babysitter_calculator(family, start, end):
    start = int(start.split(':')[0])
    end = int(end.split(':')[0])
    end = end if end > start else end + 12
    x = family['first']
    y = family['second']
    time_break = family['break'] if family['break'] > start else family['break'] + 12
    first_period_wage = (time_break - start) * x
    second_period_wage = (end - time_break) * y
    return first_period_wage + second_period_wage
