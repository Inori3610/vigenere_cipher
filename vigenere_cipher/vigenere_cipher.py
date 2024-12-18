import array
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W" ,"X", "Y", "Z",  # 26 alphabet
       "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "<", ">"]       # 25 special characters
print ("--------------------------------------------------------------")
char_need_encode = input("Enter character : ").upper()
key = input("Enter Key : ").upper()

char_number = []
key_number = []
final_key = []
encode_number = []
encode_char = ""
# Character to number 
for i in char_need_encode:
    if i in abc:
        index_char = abc.index(i)
        char_number.append(index_char)
    else:
        char_number.append("_")
for i in key:
    if i in abc:
        index_key = abc.index(i)
        key_number.append(index_key)
# Make the number array duplicate and to make it equal to the character        
for i in range(int(len(char_need_encode)/len(key))):
    for j in range (len(key)):
        final_key.append(key_number[j])
for i in range((len(char_need_encode)%len(key))):    
    final_key.append(key_number[i])
    
# Add the space to the finalkey array
for i in range(len(char_need_encode)):
    if char_number[i] == "_":
        final_key.insert(i,"_")
        final_key.pop(i+1)
        #final_key.pop(len(final_key)-1)
# Combine the two array to make the encode text
for i in range(len(char_need_encode)):
    if char_number[i] == "_":
        encode_number.append("_")
        encode_char += " "
    elif char_number[i] + final_key[i] < 26+25:
        encode_number.append(char_number[i]+final_key[i])
        encode_char += abc[(char_number[i]+final_key[i])]
    elif char_number[i] + final_key[i] >= 26+25:
        encode_number.append((char_number[i]+final_key[i])%(26+25))  # 26 alphabet + 25 special characters
        encode_char += abc[(char_number[i]+final_key[i])%(26+25)]

# Result
print (len(abc))
print ("--------------------------------------------------------------")
print ("Character        :",char_need_encode,"| Character lenght :  " + str(len(char_need_encode)) )
print ("Key              :",key, "| Key lenght : ",len(key))
print ("Key number       :",key_number)
print ("Character encode :", char_number," chr lenght : ",len(char_number))
print ("final key number :", final_key," key lenght : ", len(final_key))
print ("Encode Number    :",encode_number, "key lenght : ",len(encode_number))
print ("Encode Character :",encode_char, "| char lenght :" ,len(encode_char))
print ("--------------------------------------------------------------")
