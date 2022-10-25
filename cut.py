target = open("cut.cfg", "w")
file = open("CONFIG.cfg")
lines = []
for line in file:
        lines.append(line)
lines = lines[5:]

for K in range( len(lines)/2 ):
        coordinate = lines[K*2 + 1]
        z = float(coordinate.split()[2])
        if z > 5 and z < 30 :
                target.write(lines[K*2])
                target.write(lines[K*2 + 1])
