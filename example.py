#!/usr/bin/python3.1

print('Content-type: text/html')
print()
print ('''
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" href="static/darkly.css" type="text/css"/>
    <title>Your title</title>
  </head>
''')

import cgi
form = cgi.FieldStorage()

print('''
<body>

<nav class="navbar navbar-default">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="index.html">Your WEBSITE</a>
    </div>


  </div>
</nav>

<div class="container">

		
		<p>Here is a <a class="reference internal" href="index.html">link to go back to the index</a>.

                <p>
		Enter a number :
			<form action="example.py" method="post" class="form-inline">
			<input type="text" name="number" class="form-control"/>
			<input type="submit" value="Submit" class="btn btn-success btn-sm">
			</form>
                </p>
''')
if form.getvalue('number') == None: 
  print('''
                <p>Some message...</p>
  ''')
else:
  p = cgi.escape(form.getvalue('number')) # very important for security !!!
  # Here you can do whatever you want with the variable p...
  try:
    p = float(p)
    p2 = p**2
    print('<p>You have entered', p,'. Its squarred is:', p2, '.</p>')
  except:
    print('''<p>Some error occured in the system.</p>''')
print('''
</div>
</body>
</html>
''')
