# Vigenere cipher

## Descriptions

  The Vigenère cipher (French pronunciation: [viʒnɛːʁ]) is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.

  For example, if the plaintext is `attacking tonight` and the key is `oculorhinolaryngology`, then

  - the first letter `a` of the plaintext is shifted by 14 positions in the alphabet (because the first letter `o` of the key is the 14th letter of the alphabet, counting from zero), yielding `o`;
  - the second letter `t` is shifted by 2 (because the second letter `C` of the key is the 2nd letter of the alphabet, counting from zero) yielding `v`;
  - the third letter `t` is shifted by 20 (U) yielding `n`, with wrap-around;
  and so on; yielding the message `ovnlqbpvt eoegtnh`. If the recipient of the message knows the key, they can recover the plaintext by reversing this process.
