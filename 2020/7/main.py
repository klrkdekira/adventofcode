def color(list):
    return ' '.join(list[:2])

def bag_capacity(item):
    list = item.strip().split()
    return (color(list[1:]), int(list[0]))

def parse(item):
    bag, contains = item.split('contain')

    if 'no other' in contains:
        return (bag, [])

    bag = color(bag.split())
    return (bag, dict(map(bag_capacity, contains.split(','))))

def lookup(rules, rule, colour):
    bags = rules.get(rule)
    if not bags:
        return False

    if colour in bags:
        return True

    for bag in bags:
        if bag == colour:
            return True
        if lookup(rules, bag, colour):
            return True
    return False

def traverse(rules, colour):
    bags = rules.get(colour)
    if not bags:
        return 0

    count = 0
    for bag in bags:
        count += bags[bag] + bags[bag] * traverse(rules, bag)
    return count

if __name__ == '__main__':
    with open('input') as file:
        rows = map(lambda x: x.strip(), file)
        rules = dict(map(parse, rows))
        print(len(list(filter(lambda x: lookup(rules, x, 'shiny gold'), rules))))
        print(traverse(rules, 'shiny gold'))
