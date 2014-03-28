pwcheck results
===============

These are some results obtained on password entropy using various schemes.

Schemes used
------------

The following schemes were analysed:

1. Apple Keychain Password Assistant[1][2]
1.1. Memorable scheme
1.2. Numbers scheme

Method
------

First, a list of passwords were generated for analysis. Subsequently, these
were parsed through the pwcheck.py routine. The commands used to generate 
the lists are given below:

1. AKPA: pwgen -c 10000 -l 16

while [[ $(wc -l pwdump | awk '{print$1}') -lt 100000 ]]; do ./pwgen -a alphanumeric -c 10000 -l 16 >> pwdump; done

Results
-------

### AKPA

All schemes behaved randomly, except the memorable scheme which seemed to 
have slightly less use of 0 and 9 compared to other digits. The letter use 
was irregular, similar to natural languages.

References
----------

[1] https://support.apple.com/kb/PH10624  
[2] https://github.com/anders/pwgen  