def main():
    answer = input('File Name: ').strip().lower()
    if answer.endswith('.gif'):
        media_type = 'image/gif'
    elif answer.endswith('.jpg') or answer.endswith('.jpeg'):
        media_type = 'image/jpeg'
    elif answer.endswith('.png'):
        media_type = 'image/png'
    elif answer.endswith('.pdf'):
        media_type = 'application/pdf'
    elif answer.endswith('.txt'):
        media_type = 'text/plain'
    elif answer.endswith('.zip'):
        media_type = 'application/zip'
    else:
        media_type = 'application/octet-stream'

    print(media_type)

main()
