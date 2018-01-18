#!/usr/bin/env python
#coding=utf-8

import dns.resolver

Domain = raw_input('Please input an domain:').strip()

NS = dns.resolver.query(Domain, 'NS')

for i in NS.response.answer:
    for j in i.items:
        print j.to_text()