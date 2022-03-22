#!/usr/bin/env python
#
#   CIDR Aggregate CSV input from STDIIN
#   Steve Meuse, 3/22/2022

import sys,netaddr,csv

agglist = []
outlist = []

csv_reader = csv.reader(sys.stdin)
for row in csv_reader:
    test = row[0]
    agglist.append(row[0])

outlist = netaddr.cidr_merge(agglist)

for aggs in outlist:
    print(aggs.cidr)

inlines = len(agglist)
outlines = len(outlist)
print("\nInput {} lines".format(inlines))
print("Output {} lines".format(outlines))