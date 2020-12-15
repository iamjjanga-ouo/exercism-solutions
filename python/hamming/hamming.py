def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise Exception("Both strands length is different")

    return len([x for i,x in enumerate(strand_a) if x != strand_b[i]])

## Community Solutions
# 1
# def distance(strand_a, strand_b):
#     return sum(x != y for x, y in zip(strand_a, strand_b))

# 2
# def distance(strand_a, strand_b):
#     if len(strand_a) != len(strand_b):
#         raise Exception()
#     return len(list(filter(lambda x: x[0] != x[1], zip(strand_a, strand_b))))