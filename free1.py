import re
import requests
import json


def checker(alpha):                         # checks if a word contains digits
    for a in alpha:
        if a.isdigit():
            return False
    return True


name1= raw_input("Enter name of file to be read: ")
handle_read= open(name1, 'r')
multiple=[]


for line in handle_read:
    words=re.findall(ur"[\w\d']+",line)     # arrange alphanumeric words into a list removing punctuation
    words=filter(lambda a:checker(a),words) # remove words containing digits
    multiple+=words
filtered_list= list(set(multiple))          # remove multiple occurances from list
print filtered_list

# --------------------------------------------------------------

name2= raw_input("Enter name of file to be written: ")
handle_write= open(name2,"w")
for a in filtered_list:
    params={'sl':a}
    r= requests.request('GET',"http://api.datamuse.com/words", params=params)
    parsed_json=json.loads(r.text)
    for entry in parsed_json:
        if entry["score"]>90:
            handle_write.write(str(entry))
    handle_write.write("\n\n\n")

print "Done!"
#--------------------------------------------------------------
