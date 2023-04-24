import random

X_prime = ['0000000', '1000110', '0100101', '0010011', '0001111', '1100011', '1010101', '1001001', '0110110', '0101010', '0011100', '1110000', '1101100', '1011010', '0111001', '1111111']

#Useful funcion
def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def complement(s):
	c = ''
	for char in s:
		c += '0' if char == '1' else '1'
	return c

#Tasks
def task2():
	b = []
	d = ['000', '001', '010', '100', '101', '100', '110', '111', '011']
	for message in d:
		b = []
		for codeword in X_prime:
			if codeword.startswith('0'+message):
				b.append(codeword)
				b.append(complement(codeword))
		print("Le codeword associate ad " + str(message) + " sono: " + str(b[0]) + ' e ' + str(b[1]))
		choice = random.randint(0, 1)
		print('La codeword associata ad ' + str(message) + " è: " + str(b[choice]))

def task3(y):
	x = X_prime[0]
	for word in X_prime[1:]:
		if hamming_distance(word, y) < hamming_distance(x, y):
			x = word
	if x.startswith('1'):
		x = complement(word)
	print('Il messaggio associato alla codeword ' + y + ' è ' + x[1:4])

def main():
	task2()
	for codeword in X_prime:
		task3(codeword)


if __name__ == "__main__":
	main()
