# Vanaf 30 terugtellen tot de raketlancering. Print elke tel en print de lancering.
# Print de uren van de dag. Voor de ochtend voeg je 'AM' toe. Voor de middag voeg je 'PM' toe
# Print alle even getallen tussen 20 en 50
# Vraag een dag van de week op (ma,di,wo,do,vr,za,zo) Print alle dagen tot aan de opgegeven dag.
# Herhaal een input() tot het resultaat daarvan gelijk is aan ‘quit’ Print het aantal iteraties per iteratie.
# Tel de cijfers vanaf 50 totdat hun gezamelijke som groter is dan 1000, print elk cijfer en de totale som per iteratie.


i = 30

while i <= 30:
	print(i)
	i = i - 1
	if i == 0:
		print("wooooooooo")
		break


i = 1

while i <=24:
	i = i + 1
	if i > 11:
		print('{} {}'.format(i, "pm"))
		if i == 24:
			break
	else:
		print('{} {}'.format(i, 'am'))




while i > 20 < 50:
	if i == 30 or 40:
		print("30")
		print("40")
		break

d = input("welke dag ")

test_list = ['ma', 'di', 'wo', 'do', 'vr', 'za', 'zo']
  
N = d

temp = test_list.index(N)
res = test_list[:temp]
  
print(str(res))


inpt = input("chars: ")

for character in inpt:
	print(character)

begin = 50
oth = []

for i in range(0,1000):
	lel = 50
	a = print(lel + 50 + i)
	if a > 1000:
		break
