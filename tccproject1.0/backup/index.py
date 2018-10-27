#!/usr/bin/env python

print "Content-type: text/html \n"

import subprocess
subprocess.call(['/home/service/setstats'])

file = open("/var/log/service/stats.log", "r")
delimiter = ';;;'

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

for line in file:
	if delimiter in line:
		continue
	else:
		result = line.split()
		for field in result:
			print "<li>", field, "</li>"
print """
      </ul>
    </div>
  </div>
</body>
</html>
"""

file.close()
