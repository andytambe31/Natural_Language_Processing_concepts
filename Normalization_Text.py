# Text normalization is converting text to a more convenient form - standard form

# It involves the following steps

"""
1. Converting to lowercase
2. Removing numbers
3. Removing punctuations
4. Removing white spaces
5. Remove stop words
"""

# Step 0 - Importing relevant libraries
import re
import nltk

# Step 1 - Fetch the textual string
print('Step 1 - Fetch the textual string')
string = "       Python 3.0, released in 2008, was a major revision of the language that is not completely backward compatible and much Python 2 code does not run unmodified on Python 3. With Python 2's end-of-life, only Python 3.6.x[30] and later are supported, with older versions still supporting e.g. Windows 7 (and old installers not restricted to 64-bit Windows)."
print(string)

# Step 2 - Convert to lower case
lower_case = string.lower()

print('Step 2 - Convert to lower case')
print(lower_case)

# Step 3 - Remove numbers using regex
no_number_string = re.sub(r'\d+','',lower_case)
print('Step 3 - Remove numbers using regex')
print(no_number_string)

# Step 4 - Remove punctuations using regex
no_punc_string = re.sub(r'[^\w\s]','', no_number_string)
print('Step 4 - Remove punctuations using regex')
print(no_punc_string)

# Step 5 - Remove whitespaces using strip()
no_wspace_string = no_punc_string.strip()
print('Step 5 - Remove whitespaces')
print(no_wspace_string)

# Step 6 - Remove stop words

'''
We begin by importing a set of stop words for english language.
'''
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words("english"))
#print('Stop words for english - ')
#print(stop_words)

# convert string to list of words
lst_string = [no_wspace_string][0].split()

# remove stopwords
no_stpwords_string = ""
for i in lst_string:
    if not i in stop_words:
        no_stpwords_string += i + ' '

# removing last space
no_stpwords_string = no_stpwords_string[:-1]
print('Step 6 - Remove stop words-')
print(no_stpwords_string)



