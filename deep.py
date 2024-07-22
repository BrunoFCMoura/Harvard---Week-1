def main():
    answer = input('What is the answer to the Great Question of Life, the universe and everything? ')

    if answer.strip() == '42' or answer.lower().strip() == 'forty-two' or answer.lower().strip() == 'forty two':
        print('Yes')
    else:
        print('No')

main()
