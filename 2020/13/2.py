import sys

def main(in_string):
    buses = in_string.split('\n')[1]
    stamps = [x if x == 'x' else int(x) for x in in_string.split('\n')[1].split(',')]

    t = 0
    add = stamps[0]
    end = 2
    stack = stamps[:end]

    while True:
        first = True
        p1 = 0
        while True:
            if stack[-1] == 'x':
                break
            found = True
            t += add
            for idx,st in enumerate(stack):
                if not st == 'x':
                    if (t+idx) % st  == 0:
                        pass
                    else:
                        found = False
                        break

            if found == True:
                if first == False:
                    add = t-p1
                    t = p1
                    break
                else:
                    first = False
                    p1 = t
                    if len(stack) == len(stamps):
                        print(t)

        if len(stack) == len(stamps):
            break
        else:
            end += 1
            stack = stamps[:end]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
