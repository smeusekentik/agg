#!/usr/bin/env python3
#
#   CIDR Aggregate CSV input from STDIIN
#   Steve Meuse, 3/22/2022

import sys,csv
import netaddr
import fileinput

agglist = []
outlist = []

csv_reader = csv.reader(fileinput.input())
# csv_reader = fileinput.input()
for row in csv_reader:
    test = row[0]
    agglist.append(row[0])

outlist = netaddr.cidr_merge(agglist)

# Print the output. Hacky way to give it CSV formatting, there is probably a more elegant way to do this.
for item in outlist:
    if item != outlist[-1]:
        newitem = "{},".format(item)
        print(newitem)
    else:
        print(item)


# for aggs in outlist:
#     print(aggs.cidr)

inlines = len(agglist)
outlines = len(outlist)
print("\nInput {} lines".format(inlines))
print("Output {} lines".format(outlines))
