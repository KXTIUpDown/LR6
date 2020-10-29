key = input("Введите ключ: ")
f = open('txt.txt', encoding='utf-8')
text = f.readline()
table = [{}]
cursor = 0
for symbol in text:
	if cursor >= len(key):
		table.append({})
		cursor = 0
	digit = key[cursor]
	table[-1][symbol] =(int(digit))
	cursor += 1

result = ""

for block in table:
	keys = list(block.keys())
	values = list(block.values())
	for value in values:
		result += keys[value - 1]
f.close()
f=open('answer', 'w')
f.write("".join(result))
f.close()

