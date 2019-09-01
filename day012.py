S="Please, I want {} sandwishes and {} donutes "
replace=S.replace("I","we")
print(replace)

x=5
y=7
print(S.format(x,y))

replaceA=S.replace("a","A")
print(replaceA)

import re


new_string = re.sub(r'a', 'A', S)
print(new_string)