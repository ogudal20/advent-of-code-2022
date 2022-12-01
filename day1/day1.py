#!/usr/bin/python3


def day1(data):

    result = []
    total = 0
    for count in day1_data:
        if count == '':
            result.append(total)
            total = 0
            continue
        total += int(count)
    return max(result)

if __name__ == "__main__":
    day1_data = open('input.txt', 'r').read().split('\n')
    day1_result = day1(day1_data)
    print(day1_result)


    

