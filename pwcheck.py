#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
@file pwcheck.py -- measure password entropy from bulk of passwords
@author Tim van Werkhoven
@date 20140328
@copyright Copyright (c) 2014 Tim van Werkhoven <timvanwerkhoven@gmail.com>

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

This file is licensed under the Creative Commons Attribution-Share Alike
license versions 3.0 or higher, see
http://creativecommons.org/licenses/by-sa/3.0/
"""

############################################################################
# Import libraries
############################################################################

import sys, os
import argparse
import string
try:
	raise
	import pylab
	import numpy
	HAVE_PYLAB=True
except:
	HAVE_PYLAB=False

def main():
	(parser, args) = parsopts()

	pwdbl, pwdb = read_passwords(args.pwfile)

	# Check if all entries are unique
	# @todo Should include check of len(pwdbl) and len(pwdbl[0])
	assert len(pwdbl) == len(set(pwdbl)), "Duplicate passwords found!"

	# Check spread of characterset
	uchars, ucount = count_chars(pwdb)
	show_char_use(uchars, ucount)
	raw_input("Press key to quit...")

def parsopts():
	"""
	Parse program options and return results. This routine will take input 
	from sys.argv through parser.parse_args().

	@return Tuple of (parser, args), see argparse.ArgumentParser for details.
	"""

	parser = argparse.ArgumentParser(description=
"""Analyse the entropy in a password scheme.

Using a list of passwords generated with some method, statistically analyse the quality of this password generation scheme. Currently, the following checks are performed: 1) password duplication; 2) spread of the use of different character sets.""", epilog='', prog='pwcheck', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('pwfile', 
				help='file containing one password per line.')

	args = parser.parse_args()
	return (parser, args)

def read_passwords(pwdbfile):
	"""
	Read passwords from **pwdbfile**, expect one password per line. Return 
	list of passwords, with newlines removed.
	"""
	with open(pwdbfile) as fd:
		pwdbl = fd.readlines()
	# Drop newlines
	pwdbl = [p[:-1] for p in pwdbl]
	# Concatenate
	pwdb = "".join(pwdbl)
	assert len(pwdbl) > 10000, "Sample size too small (< 10000)"
	return pwdbl, pwdb

def count_chars(buf):
	"""
	Count unique characters in **buf**. Return a list of unique characters 
	and a list of counts as tuple.
	"""
	uchars = sorted(list(set(buf))) # Get unique chars
	ucount = [buf.count(c) for c in uchars]
	return uchars, ucount

def show_char_use(uchars, ucount):
	"""
	Plot spread of characters used in different sets:
	- digits
	- lowercase
	- uppercase
	- symbols (not alphanumeric)
	"""

	# Symbols are all printable characters minus alphanumerics
	charsymbols = "".join(set.difference(set(string.printable), set(string.digits+string.ascii_letters)))

	charsets = [string.digits, string.ascii_lowercase, string.ascii_uppercase, charsymbols]
	charsetnames = ['digits', 'lowercase', 'uppercase', 'symbols']

	for idx, (cs, csn) in enumerate(zip(charsets, charsetnames)):
		# Select charset subset
		thischars = [i for i in uchars if i in cs]
		thiscount = [c for i, c in zip(uchars, ucount) if i in cs]
		thiscountn = [t/(1.0*sum(thiscount)) for t in thiscount]
		if (HAVE_PYLAB):
			pylab.figure(100+idx);
			pylab.title("Spread of %s" % csn)
			thisidx = numpy.arange(len(thiscount))
			pylab.bar(thisidx-0.4, thiscountn)
			pylab.xticks(thisidx, thischars)
		else:
			print "Spread of %s" % csn
			for c, n in zip(thischars, thiscountn):
				# There are N=len(thischars) characters in this set,
				# so on average each occurs 1/N times. A terminal window
				# is 80 chars wide, which we equate to 4/N.
				bar = "="*int(round(70.0/4.0*n*len(thischars)))
				print " %s %s" % (c, bar)

# Run main program, must be at end
if __name__ == "__main__":
	sys.exit(main())

# EOF
