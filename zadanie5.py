
def automat(n, k, cels, rule):
    rule_binary = f'{rule:08b}'
    generations = [cels]

    for _ in range(k):
        new_generation = calculate_new_generation(generations[-1], n, rule_binary)
        generations.append(new_generation)
        
    for i in generations:
        print(i)

def calculate_new_generation(current, length, rule):
        new_gen = '' 

        for i in range(length):
            left = current[i - 1] if i > 0 else '_'
            center = current[i]
            right = current[i + 1] if i < length - 1 else '_'

            new_gen += calculate_character_for_next_generation(left, center, right, rule)

        return new_gen

def calculate_character_for_next_generation(left, center, right, rule):
    triplet_as_binary = str(left + center + right).replace('_', '0').replace('*' , '1')

    index = int(triplet_as_binary, 2)

    if (rule[7 - index] == '1'):
        return '*'
    else:
        return '_'

automat(21, 10, '__________*__________', 90)
automat(21, 10, '__*_*_*___****_*__*__', 30)