f=open('Runs.txt','r')
players_n=int(f.readline())
i=1
while i <=players_n:
    matches_n=int(f.readline())
    j=1
    scoresum=0
    maxscore=0
    while j <=matches_n:
        score=int(f.readline())
        scoresum=scoresum+score
        if score >maxscore:
            maxscore=score
        if j==1:
            m1=score
        if j==2:
            m2=score
        if j==3:
            m3=score
        j = j + 1
        print(f'PLAYER{i} {m1} {m2} {m3} AVERAGE:{averagescore} Maxscore:{maxscore}')
    averagescore=scoresum//matches_n
    i=i+1
   




