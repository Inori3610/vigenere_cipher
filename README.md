# Vigenere cipher

## Descriptions

  The Vigenère cipher (French pronunciation: [viʒnɛːʁ]) is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.

  For example, if the plaintext is `attacking tonight` and the key is oculorhinolaryngology, then

  the first letter a of the plaintext is shifted by 14 positions in the alphabet (because the first letter o of the key is the 14th letter of the alphabet, counting from zero), yielding o;
  the second letter t is shifted by 2 (because the second letter C of the key is the 2nd letter of the alphabet, counting from zero) yielding v;
  the third letter t is shifted by 20 (U) yielding n, with wrap-around;
  and so on; yielding the message ovnlqbpvt eoegtnh. If the recipient of the message knows the key, they can recover the plaintext by reversing this process.

  The Vigenère cipher is therefore a special case of a polyalphabetic substitution.

  First described by Giovan Battista Bellaso in 1553, the cipher is easy to understand and implement, but it resisted all attempts to break it until 1863, three centuries later. This earned it the description le chiffrage indéchiffrable (French for 'the indecipherable     cipher'). Many people have tried to implement encryption schemes that are essentially Vigenère ciphers.[3] In 1863, Friedrich Kasiski was the first to publish a general method of deciphering Vigenère ciphers.
