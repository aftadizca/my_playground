import random

deposit = 1000_000
bet = 100_000
win_price = 0.8
lose_price = 1

win_percentage = 0.5

for i in range(10000):
    
    if deposit <= 0:
        print(str(i)+"x Transaksi anda kalah")
        break;

    if random.random() < win_percentage:
        deposit = (deposit - bet) + (bet* (1+win_price) )
    else:
        deposit = deposit - bet

print(deposit)