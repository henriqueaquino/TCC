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
