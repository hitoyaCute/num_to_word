#the final was at the bottom 
def num_to_word1(number: int):

#	if not (0 > number > int("9"*15)):
#		import inspect
#		a = inspect.stack()[1]
#		raise ValueError(f"{a.funtion} on line {a.lineno}:Value must be inside the range 0 to {'9'*15}")

	f,c = len(str(number)),0
	while f > 3:f,c = f-3,c+1
	f,output = c,""
	del c
	
	word = ("",'One','Two','Three','Four','Five','Six','Seven',
					 'Eight','Nine','Ten','Eleven','Twelve','Thirteen',
					 'Fourteen','Fifteen','Sixteen','Seventeen','Eighteen',
					 'Nineteen','Twenty','Thirty','Forty','Fifty','Sixty',
					 'Seventy','Eighty','Ninety', "","thousand", "million", 
					 "billion", "trillion", "quadrillion", "quintillion", 
					 "sextillion", "septillion", "octillion", "nonillion", 
					 "decillion", "undecillion", "duodecillion", "tredecillion")
	
	while number != 0:
		num = number
		print("B:",str(num)[0])
		msn = int(str(num)[0])
		while num > 1000:
			num/=1000
		print(num)
		num = cnum = int(num)
		if num > 99:
			output += word[msn] + " hundred "
#			mun -= msn*100
		if 19 < num < 100:
			output += word[msn+19] + " "
		if num < 20:
			output += word[num]
			output += word[f+27]
			f-1
			
		
					 


		number = int(str(number)[1:]).strip()
	return output
if __name__ == "__m ain__":
	print(num_to_word(86000017981017))


	number -= int(str(msn)+("000"*f))
	num = 9370
	num = list(str(num))
	num.pop(0)

	print("".join(num))




#get the largest num using the int(str(number)[1]) => msn
#get the number inside the hundred range like from 8769014 -> 86 => num
#read how manny gruop of 3 number behind the num like from 82081819000891
# 82  017 819 000 891
# num  1   2   3   4   => f
#.........summary of variables.......
# msn -> most significant number
# num -> the largest group of hundreds
# f tell how manny the group of 3 zero in back will be


#this how must it work
#first get the data of the number
#91890098--------->number
#^---------------->msn
#91890098
#└┘└─┘└─┘
#x  1  2---------->f
#91890098
#└┘--------------->num
#check if what group num is like
#gruop >99 , gruop from 19 to 99 and gruop les than 20
#repeat and subtract till number became 0
num = number = 86000017981017
def num_to_word2(number):
	if number == 0:
		return "zero"
		
	if not(0 < number < int("9"*(45))):
		import inspect
		a = inspect.stack()[1]
		raise ValueError(f"{a.funtion} on line {a.lineno}:Value must be inside the range 0 to {'9'*45}")

	f,output = 0,""

	word = ("",'One','Two','Three','Four','Five','Six','Seven',
'Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen',
'Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty',
'Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety',
"","thousand", "million","billion", "trillion", "quadrillion",
"quintillion","sextillion", "septillion", "octillion", "nonillion",
"decillion", "undecillion", "duodecillion", "tredecillion")
#............86,000,017,981,017
	while number > 0:
		msn,num = int(str(number)[0]),number#8,86000017981017

		while num > 1000:num,c = num//1000,f+1#num = 86,f=4 
		cnum = num#86
		
		if num > 99:
			output += word[msn] + " hundred "
			num -= msn*100
		if 19 < num < 100:
			output += word[msn]
			num - msn*10#86-80 = 6
		if num < 20:
			output += word[num]
			output += word[f+27]
		f-1

		number = int(str(number)[len(str(cnum)):].strip())#86000017981017 86(2) ->17,981,017
	return output
if __name__ == "__m ain__":
	print(num_to_word(86000017981017))


#final lmao
#i just fix some bugs where i forgot that 1000919 where if we just simply 
#decrement the f it will register as 919000 so yeah
#i just reset the f each time
def num_to_word(number:int=None):
	if str(number).isalpha() or not(0 < number < int("9"*(45))):
		import inspect
		a = inspect.stack()[1]
		raise ValueError(f"{a.function} on line {a.lineno} Value must be inside the range 0 to {'9'*45}")
	if number == 0 or number == None:
		return "zero"
	if __name__ == "__main__":
		print(number)
	f,output = 0,""
	word = ("",'One ','Two ','Three ','Four ','Five ','Six ','Seven ',
'Eight ','Nine ','Ten ','Eleven ','Twelve ','Thirteen ','Fourteen ',
'Fifteen ','Sixteen ','Seventeen ','Eighteen ','Nineteen ','Twenty ',
'Thirty ','Forty ','Fifty ','Sixty ','Seventy ','Eighty ','Ninety ',
"","thousand ","million ","billion","trillion ","quadrillion ",
"quintillion ","sextillion ","septillion ","octillion ","nonillion ",
"decillion ","undecillion ","duodecillion ","tredecillion ")
	while number > 0:
		q = len(str(number))%3
		msn,num = [int(str(number)[i]) for i in (range(q) if q != 0 else range(3))],number
		del q
		while num > 1000:num,f = num//1000,f+1
		cnum = num
		if num > 99:
			output += word[msn[-3]] + " hundred "
			num -= msn[-3]*100
		if 19 < num < 100:
			output += word[msn[-2]+18]
			num -= msn[-2]*10
		if num < 20:
			output += word[num] if number > 1000 else "and "+word[num]
			output += word[f+28]
		number,f = int(str(number)[len(str(cnum)):]) if number > 19 else 0,0
	return output
if __name__ == "__main__":
	print(num_to_word(86000017981017))
	print(num_to_word())
	print(num_to_word("h"))