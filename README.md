pwcheck
=======

Analyse the entropy in a password scheme from a list of pre-generated 
passwords with said scheme.

Using a list of passwords generated with some method, statistically analyse 
the quality of this password generation scheme. Currently, the following 
checks are performed: 

1. Password duplication
2. Spread of the use of different character sets

This is a crude check and does not guarantee against a broken password 
scheme. In the future, the entropy of the passwords should be properly 
estimated from the occurence of digrams and trigrams in the list.
