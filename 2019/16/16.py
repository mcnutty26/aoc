signal = []
BASE = [0, 1, 0, -1]
BASE_CACHE = []

with open('input.txt', 'rt') as textfile:
    for line in textfile:
        line_i = int(line)
        while line_i is not 0:
            signal.insert(0, line_i % 10)
            line_i //= 10

def p_print(l):
    output = ""
    for element in l:
        output += str(element)
    return int(output)

def rel_base(n):
    if n < len(BASE_CACHE):
        return BASE_CACHE[n]
    output = []
    for item in BASE:
        for i in range(n+1):
            output.append(item)
    BASE_CACHE.append(output)
    return output

def rep_base(n, l):
    base = rel_base(n)
    output = []
    while len(output) < (l + 1):
        output += base
    output.pop(0)
    return output

def fft(start, phases):
    old = start.copy()
    for i in range(phases):
        new = []
        for j in range(len(old)):
            base = rep_base(j, len(old))
            new.append(abs(sum([old[i] * base[i] for i in range(len(old))])) % 10)
        old = new.copy()
    return new

def ffft(start, phases):
    start.reverse()
    old = start.copy()
    for i in range(phases):
        new = []
        total = 0
        for j in range(len(old)):
            total += old[j]
            new.append(total % 10)
        old = new.copy()
    new.reverse()
    return new

print(p_print(fft(signal, 100)[0:8]))
length = len(signal)
offset = p_print(signal[0:7])
signal *= 10000
signal = signal[offset - (offset % length):]
offset -= offset - (offset % length)
print(p_print(ffft(signal, 100)[offset:offset + 8]))
