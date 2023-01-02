from expression import compose
from expression.collections import seq, Seq

xs = Seq.of(2, 1, 11)
custom = compose(
    seq.map(lambda x: x * 10),
    seq.filter(lambda x: x > 100),
    seq.fold(lambda s, x: s + x, 0)
)
ys = custom(xs)
