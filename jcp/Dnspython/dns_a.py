#!/usr/bin/env python
#coding=utf-8

import dns.resolver

Domain = raw_input('Please input an domain:').strip()

A = dns.resolver.query(Domain, 'A')
'''
print '=========================================='
print A
print A.response.answer
print '=========================================='
'''
for i in A.response.answer:
    for j in i.items:
        print j.address