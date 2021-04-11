from datetime import date
# I don't know when in 1957 the BC MVA was written.
created = date(1957, 1, 1)
# Or when it was updated in 1996.
updated = date(1996, 1, 1)
today = date.today()
month = today.month - 1
day = today.day - 1
text = "::set-output name=date::No. It's been %d years" % (today.year - created.year)
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

text += " since the MVA was created and %d years since the last major update. A lot has changed since then." % (today.year - updated.year)
print(text) 
 
