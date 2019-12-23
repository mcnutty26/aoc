import csv, sys
from vm import intcode_vm

program = []

# Read in the intcode program
with open("input.csv", 'rt') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for token in row:
            program.append(int(token))

# Boot up the computers
devs = []
sent_to_brd = False
since_sent = 0
NAT = [None, None]
NAT_Y = None
for i in range(50):
    devs.append(intcode_vm(program, [i], True))

# Process the messages
while True:
    sent = False
    msg_queue = []
    for dev in devs:
        dev.step()
        
        # We have a fully formed message
        if len(dev.output_queue) == 3:
            sent = True
            n, x, y = dev.output_queue
            dev.output_queue = []
            
            # Sent to NAT
            if n == 255:
                if not sent_to_brd:
                    sent_to_brd = True
                    print(y)
                NAT = [x, y]
            
            # Sent to a normal computer
            else:
                devs[n].input_queue += [x, y]
    
    # Keep track of inactivity
    if not sent:
        since_sent += 1
    
    # Looks like we're in a loop
    if since_sent > 5000:
        since_sent = 0
        devs[0].input_queue += NAT
        if NAT_Y == NAT[1]:
            print(NAT_Y)
            sys.exit(0)
        else:
            NAT_Y = NAT[1]
