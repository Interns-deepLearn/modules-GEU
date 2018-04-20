word= ''
word = word.lower()
if (len(word) > 0 and word.isalpha()):
 if(word == 'a' or word ==  'e' or word == 'i' or word == 'o' or word == 'u'): 
   print 'vowel'
 else:
   print 'Consonant'
else: 
 print 'empty'

