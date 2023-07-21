def hangman(count):
    a=' +---------+'
    b='       |   |'  
    c='       O   |'
    list=['           |','       |   |',"      /|   |","      /|\  |",'      /    |','      / \  |']
    print(f'{a}\n{b}\n{c}\n',end='')
    if count<=3:
        print(f'{list[count]}\n',end='')
        print('           |' )
        print('           |')
        print('===============')
    elif count==4:
        print(f'{list[3]}\n',end='')
        print(f'{list[4]}\n',end='')
        print('           |')
        print('===============')
    else:
        print(f'{list[3]}\n',end='')
        print(f'{list[5]}\n',end='')
        print('===============')
import random
import sys
def main():
    list_of_words=['apple','orange','computer','school']
    word=random.choice(list_of_words)
    length=len(word)
    spaces= ['-']*length
    print(spaces)
    count=0
    life=5
    while count<=5:
        if count==5:
            hangman(count)
            print(f'SORRY! YOU LOOSE.The word was "{word.upper()}"')
            sys.exit()
        else:
            hangman(count)
        if word==(''.join(spaces)):
            print(f'Congratulations YOU WIN!. The word was "{word}" ')
            break
        else:
            alpha=input(f'Guess alphabets to complete word(you can make only 5 miistakes):')
            if alpha not in word:
                count+=1
                if count!=5:
                    print(f"YOU ARE LEFT WITH {life-count} lives")
            if alpha in word:
                if word.count(alpha)==spaces.count(alpha):
                    count+=1
                else:
                    for j in range(length):
                        if alpha==word[j] and spaces[j]!=alpha:
                            spaces[j]=alpha
                            break
            print(spaces)
main()