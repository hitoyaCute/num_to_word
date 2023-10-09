def num_to_word(number):
	"""will convert number to word
	on this ver suport upto 999,999,999,999,999"""
	if 0 >= number > int("9"*15):
		raise (f"ValueError:the input must not larger than {int('9'*15)} ")
	if number == 0:
		return "zero"
	user,output = int(number),""
	words = ("",'One','Two','Three','Four','Five','Six','Seven',
					 'Eight','Nine','Ten','Eleven','Twelve','Thirteen',
					 'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen',
					 'Nineteen','Twenty','Thirty','Forty','Fifty','Sixty',
					 'Seventy','Eighty','Ninety',"thousand","milion",
					 "bilion","trilion")
	f,c = len(str(user)), 0
	while f > 3:
		f ,c = f-3, c+1
	f = c
	del c,number
	while user != 0:
		msn = 10**(len(str(user))-1)
		cnos = nos = (user//msn)*msn
		Nnum = user//(10**(len(str(user))-1))
		while cnos > 1000:
			cnos /= 1000
		cnos = int(cnos)
		if cnos >= 100:
			output += words[Nnum] + " hundred "
		if 100 > cnos > 19:
			output += words[Nnum+18] + " "
		if cnos < 20:
			output += words[int(str(user)[:2])] + " " if len(str(cnos)) == 2 else words[Nnum] +" "
			output += words[f+27] + " " if f != 0 else ""
			f -= 1 if cnos <10 else 0
		user -= int(str(user)[:2]) if nos < 20 else nos
	return output
if __name__ == "__main__":
	while True:
		num = input()
		if num == "exit" or str(num).isalpha():
			break
		print(num_to_word(int(num)))