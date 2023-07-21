def encypt(data,k):
    encrypted=''
    for i in data:
        a=ord(i)
        if 65<= a <=90:
            char= chr((a+k-65)%26 +65)
        elif 97<= a <= 122:
            char= chr((a+k-97)%26 +97)
        else:
            char= i
        encrypted+=char
    return encrypted
def decrypt(data,k):
    decrypted=''
    for i in data:
        a=ord((i))
        if 65<= a <=90:
            char= chr((a-k-65)%26 +65)
        elif 97<= a <= 122:
            char= chr((a-k-97)%26 +97)
        else:
            char= i
        decrypted+=char
    return decrypted
def main():
    task=input('WHAT YOU WANT TO DO? TYPE "encypt" for ENCYRPTION AND TYPE ""decrypt" for DECRYPTION:')
    data=input('ENTER YOUR DATA TO BE CONVERTED:')
    k=int(input('ENTER SHIFT KEY:'))
    if task=='encrypt':
        print(encypt(data,k))
    elif task=="decrypt":
        print(decrypt(data,k))
    next=input("DO YOU WANT TO CONTINUE ? TYPE YES OR NO!")
    if next=="YES":
        main()
    else:
        print("THANK YOU FOR USING OUR SERVICE")
main()