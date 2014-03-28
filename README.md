pwcheck
=======

Analyse the entropy in a password scheme from a list of pre-generated 
passwords with said scheme.

Use
===

This script is meant to assess the entropy of a password generating 
_scheme_, not an individual password. This could expose flaws in password 
generation, making passwords with such schemes weak.

Method
======

Using a list of passwords generated with some method, statistically analyse 
the quality of this password generation scheme. Currently, the following 
checks are performed: 

1. Password duplication
2. Spread of the use of different character sets

This is a crude check and does not guarantee against a broken password 
scheme. In the future, the entropy of the passwords should be properly 
estimated from the occurence of digrams and trigrams in the list.

Password generation
===================

Related links
=============

Alternative schemes are available online:
- http://rumkin.com/tools/password/passchk.php
- https://tech.dropbox.com/2012/04/zxcvbn-realistic-password-strength-estimation/
- https://github.com/dropbox/zxcvbn