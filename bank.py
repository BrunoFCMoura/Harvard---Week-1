def main():
    answer = input('Greeting: ')
    if answer == "How you doing?":
        print('$20')
    elif answer == "What's happening?" or answer == "What's up?":
        print('$100')
    else:
        print('$0')

main()
