# Vigenere cipher

## Descriptions

  The Vigenère cipher (French pronunciation: [viʒnɛːʁ]) is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.

  For example, if the plaintext is `attacking tonight` and the key is `oculorhinolaryngology`, then

  - the first letter `a` of the plaintext is shifted by 14 positions in the alphabet (because the first letter `o` of the key is the 14th letter of the alphabet, counting from zero), yielding `o`;
  - the second letter `t` is shifted by 2 (because the second letter `C` of the key is the 2nd letter of the alphabet, counting from zero) yielding `v`;
  - the third letter `t` is shifted by 20 (`U`) yielding `n`, with wrap-around;
  and so on; yielding the message `ovnlqbpvt eoegtnh`. If the recipient of the message knows the key, they can recover the plaintext by reversing this process.

  Source: (https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Cryptanalysis)

  Anyway you can use this to make secure password, bla, bla 
  
**Encrypt**
---
Enter your character (alphabet)

Enter your key       (alphabet)
```
--------------------------------------------------------------
Enter character : attacking tonight
Enter Key : oculorhinolaryngology
--------------------------------------------------------------
```
Output :
```
--------------------------------------------------------------
Character        : ATTACKING TONIGHT | Character lenght :  17
Key              : OCULORHINOLARYNGOLOGY | Key lenght :  21
Key number       : [14, 2, 20, 11, 14, 17, 7, 8, 13, 14, 11, 0, 17, 24, 13, 6, 14, 11, 14, 6, 24]
Character encode : [0, 19, 19, 0, 2, 10, 8, 13, 6, '_', 19, 14, 13, 8, 6, 7, 19]  chr lenght :  17
final key number : [14, 2, 20, 11, 14, 17, 7, 8, 13, '_', 11, 0, 17, 24, 13, 6, 14]  key lenght :  17
Encode Number    : [14, 21, 13, 11, 16, 1, 15, 21, 19, '_', 4, 14, 4, 6, 19, 13, 7] key lenght :  17
Encode Character : OVNLQBPVT EOEGTNH | char lenght : 17
--------------------------------------------------------------
```
**Decrypt**
---
Enter your character (alphabet)

Enter your key       (alphabet)
```
--------------------------------------------------------------
Enter character : OVNLQBPVT EOEGTNH
Enter Key : OCULORHINOLARYNGOLOGY
--------------------------------------------------------------
```
Output :
```
--------------------------------------------------------------
Character        : OVNLQBPVT EOEGTNH | Character lenght :  17
Key              : OCULORHINOLARYNGOLOGY | Key lenght :  21
Key number       : [14, 2, 20, 11, 14, 17, 7, 8, 13, 14, 11, 0, 17, 24, 13, 6, 14, 11, 14, 6, 24]
Character encode : [14, 21, 13, 11, 16, 1, 15, 21, 19, '_', 4, 14, 4, 6, 19, 13, 7]  chr lenght :  17
final key number : [14, 2, 20, 11, 14, 17, 7, 8, 13, '_', 11, 0, 17, 24, 13, 6, 14]  key lenght :  17
Encode Number    : [0, 19, 19, 0, 2, 10, 8, 13, 6, '_', 19, 14, 13, 8, 6, 7, 19] key lenght :  17
Encode Character : ATTACKING TONIGHT | char lenght : 17
--------------------------------------------------------------
```
**Different bettween vanila and non vanila**
---
Basicly vanila doesn't have numbers and special characters

With the same example : character `attacking tonight` and key `oculorhinolaryngology`

Vanila output : `Encode Character : OVNLQBPVT EOEGTNH | char lenght : 17`

Non vanila output : `Encode Character : OV$LQ2PVT 5O57TN8 | char lenght : 17`

P/s : sorry for bad english and this simple and non optimalize code




