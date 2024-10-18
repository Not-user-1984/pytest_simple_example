# print('Enter some numbers in one line')
# raw_input = input()
# splitted_input = raw_input.split()
# parsed_input = list()
# for raw in splitted_input:
#     parsed_input.append(int(raw))
#     parsed_input.sort()
# print(f'if your result: {parsed_input}')

def sort_numbers(input_string):
    splitted_input = input_string.split()
    parsed_input = [float(raw) for raw in splitted_input]
    parsed_input.sort()
    return parsed_input


if __name__ == "__main__":
    print('Enter some numbers in one line')
    raw_input = input()
    result = sort_numbers(raw_input)
    print(f'Your sorted result: {result}')
