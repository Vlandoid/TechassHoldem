import random

SUIT_DIAMONDS = 1
SUIT_HEARTS = 2
SUIT_CLUBS = 3
SUIT_SPADES = 4
HANDS_AMOUNT=1;
SUIT_AMOUNT = 4
FIRST_CARD_VALUE= 2
LAST_CARD_VALUE = 14
card_deck=[]
first_table_card=0
hand=[]
street_string=''
hand_string=''
for j in range(1,SUIT_AMOUNT+1,1):
	for i in range (FIRST_CARD_VALUE,LAST_CARD_VALUE+1,1):
			if (i<=10):

				card_deck = card_deck + [[str(i),str(j)]]
			else:
				if (i == 11):# Jack
					card_deck = card_deck + [[str(i),str(j)]]
				elif (i == 12):	# Queen
					card_deck = card_deck + [[str(i),str(j)]]
				elif (i ==13):	# King
					card_deck = card_deck + [[str(i),str(j)]]
				elif (i == 14):	# Ace
					card_deck = card_deck + [[str(i),str(j)]]
random.shuffle(card_deck)

# HandsAmount= int(input())
# Diamonds (Бубы / Алмазы)	
# Hearts (Черви / Сердца)
# Clubs (Трефы / Клубы)
# Spades (Пики / Лопаты)
# Ace (Туз)
# Jack (Валет / Джек)
# Queen (Дама / Королева(
# King (Король)



print(card_deck) # some debugshit

for i in range(1,HANDS_AMOUNT*2,2):
	hand = [card_deck[i-1],card_deck[i]]
	first_table_card=i
print('Your hand:',hand[0],'|',hand[1])

print("-" * 24)
print('Your hand')
print("-" * 24)
for i in range(-1,1,1):# потомушто нипалучается вызвать цикл нормально
	if int(hand[i][1]) == SUIT_DIAMONDS:
		if (int(hand[i][0]) == 11):		# Jack
			hand_string=('| Jack of Diamonds ♦')

		elif (int(hand[i][0]) == 12):	# Queen
			hand_string=('| Queen of Diamonds ♦')

		elif (int(hand[i][0]) ==13):	# King
			hand_string=('| King of Diamonds ♦')

		elif (int(hand[i][0]) == 14):	# Ace
			hand_string=('| Ace of Diamonds ♦')

		else:			
			hand_string=('| '+hand[i][0]+ ' of Diamonds ♦')

	elif int(hand[i][1]) == SUIT_HEARTS:
		if (int(hand[i][0]) == 11):		# Jack
			hand_string=('| Jack of Hearts ♥')

		elif (int(hand[i][0]) == 12):	# Queen
			hand_string=('| Queen of Hearts ♥')

		elif (int(hand[i][0]) ==13):	# King
			hand_string=('| King of Hearts ♥')

		elif (int(hand[i][0]) == 14):	# Ace
			hand_string=('| Ace of Hearts ♥')

		else:			
			hand_string=('| '+hand[i][0]+ ' of Hearts ♥')

	elif int(hand[i][1]) == SUIT_CLUBS:
		if (int(hand[i][0]) == 11):		# Jack
			hand_string=('| Jack of Clubs ♣')

		elif (int(hand[i][0]) == 12):	# Queen
			hand_string=('| Queen of Clubs ♣')

		elif (int(hand[i][0]) ==13):	# King
			hand_string=('| King of Clubs ♣')

		elif (int(hand[i][0]) == 14):	# Ace
			hand_string=('| Ace of Clubs ♣')

		else:
			hand_string=('| '+hand[i][0]+ ' of Clubs ♣')

	elif int(hand[i][1]) == SUIT_SPADES:
		
		if (int(hand[i][0]) == 11):		# Jack
			hand_string=('| Jack of Spades ♠')
		elif (int(hand[i][0]) == 12):	# Queen
			hand_string=('| Queen of Spades ♠')
		elif (int(hand[i][0]) ==13):	# King
			hand_string=('| King of Spades ♠')
		elif (int(hand[i][0]) == 14):	# Ace
			hand_string=('| Ace of Spades ♠')
		else:
			hand_string=('| '+hand[i][0]+ ' of Spades ♠')
	result = (hand_string+"               ")[:22]
	result = result +' |'
	print(result)

print("-" * 24)
print('Table')
print("-" * 24)
for i in range(first_table_card,first_table_card+5,1):
	if int(card_deck[i][1]) == SUIT_DIAMONDS:
		if (int(card_deck[i][0]) == 11):		# Jack
			street_string=('| Jack of Diamonds ♦')
		elif (int(card_deck[i][0]) == 12):	# Queen
			street_string=('| Queen of Diamonds ♦')
		elif (int(card_deck[i][0]) ==13):	# King
			street_string=('| King of Diamonds ♦')
		elif (int(card_deck[i][0]) == 14):	# Ace
			street_string=('| Ace of Diamonds ♦')
		else:
			street_string =('| '+card_deck[i][0]+ ' of Diamonds ♦')

	elif int(card_deck[i][1]) == SUIT_HEARTS:
		if (int(card_deck[i][0]) == 11):		# Jack
			street_string=('| Jack of Hearts ♥')
		elif (int(card_deck[i][0]) == 12):	# Queen
			street_string=('| Queen of Hearts ♥')
		elif (int(card_deck[i][0]) ==13):	# King
			street_string=('| King of Hearts ♥')
		elif (int(card_deck[i][0]) == 14):	# Ace
			street_string=('| Ace of Hearts ♥')
		else:
			street_string =('| '+card_deck[i][0]+ ' of Hearts ♥')

	elif int(card_deck[i][1]) == SUIT_CLUBS:
		if (int(card_deck[i][0]) == 11):		# Jack
			street_string=('| Jack of Clubs ♣')
		elif (int(card_deck[i][0]) == 12):	# Queen
			street_string=('| Queen of Clubs ♣')
		elif (int(card_deck[i][0]) ==13):	# King
			street_string=('| King of Clubs ♣')
		elif (int(card_deck[i][0]) == 14):	# Ace
			street_string=('| Ace of Clubs ♣')
		else:
			street_string =('| '+card_deck[i][0]+ ' of Clubs ♣')

	elif int(card_deck[i][1]) == SUIT_SPADES:
		if (int(card_deck[i][0]) == 11):		# Jack
			street_string=('| Jack of Spades ♠')
		elif (int(card_deck[i][0]) == 12):	# Queen
			street_string=('| Queen of Spades ♠')
		elif (int(card_deck[i][0]) ==13):	# King
			street_string=('| King of Spades ♠')
		elif (int(card_deck[i][0]) == 14):	# Ace
			street_string=('| Ace of Spades ♠')
		else:
			street_string =('| '+card_deck[i][0]+ ' of Spades ♠')

	result = (street_string+"               ")[:22]
	result = result +' |'
	print(result)

print("-" * 24)




