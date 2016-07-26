# ReadMe
######Mingzhi Yu, MIT39@pitt.edu, 2016-1-24


## Overview

**Converter** takes a `text` file as input and convert all  expressions involving numbers, data, decimal numbers to their appropriate word forms. 
 
  

### Running instruction
	1. Go to the dir that contains the Convertor.py 
	2. Create your own input file under this dir (the default test file is input.txt)
	3. Type:
		python Convertor.py input.txt
	4. Convertor will create a text file "output.txt" as the translation result.
		

### Converage
1. Basic requirments: Basic numbers; Date; Dollar amounts; Percentages Fraction; (More details are mentioned in the report) 
2. Augmented portion:
	i. Expressions not under above categories:
		*	Century. For example: 
			a. 1990s -> nineteen ninty century
			b. 1900s-2000s -> nineteen to twenty century
		*   Date and time. For example:
			a. Friday-March-13th -> Friday the thirteen
			b. 12:30 -> twelve thirty
			c. 1999-3-21 -> nineteen ninety nine March twenty one
			d. '30s -> ninteen thirty
		*	Duration,For example: 
			a. 1990-2000 -> nineteen ninety to two thousand
			b. 1950-89 -> nineteen fifty to eighty nine			
			c. 9-10:30 -> nine to ten thrity
		*	Prefix combination,For example: 
			a. pre-1990 -> pre nineteen ninty
		*	Suffix combination,For example: 
			a. 30-days -> thirty days
		*	Comparision,For example:
			a. 1-to-1 -> one to one
		*	Age:
			a. 30s: thirty
	
	2. Combination of above catogories:
		*	example 1: $ 1,234.567
		*	example 2: $ 7\/8
		*	example 3: $ 0.35 %
		* 	example 4: 10 8\/7 % 
		
	
	3. Ambiguities: 
		*	case 1. Exlusive noun: `Craig-1999` and `pre-1990`. The first term might be the name of a company; however, the second term means before the year 1990. To solve this ambiguity, any word that does not belong to the default prefix(suffix) table will be interpreted as an exclusive nounce. The number adjacent to this exclusive nounce will be understood as a simple and will not be converted.
		
		* case 2. Exlusive noun: the terms `'82s Some Company name here` and `'30 to '40s`. The first term is an exclusive noun that is the name of some company contaning numbers and the second term means from the time 1930 to 1940, To solve the ambiguity, the program will look at the terms after and before numbers. If the words follow the numbers are some exclusive noun, then the term will be interpreted as a exclusive noun as a whole. If the words follow the numbers are number and also in certain parttern that means duration, then the term will be interpreted as a duration.

