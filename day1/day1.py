#!/usr/bin/python3


def day1_part1(data):

    result = []
    total = 0
    for count in data:
        if count == '':
            result.append(total)
            total = 0
            continue
        total += int(count)
    return result

def day1_part2(data):

    data = sorted(data, reverse=True)
    return sum(data[:3])


if __name__ == "__main__":
    day1_data = open('input.txt', 'r').read().split('\n')
    day1_part1_result = day1_part1(day1_data)
    print(max(day1_part1_result))

    day1_part2 = day1_part2(day1_part1_result)
    print(day1_part2)
    

