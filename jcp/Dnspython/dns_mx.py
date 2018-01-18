#!/usr/bin/env python
#coding=utf-8

import dns.resolver

Domain = raw_input('Please input an domain:').strip()

MX = dns.resolver.query(Domain, 'MX')

for i in MX:
    print 'MX preference =', i.preference, 'mail exchanger=', i.exchange