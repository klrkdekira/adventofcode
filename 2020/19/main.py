def parse(line):
    id, rules = line.split(':')
    forks = []
    for rule in rules.strip().split('|'):
        rule = rule.replace('"', '')
        forks.append(list(rule.strip().split()))
    return (id, forks)
    
def match(rules, message):
    rule = rules['0'][0]
    return match_inside(rules, rule, message, 0)

def match_inside(rules, rule, message, position):
    if len(rule) > len(message[position:]):
        return False
    elif len(message[position:]) == 0 or len(rule) == 0:
        return len(message[position:]) == 0 and len(rule) == 0

    key, *rule = rule
    if key.isalpha():
        if message[position] == key:
            return match_inside(rules, rule, message, position + 1)
    else:
        for r in rules[key]:
            if match_inside(rules, r + rule, message, position):
                return True
    return False

if __name__ == '__main__':
    rules, messages = [], []
    with open('input') as file:
        separated = False
        for line in file:
            line = line.strip()
            if not line:
                separated = True
                continue

            if separated:
                messages.append(line)
            else:
                rules.append(line)

    rules = dict(map(parse, rules))
    
    print(sum([1 for msg in messages if match(rules, msg)]))

    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31",], ["42", "11", "31"]]
    print(sum([1 for msg in messages if match(rules, msg)]))
