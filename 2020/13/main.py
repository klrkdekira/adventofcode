from functools import reduce 

def nearest(departure, buses):
    lowest = 0

    prev = None
    for bus in buses:
        distance = departure % bus
        delta = bus - distance 
        
        if prev == None:
            lowest = bus
            prev = delta
            continue

        if prev > delta:
            lowest = bus
            prev = delta

    p = int(departure / lowest)
    q = (p + 1) * lowest
    return abs(q - departure) * lowest

def gcd(a, b):
    print(a, b)
    while b:
        a, b = b, a % b
        print(a, b)
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def earliest(timetable):
    buses = []
    for i, bus in enumerate(timetable):
        if bus.isdigit():
            buses.append((int(bus), i))
    
    i, di = 0, 1
    count = 0
    while True:
        t = i
        if len(buses) == count:
            return t

        found = list(filter(lambda bus: (t + bus[1]) % bus[0] == 0, buses))
        if len(found) > count:
            i = t
            di = reduce(lcm, map(lambda bus: bus[0], found))
            count = len(found)
            continue  
        i += di

if __name__ == '__main__':
    departure = 0
    timetable = []
    with open('input') as file:
        lines = file.readlines()
        departure = int(lines[0].strip())
        timetable = list(map(lambda x: x.strip(), lines[1].split(',')))

    # buses = list(map(int, filter(lambda x: x.isdigit(), timetable)))
    # print(nearest(departure, buses))
    print(earliest(timetable))

    