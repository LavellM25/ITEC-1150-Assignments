import re

people = []
people.append('ideguy ideguy@mac.com')
people.append('yenya yenya@optonline.net')
people.append('kosact kosact@yahoo.ca')
people.append('sjava sjava@live.com')
people.append('papathan papathan@msn.com')
people.append('vmalik vmalik@att.net')
people.append('singer singer@msn.com')
people.append('kronvold kronvold@aol.com')
people.append('campware campware@att.net')
people.append('hyper hyper@hotmail.com')
people.append('rogerspl rogerspl@yahoo.ca')
people.append('tromey tromey@verizon.net')

email_regex = re.compile(r'[\w\-.]+@([\w\-.]+\.[A-z]+)')

domains = []
for person in people:
    match = email_regex.search(person)
    if match:
        domain = match.group(1)
        if domain not in domains:
            domains.append(domain)
domains.sort()
print(domains)

"""
Here is a quick reference guide for various rules in regular expressions:
Identifiers:
\d Any number
\D Anything but a number
\s Whitespace (spaces, tabs, newline)
\S Anything but a space
\w Any letter, number, or underscore
\W Anything but a letter, number, or underscore
. Any character, except for a new line
\b Space around whole words

Modifiers:
+ 1 or more repetitions
? 0 or 1 repetitions
* 0 or more repetitions
$ The end of string
^ The start of a string
| Either/or. For example, x|y will match either x or y
[] A range. For example, [A-Za-z1-5] which means A-Z or a-z or 1-5
{x} Exactly x repetitions
{x,y} Between x and y repetitions

White Space Characters:
• \n = new line
• \s = space
• \t = tab
• \e = escape
• \f = form feed
• \r = carriage return
Characters to REMEMBER TO ESCAPE IF USED!

• . + * ? [ ] $ ^ ( ) { } | \
Brackets:
• [] = quant[ia]tative = will find either quantitative, or quantitative.
• [a-z] = return any lowercase letter a-z
• [1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z
"""
