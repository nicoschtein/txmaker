#!/usr/bin/python

import random, sys
import argparse

def printHeader():
  print '-------------------------------------------------'
  print '--------- Crypto Transaction Maker v0.1 ---------'
  print '-------- github.com/nicoschtein/txmaker/ --------'
  print '-------------------------------------------------'

def check_gt0(value):
    ivalue = int(value)
    if ivalue >0:
      return ivalue
    raise argparse.ArgumentTypeError("%s must be greater than 0." % value)

parser = argparse.ArgumentParser(description='Transactions maker')
group = parser.add_argument_group()
group.add_argument("-c", "--count", help="the number of transactions to generate", type=check_gt0)
group.add_argument('-a', '--addresses', nargs='*', help='list of addresses to use, will repeat if less than count', default=['<address>'])
parser.add_argument('-p', '--prefix', help='prefix for tx comment', default='backup')
parser.add_argument("-f", "--fee", help="coind transaction fee", type=float, default='0.01')
parser.add_argument('-d', '--daemon', help='coin daemon name', default='coind')
args = parser.parse_args()
cantAdds = len(args.addresses)
if (args.count):
  L=[args.count]
  L[0]=args.count
else:
  L=[cantAdds]
  L[0]=cantAdds
  
fees = args.fee*L[0]

printHeader()
print 'Transactions count: '+ str(L[0])
print 'Aprox txfees: ' + str(fees)
print 'Transactions:\n'
for i in xrange(1,L[0]+1):
  L.append(random.uniform(1.5,4.9)*1)
  print args.daemon + ' sendtoaddress ' + args.addresses[i%cantAdds] + ' ' + '%.8f' % L[i] + ' \"' + args.prefix + ' ' + str(i) + '\"'
total = sum(L[1:len(L)-1])
print '\nTotal amount: ' + str(total)
print 'Total amount+fees: ' + str(total+fees)