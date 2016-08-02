template = """
<html>
	<head>
		<title>Search results for %s in %d files</title>
	</head>

	<body>
		<h2>Search results for <b>%s</b> in <b>%d</b> files</h2>

		<p><a href="file:///home/andre/Documents/msan501/t.html">path/to/my/file</a><br>
		<br>

		<p><a href="file:///home/andre/Documents/msan501/t.html">path/to/another/file</a><br>
		<br>

	</body>
</html>
"""

html = template % ("term1 term2", 45, "term1 term2", 45)

f = open("/tmp/duh.html", "w")
f.write(html)
f.close()