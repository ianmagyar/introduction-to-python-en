test_intervals1 = [
    ('Dan', 7, 9),
    ('Paul', 8, 11),
    ('Julie', 10, 12),
    ('Jerry', 9, 1),
    ('Lewis', 11, 12),
    ('Mark', 10, 12),
    ('Nate', 9, 11),
    ('Ruby', 8, 10),
    ('Marge', 7, 8),
    ('Pete', 9, 11)
]
test_intervals2 = [
    ('Dan', 10, 12),
    ('Paul', 9, 12),
    ('Julie', 10, 12),
    ('Jerry', 9, 1),
    ('Lewis', 10, 11),
    ('Mark', 11, 2),
    ('Nate', 10, 1),
    ('Ruby', 9, 12),
    ('Marge', 9, 11),
    ('Pete', 9, 1),
    ('Jen', 10, 12),
    ('Rob', 10, 11),
    ('Matt', 11, 3),
    ('Brandon', 10, 1),
    ('Dave', 9, 11)
]
test_intervals_weights = [
    ('Dan', 8, 10, 1),
    ('Paul', 8, 11, 2),
    ('Julie', 8, 9, 3),
    ('Jerry', 11, 1, 4),
    ('Lewis', 9, 12, 2),
    ('Mark', 10, 12, 2),
    ('Nate', 10, 3, 1),
    ('Ruby', 11, 12, 2),
    ('Marge', 10, 12, 1),
    ('Pete', 8, 11, 2)
]


def load_intervals(intervals):
    # returns a list of intervals as tuples
    pass


def choose_time(interval_list):
    # return best time to party and number of friends present
    pass


def when_to_go(friends_list):
    # process intervals from list
    # call function to calculate best time for party
    # print results
    pass


def choose_time_constrained(interval_list, y_start, y_end):
    # return best time to party and number of friends present
    # look only in interval <y_start, y_end)
    pass


def choose_time_with_weights(interval_list):
    # return best time to party and total weight
    pass
