import operator
input1=input()
def is_unique(input):#this function is identifying unique substrings in a string
  char_seen = []
  for char in input:
    if char in char_seen:
      continue
    char_seen.append(char)
  return char_seen

'''stru=is_unique(input1)
stru=''.join(stru)
print(stru)'''
new_dict={}
for i in range(len(input1)):#This is for adding substrings in a new dictionary
  k=1
  new_dict[input1[i:]] = len(input1[i:])
  for p in range(len(input1)):
    new_dict[input1[i:-k]]=len(input1[i:-k])
    k+=1

#print(new_dict)
up_dict={}
for key,value in new_dict.items():#identifying substrings and checking them if unique or not
  if key in input1:
    spr=''.join(is_unique(key))
    if spr==key:
      up_dict[key]=value
#print(up_dict)
maxkey=max(up_dict.items(),key=operator.itemgetter(1))[0]#identifying the substring with maximum length and retrieving that substring
print(maxkey,":",len(maxkey))
'''for key,value in up_dict.items():
  if value==up_dict[maxkey]:
    print(key,":",value)'''