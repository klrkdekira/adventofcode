import re

def to_dict(s):
    items = s.split()
    d = {}
    for item in items:
        key, value = item.split(':')
        d[key] = value
    return d

REQUIRED = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
REQUIRED_COUNT = len(REQUIRED)

def validate(item):
    found = 0
    for key in item.keys():
        if key in REQUIRED:
            found += 1
    return found == REQUIRED_COUNT

def validate_field(item):
    key, value = item
    if key == 'byr':
        return int(value) >= 1920 and 2002 >= int(value)
    elif key == 'iyr':
        return int(value) >= 2010 and 2020 >= int(value)
    elif key == 'eyr':
        return int(value) >= 2020 and 2030 >= int(value)
    elif key == 'hgt':
        height, unit = re.findall('(\d+)(\w+)', value)[0]
        height = int(height)
        if unit == 'cm':
            return height >= 150 and height <= 193
        elif unit == 'in':
            return height >= 59 and height <= 76
    elif key == 'hcl':
        return re.match('^#[a-f0-9]{6}$', value) != None
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return re.match('^\d{9}$', value) != None
    elif key == 'cid':
        return True
    return False

if __name__ == '__main__':
    with open('input') as file:
        batch = []
        passport = {}
        for row in file:
            row = row.strip()
            if not row:
                batch.append(passport)
                passport = {}
                continue
            passport.update(to_dict(row))
        batch.append(passport)

        first = list(filter(validate, batch))
        print(len(first))
        second = list(filter(lambda x: all(map(validate_field, x.items())), first))
        print(len(second))
