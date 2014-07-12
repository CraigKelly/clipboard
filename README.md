Clipboard README
=================================

This is a super-simple Windows program for those of us forced to work
on windows who actually like the command prompt.  The idea is to be
able to do things like:

 * Grab the contents of a file: `cat somefile.txt | clipboard`
 * Sort the contents of the clipboard: `clipboard -o | sort | clipboard`

So it's kind of like 
 
Building
-----------

TL;DR - If you have MinGW and scons installed, run `scons` in this
directory. 

C'mon - it's a single file with one header.  Build it however you want.
I like the scons system and I've used this little project as an example
of building with scons and MinGW on Windows.

If you're unfamiliar with scons, basically you get to use a Python
script as your makefile (named SConstruct).  That let's you do things
like externalize some configuration settings (see clipboard_config.py
in this project) and perform custom logic during builds.

Note that if you're using Visual Studio instead of MinGW, you'll need
to update clipboard_config.py to build with scons. 

Extra Goodies
--------------

A great many database tools will output the text of query in a very
specific format.  For a query like `SELECT a,b FROM SomeTable` you
get output like

    Column a  Column b
    ========= ========
    Hello     World
    Goodnight Moon
    
Which is nice when you're running queries and checking things, but
sometimes you want that data in something like a spreadsheet program.
It turns out that most spreadsheet programs will accept data pasted
directly from the clipboard in tab-separated format.  Luckily the
fixed-width format shown above is easy to parse because the separator
row (row 2 with the equal signs) gives us the column widths.

Thus the included tool db2tab.py.  It reads in the format shown above from
stdin and writes a tab-separated version to stdout.  As a result, you can use
this pattern when working with a database query tool:

 * Keep running your query until you like your result
 * Select all the output text and copy to the clipboard
 * Flip to a command prompt window (which you always have open, right?)
 * Run `clipboard -o | db2tab.py | clipboard`
 * Paste the result into your favorite spreadsheet program
