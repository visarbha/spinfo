#!/usr/bin/env python3

from spi import *

opt = ap.opt()
o = opt.check()
if o.tcp:
    proto = "tcp"
elif o.udp:
    proto = "udp"
if o.service:
    if o.tcp or o.udp:
        s = sp.service(o.service,proto)
    else:
        s = sp.service(o.service)
    s.fetch()
if o.port:
    if o.tcp or o.udp:
        p = sp.port(o.port,proto)
    else:
        p = sp.port(o.port)
    p.fetch()
