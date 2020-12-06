QUESTIONS = ['a', 'b', 'c', 'x', 'y', 'z']

def anyone(group):
    answers = []
    for person in group:
        answers.extend(person)
    return len(set(answers))

def everyone(group):
    answers = set.intersection(*(set(person) for person in group))
    return len(answers)

if __name__ == '__main__':
    with open('input') as file:
        groups = []
        group = []
        for row in file:
            row = row.strip()
            if not row:
                groups.append(group)
                group = []
                continue
            group.append(row)
        groups.append(group)

        print(sum(map(anyone, groups)))
        print(sum(map(everyone, groups)))
