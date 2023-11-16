roundplayer1win = 0
roundplayer2win = 0
Countplayer1flase = 0
Countplayer2flase = 0
listsaveplayer1win = []
listsaveplayer2win = []
while True:
    n,k = -1, 0
    while n < k:
        print("Enter n > k: ")
        print("Enter n: ", end = "")
        n = int(input())
        print("Enter k: ", end = "")
        k = int(input())
    cnt = 0
    while n > 1:
        print("One player enter:")
        x1 = 0
        cnt1 = 0
        while x1 < 1 or x1 > min(n, k):
            print("Enter a number in the range(1, min({}, {})): ".format(n , k) , end = "")
            x1 = int(input())
            cnt1 += 1
        Countplayer1flase += cnt1
        cnt1 = 0
        n -= x1
        cnt += 1
        if n < 1 : break
        print("Two player enter:")
        x2 = 0
        cnt2 = 0
        while x2 < 1 or x2 > min(n, k):
            print("Enter a number in the range(1, min({}, {})): ".format(n , k) , end = "")
            x2 = int(input())
            cnt2 += 1
        Countplayer2flase += cnt2
        cnt2 = 0
        n -= x2
        cnt += 1
    
    if cnt % 2 == 0: 
        roundplayer2win += 1
        listsaveplayer2win.append(roundplayer2win)
    else: 
        roundplayer1win += 1
        listsaveplayer1win.append(roundplayer1win)

    print("Do you want to play the game again? (YES/NO):", end = "")
    if input().upper() == "YES":
        continue
    else: break

if(roundplayer1win > roundplayer2win):
    print("Player 1 wins")
    print("Number round player 1 wins: ", end = "")
    print(listsaveplayer1win)
elif(roundplayer2win > roundplayer1win):
    print("Player 2 wins")
    print("Number round player 2 wins: ", end = "")
    print(listsaveplayer2win)
elif(roundplayer1win == roundplayer2win and Countplayer1flase > Countplayer2flase):
    print("Player 1 wins")
    print("Number round player 1 wins: ", end = "")
    print(listsaveplayer1win)
elif(roundplayer1win == roundplayer2win and Countplayer2flase > Countplayer1flase):
    print("Player 2 wins")
    print("Number round player 2 wins: ", end = "")
    print(listsaveplayer2win)
else:
    print("Draw")
    print("Number round player 1 wins: ", end = "")
    print(listsaveplayer1win)
    print("Number round player 2 wins: ", end = "")
    print(listsaveplayer2win) 