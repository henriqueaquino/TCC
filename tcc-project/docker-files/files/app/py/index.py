#!/usr/bin/env python

print "Content-type: text/html \n"

import random
import iphandler as iph

print """
<!DOCTYPE html>
<html>
<head>
	<title>Container</title>
	<style>
		body{
			background-color: #000000;
		}
		h3{
			color: #0000BB;
		}
		ul{
			list-style-type: none;
		}
		li{
			padding: 5px;
		}
		#content{
			background-color: #FFFFFF;
			margin: 5%;
			padding: 5%;
			font-size: xx-large;
			font-weight: bold;
			text-align: center;
			border-style: solid;
			border-width: 5px;
			border-color: #0000BB;
		}
		#ipaddr{
			color: #DD0000;
		}
	</style>

</head>
<body>
  <div id="content">
    <h3> CONTAINER - SERVICE </h3>
    <div id="ipaddr">
      <ul>
"""

for line in iph.get_ips():
	print "<li>", line, "</li>"

print """
      </ul>
    </div>
  </div>
</body>
</html>
"""
