# Report


#####1. For each of the specified types, what are some variations that your program can cover? 

1. Basic number: 
	a. Natural Numbers in the form of (xxx,xxx,xxx)
	b. Natural Numbers in the form of (xxxxxxx)
	
2. Dates and time:
	a. Date in the form is (Month , Day , Year)
	b. Date in the form is (Year , Month , Day)
	c. Date in the form is (Day , Month , Year)
	b. Date in the form of the example (1999-3-20)
	e. Time in the form of the example (6:30)
	f. Time in the form of the example (18:30)
	g. Date in the form of the example (Friday-the-13th)

3. Dollar amount( the biggest number can take is 999 million)
	a. Amount in the form of $ 45 or $ 45.4
	c. Amount in the form of $ 4.56 %

4. Percentages:
	a. Percentages in the form such as 45 % or 45.5 %
	b. Percentages in the form such as % 45 or % 45.5
	

5. Fractions: 
	a. Fractions in the form such as 9\/10
	b. Fractions in the form such as 3 9\/10
	c. Fractions in the form such as 456\/1987 

6. Duration and time:
	a. The form such as 1990-2000
	b. The form such as 1980-89
	c. The form such as 1990s-2000s
	d. The form such as '30s
	e. The form such as 9-10:30
	f. The form such as 20s (age)

7. Word with preffix or suffix:
	a. The form such pre-2000
	b. The form such 30-years-old
	c. The form such 3 1\/2-year

#####2. What was your strategy for identifying variations, given that the input file is too large for you to read every sentence? 
	Answer: I use regular expressions and rules. 
			For regular expression part, the regular expression will capture the general form of a specific type(such as date,fractions,duration...). For example, the word pre-2000, it is the word with prefix. The general form will be "[alphalbets]-[number]" . My regualr expression will capture any word that has this general without knowing each variation. Even though the input file is too large to read line by line, it is still possible to many variations converted.
	Therefore, because no matter variations the form of numbers could be, I suppose the form of number will fall into one of the below catogries(of course, there may be more forms of number in english. But here we just use the common forms):
	
		a. Fraction
		b. Interger
		c. Decimals
		d. Ordinal numbers
	
	After translating the essential part, my program will examine the translation based on some rules that we commonly use in english. For some examples:
		Rule 1. Fraction `one over two` is writen as `a half`
		Rule 2. Time '30s(or other number) is written as 30 century
		
	And so on...
	
	To be more specific, the regular expressions and rules are all coded in the program. One can go check to get more information.  


#####3. Were there difficult cases that your program cannot correctly handle using regular expression matching?  If so, what additional tools do you think might be needed? 
	Answer: Yes. For example my program cannot correctly handle the fraction (100\/200)\/(300\/400) (or we can say recursion of fraction) by using regular expression. In order to solve this problem, I might need tools that can interprete context free language, because context free language can recognize the endless embedded recursive expression, which regular expression cannot.



