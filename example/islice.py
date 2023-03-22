import itertools

d = {1: 2, 3: 4, 5: 6}

dict(itertools.islice(d.items(), 2))

# {1: 2, 3: 4}
