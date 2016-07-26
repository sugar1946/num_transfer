'''
Created on Jan 17, 2016

@author: Mingzhi Yu
'''

import sys,io,re

'''
Attributes-------------------------------------------

'''

PREFIX_SUFFIX = ("pre","post","'")
FRAC_DICT = {1:"first",
                 2:"second",
                 3:"third",
                 4:"forth",
                 5:"fifth",
                 6:"sixth",
                 7:"seventh",
                 8:"eighth",
                 9:"ninth",
                 10:"tenth",
                 11:"eleventh",
                 12:"twelfth",
                 13:"thirteenth",
                 14:"fourteenth",
                 15:"fifteen",
                 16:"sixteenth",
                 17:"eventeenth",
                 18:"eighteenth",
                 19:"nineteenth",
                 20:"twentieth",
                 30:"thirtieth",
                 40:"fourtieth",
                 50:"fiftieth",
                 60:"sixtieth",
                 70:"seventieth",
                 80:"eightieth",
                 90:"nintieth",
                 100:"hundredth",
                 1000:"thousandth"
        
                 }


def main(argv):
    '''
    Read file by lines, do converting and then write line
    back to the file
    '''
    
    print "Got file = ", argv
    ro = open(argv,"r+")
    wo = open("output.txt","w+")
    print "Name of the file: ",ro.name
    writeText = ""

    
    #line = ro.readline()
    #print "Read line", line
    for line in ro:
        wordsList = line.split()
    #print wordsList
        sentence = "";
        for i in range(len(wordsList)):
            if '$' in wordsList[i]:
                wordsList[i] = "$"+ wordsList[i+1]
                wordsList[i+1] =""
            if re.match('\$?[0-9]+,[0-9]+(,[0-9]+)*',wordsList[i]):
                wordsList[i] = wordsList[i].replace(',','')
            
                
            if ('\/' in wordsList[i]):
                if (re.match('[0-9]+',wordsList[i-1])):
                    wordsList[i] = "a" + wordsList[i] # a is a flag means add 'and'
                    print "The fraction is added with an 'and': " + wordsList[i]
        
        print wordsList
        for word in wordsList:
            if word is not '':            
                word = convert(word)
                sentence = sentence + word + " "

            # Hack here for checking if I have "dollar millions"....
        sentence = sentence.split()
        if 'dollars' in sentence:
            i = sentence.index('dollars')
            if i + 1 < len(sentence):
                print sentence[i + 1]
                if sentence[i + 1] == 'million':
                    sentence[i + 1] = 'dollars'
                    sentence[i] = 'million'

        newSentence = " "
        for word in sentence:
            newSentence = newSentence + word + " "
                                          
        print "The converted line is: ", sentence
        writeText = writeText + newSentence +"\n"
    wo.write(writeText)
    wo.close()
    ro.close()
    

def convert(word):
    '''
    search if a word is in certain pattern and if it is,
    we convert it.
    '''

    #example for each re. $99.99s, %, a7/8, 1990-1991(30s-40s),30-years-old
    #                     pre-1999

    patterns = ['^\$?[0-9]+(\.([0-9]+))?[s]?$','[%]','^[a]?[0-9]*\\\/[1-9]*$',
                '[0-9]+[-][0-9]+','[a-zA-Z]+[-]([0-9]+)|([0-9]+)[-][a-zA-Z]+',
                '[0-9]+[:][0-5][0-9]','\'[0-9]{2}[s]']
    translation = ""

    for pattern in patterns:
        print 'Looking for "%s" in "%s" ->' % (pattern, word)
        if re.search(pattern,word):
            print "Match!! the word " + word + " matchs the pattern " + pattern
            dollarflag = False
            yearflag = False
            centuryflag = False
            ageflag = False
            

            if re.match('[0-9]+[:][0-5][0-9]$',word):
                translation = timeToEnglish(word)
                return translation

            if re.search('^\'?[0-9]{2}[s]$',word):
                if '\'' in word:
                    word = word.replace('\'','')
                    word = word.replace('s','')
                    translation = "nineteen " + numToEnglish(int(word))
                else:
                    word = word.replace('s','')
                    translation = FRAC_DICT[int(word)]
                return translation
                
                

            if re.search('[0-9]+[s]',word):
 
                if re.search('^[0-9]{4}[s]',word):
                     centuryflag = True
                word = word.replace('s','')


                       

            if '\/' in word:
                parts = word.split('-')
                for x in parts:
                    if '\/' in x:
                        x = fracToEnglish(x)
                    translation = translation + " " + x                
                return translation

            #e.g. 30-years-old, 30-days,pre-1999,post-1999,Friday-the-13th
            if re.search(patterns[4],word):
                word = word.replace('-',' ')
                parts = word.split()
                nounce = False
                
                for x in parts:
                    print x
                       
                    if re.match('[0-9]+',x):
                        
                        prefix,suffix = "",""
                        
                        if parts.index(x) + 1 < len(parts) :
                            suffix = parts[parts.index(x) + 1]
                            print "suffix is: " + suffix
                        
                        if parts.index(x) - 1 >= 0 :
                            prefix = parts[parts.index(x) - 1]
                            print "preffix is: " + prefix
                            
                        if re.match('[A-Z]',prefix):
                            nounce = True
                            print nounce

                        if re.match('[A-Z]',suffix):
                            nounce = True
                            print nounce

                        if not nounce:
                            
                            if '.' in x:
                                x = deciToEnglish(x)


                            elif 'th' in x:
                                x = x.replace('th','')
                                x = FRAC_DICT[int(x)]
                            
                            else:
                                x = yearToEnglish(x)

                    translation = translation + x + ' '

                if centuryflag :
                    translation = translation + " century"
                return translation
                        

            # e.g. 1900-1990, 1900s-2000s, 1999-3-20,CF6-6,9-10:30
            if re.search(patterns[3],word):
                
                parts = word.split('-')

                for x in parts:
                    print x
                    if re.search('[A-Z]+',x):
                        return word
                    

                print "right now parts are: "
                print parts
                
                if len(parts) < 3:
                    
                    for x in parts:
                        
                        i = parts.index(x)
                        if ':' in x:
                            x = timeToEnglish(x)

                        elif ageflag:
                            x = ageToEnglish(x)
                        else:
                            x = yearToEnglish(x)


                        if i != len(parts)-1:   
                            translation = translation + x + ' to '
                        else:
                            translation = translation + x
                            
                                    

                else:
                    month = dateToEnglish(parts[1])
                    translation = yearToEnglish(parts[0]) + ' ' + month + ' ' + \
                                    yearToEnglish(parts[2])
                    
                if centuryflag:
                    translation = translation + " century"

                
                print "the translation of this num-num is: " + translation
                return translation
                

            if '%' in word:
                translation = 'percents'
                return translation
            
            if '$' in word:
		dollarflag = True
		word = word.replace('$','')

	    if '.' in word:
		intergerPart =int(word[:word.index('.')])
		floatPart = word[word.index('.')+1:]
		print "The floatPart of the word " + word + " is " + floatPart

		if dollarflag:
		    floatPart = numToEnglish(int(floatPart))
		    if (intergerPart == 0):
			translation = floatPart + ' cent '
		    else:
                        translation = numToEnglish(intergerPart) + ' dollars ' + floatPart + ' cents'

		else:
		    floatList = re.split('([0-9])',floatPart)
		    print floatList
		    for num in floatList:
			if num is not '':
			    num = numToEnglish(int(num))
			    print "this float num after translation is " + num + "\n"
			    translation = translation + " " + num 
		    translation = numToEnglish(intergerPart) + ' point' + translation         
	    else:
		if dollarflag:
		    translation = numToEnglish(int(word)) + ' dollars'
		else: 
		    translation = numToEnglish(int(word))

            return translation
            
                
        else:
            print "no match the parttern " + pattern

    return word


def ageToEnglish(word):
    word = word.replace('s','')
    translation = FRAC_DICT[int(word)]
    return translation

def timeToEnglish(word):
    words = word.split(':')
    if int(words[0]) == 0:
        words[0] = '12'
    hour = numToEnglish(int(words[0]))
    minutes = numToEnglish(int(words[1]))
    if minutes is 'zero':
        minutes =''
    translation = hour + ' ' + minutes
    return translation

def deciToEnglish(word):
    '''
    Input is fraction. Output is the word
    '''

    translation = ""
    intergerPart =int(word[:word.index('.')])
    floatPart = word[word.index('.')+1:]
    print "The floatPart of the word " + word + " is " + floatPart
    translation = numToEnglish(intergerPart) + " point " + numToEnglish(int(floatPart))
    return translation
    
def dateToEnglish(n):
    '''
    Input is date. Month here temparorily
    '''
    translation = ""
    MONTH_DICT = {1: "January", 2:"Febuary", 3: "March", 4: "April", 5:"May",
                  6: "June", 7: "July", 8: "August", 9: "September",
                  10: "October",  11: "November", 12: "Feburay"}

    translation = MONTH_DICT[int(n)] + " the"

    return translation
                


def yearToEnglish(n):
    '''
    Input is the time such as the year 1990, which is a 4-digits string
    Output will be like nineteen ninty, instead of one thousand and nine hundred
    and ninety
    '''

    translation = ""
    # 4-digits year
    print "yearToEnglish n: " + n
    if len(n) == 4:
        part_1 = int(n[:2])
        part_2 = int(n[2:])
        print part_2
    
        part_1 = numToEnglish(part_1)
        if int(part_2) != 0:
            part_2 = numToEnglish(part_2)
        else:
            part_2 = ""

        translation = part_1 + " " + part_2 

    else :
        translation = numToEnglish(int(n))

    return translation

    

def fracToEnglish(n):
    '''Translate fraction to Enlish.'''
    translation = ""
    print "this fraction that is needed to be translated is: " + n
    if 'a' in n:
        translation = "and "
        n = n.replace('a','')
    
 

    parts = n.split('\/')

    if int(parts[1]) == 2: #special case for 1/2
        translation = translation + "a half"
        

    #if the dominator is less than 10, then find the
    #translation in the FRAC_DICT. The elif is excluded
    elif int(parts[1]) <= 10:  #such as 7/8
        translation = translation + numToEnglish(int(parts[0])) #e.g. 7 in 7/8       
        translation = translation + " " + FRAC_DICT[int(parts[1])] #e.g. 8 in 7/8
        

    #if the dominator is larger than 10, then find the
    #translation in both FRAC_DICT and NUMBER_DICT
    else:
        translation = translation + numToEnglish(int(parts[0])) #e.g. 77 in 77/829
        translation = translation + " over " + numToEnglish(int(parts[1]))

    print "the translation is of this fraction is: " + translation
    return translation
    

def numToEnglish(n):
    '''
    Translate numbers to Enlish. The biggest number
    can be interpreted is 999,999,999
    '''
    translation = ""
    if (n == 0):
        translation = "zero"
        return translation

    else:
	million = divmod(n,1000000)
	thousand = divmod(million[1],1000)
	hundred = divmod(thousand[1],100)
	ten = divmod(hundred[1],10)
	one = ten[1]

	print 'the million of this number is "%i", thousand is "%i", hundred is "%i" \
the ten is "%i", the one is "%i" \n' %(million[0],thousand[0],hundred[0],ten[0],one)

	
	NUMBER_DICT = {
		1 : "one",
		2 : "two",
		3 : "three",
		4 : "four",
		5 : "five",
		6 : "six",
		7 : "seven",
		8 : "eight",
		9 : "nine",
		10 : "ten",
		11 : "eleven",
		12 : "twelve",
		13 : "thirteen",
		14 : "fourteen",
		15 : "fifteen",
		16 : "sixteen",
		17 : "seventeen",
		18 : "eighteen",
		19 : "nineteen",
		20 : "twenty",
		30 : "thirty",
		40 : "forty",
		50 : "fifty",
		60 : "sixty",
		70 : "seventy",
		80 : "eighty",
		90 : "ninety"
	}

	if million[0] is not 0:
                if million[0] > 9: #case for 999,999,999
                    translation = translation + numToEnglish(million[0]) + " million and "
                else:
                    translation = NUMBER_DICT[million[0]] + " million and "
		   
	if thousand[0] is not 0:
		if thousand[0] > 9:  #case for 999,999
			translation = translation + numToEnglish(thousand[0]) + " thousand and "
		else:    
			translation = translation + NUMBER_DICT[thousand[0]] + " thousand and "

	if hundred[0] is not 0:
		translation = translation + NUMBER_DICT[hundred[0]] + " hundred "

	if ten[0] is not 0:
            if ten[0] is 1:
		translation = translation + NUMBER_DICT[10 + one] 
		one = 0
	    else:
                translation = translation + NUMBER_DICT[(ten[0]*10)] + " "
                

	if one is not 0:
		translation = translation + NUMBER_DICT[one] 

	print "The translation of the number " + str(n) + " is: " + translation + "\n"
	return translation


if __name__ == '__main__':

    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print "Error. Giva a file."
