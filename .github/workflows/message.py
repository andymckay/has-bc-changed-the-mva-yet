from datetime import date
from random import choice

suffix = [
    "A lot has changed since then.",
    "We are in a climate emergency.",
    "It should be the Road User Act.",
    "E-bikes are now a thing.",
    "E-scooters and now a thing.",
    "One more lane won't fix it.",
]

# I don't know when in 1957 the BC MVA was written.
created = date(1957, 1, 1)
# Or when it was updated in 1996.
updated = date(1996, 1, 1)
today = date.today()
month = today.month - 1
day = today.day - 1
text = "No. It's been %d years" % (today.year - created.year)
if month: 
    if month > 1:
        text += ", %s months" % month
    elif month:
        text += ", %s month" % month

if day:
    if day > 1:
        text += " and %s days" % day
    elif day:
        text += " and %s day" % day

text += " since the MVA was created and %d years since the last major update." % (today.year - updated.year)
text += "\n%s" % choice(suffix)
print("::set-output name=date::", text) 
print(text)
 
