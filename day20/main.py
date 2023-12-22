import sys
import collections
import itertools

with open("example.txt" if "x" in sys.argv else "input.txt") as f:
    data = f.read()

counts = [0, 0]
types = {"rx": "r"}
outputs = collections.defaultdict(list)
inputs = collections.defaultdict(list)
states = {}

for line in data.splitlines():
    sym, outs = line.split(' -> ')
    first = sym[0]
    if first != 'b':
        sym = sym[1:]
    types[sym] = first
    for out in outs.replace(' ', '').split(','):
        outputs[sym].append(out)
        inputs[out].append(sym)

for sym, typ in types.items():
    if typ == '%':
        states[sym] = 0
    if typ == '&':
        states[sym] = {inp: 0 for inp in inputs[sym]}

p1 = 0
p2 = 1

history = {k: 0 for k in inputs[inputs["rx"][0]]}

for i in itertools.count(1):

    pulses = collections.deque([("broadcaster", 0, "button")])

    while pulses:
        sym, sig, src = pulses.popleft()
        counts[sig] += 1
        if types[sym] == '%' and not sig:
            states[sym] ^= 1
            pulses.extend((out, states[sym], sym) for out in outputs[sym])
        elif types[sym] == '&':
            states[sym][src] = sig
            send = 1 - all(v == 1 for v in states[sym].values())
            pulses.extend((out, send, sym) for out in outputs[sym])
        elif types[sym] == 'b':
            pulses.extend((out, sig, sym) for out in outputs[sym])

        if sym in history and sig == 0 and history[sym] == 0:
            history[sym] = i

    if all(history.values()):
        break

    if i == 1000:
        p1 = counts[0] * counts[1]

for v in history.values():
    p2 *= v

print(f"Part one: {p1}")
print(f"Part two: {p2}")
