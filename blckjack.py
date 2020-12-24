k = input()

card = k.split()

card.sort()


for i in range(len(card)) :
    if (card[i] == 'A'):
        card.insert(0,(card.pop(i)))
    elif (card[i] == 'K'):
        card.insert(len(card),(card.pop(i)))

print(*card)