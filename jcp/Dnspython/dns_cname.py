#!/usr/bin/env python
#coding=utf-8

import dns.resolver

Domain = raw_input('Please input an domain:').strip()

CNAME = dns.resolver.query(Domain, 'CNAME')

for i in CNAME.response.answer:
    for j in i.items:
        print j.to_text()