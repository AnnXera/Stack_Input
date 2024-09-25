def ask_user_stacks():
    try:
        return int(input('Enter how many stacks you want to enter: '))
    except ValueError:
        return ask_user_stacks()


stacks = []
result = ''
stacks_number = ask_user_stacks()

for number in range(stacks_number):
    stack_name = input(f'Enter stack #{number+1}: ')
    stacks.append(stack_name)

for index in range(len(stacks)):
    if len(stacks) == 1:
        result = 'stack of ' + stacks[0]
        print(f'You have {result}.')
    elif index == len(stacks)-1:
        result = result + 'and ' + stacks[index]
        print(f'You have stacks {result}.')
    else:
        result = result + stacks[index] + ', '

while stacks:
    ask_remove = input('Click R to remove an item: ')
    if ask_remove == 'R':
        if stacks:

            stacks.pop()
            result = ''

            for index in range(len(stacks)):
                if len(stacks) == 1:
                    result = stacks[0]
                elif index == len(stacks) - 1:
                    result = result + 'and ' + stacks[index]
                else:
                    result = result + stacks[index] + ', '

            if len(stacks) == 1:
                print(f'You have stack {result}.')
            elif stacks:
                print(f'You have stacks {result}.')
            else:
                print('You do not have any item left on your stack.')
