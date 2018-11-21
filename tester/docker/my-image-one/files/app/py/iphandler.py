#!/usr/bin/env python

import re
import subprocess as sp

def get_ips():
	input_values = sp.check_output(['ip','addr'])
	testers = input_values.split()
	ips = []

	for i in testers:
		if re.match('^\d{2,3}\.[\d./]+$', i) <> None:
			ips.append(re.match('^\d{2,3}\.[\d./]+$', i).group(0))
	return ips

def choose_ips():
    ips = get_ips()
    res = []

    for i in ips:
        aux = i.split("/")
        aux_ = aux[0].split(".")
        tester = int(aux_[len(aux_)-1])
        if tester <> 255 and tester <> 1:
            res.append(aux[0])
    return res
