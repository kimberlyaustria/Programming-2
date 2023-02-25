# Write your code here
def add_indices(xs):
    ys = []
    for i in range(len(xs)):
        ys += [i]

    return list(zip(ys, xs))
