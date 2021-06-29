from datetime import date
from random import choice

suffix = [
    "A lot has changed since then.",
    "We are in a climate emergency.",
    "It should be the Road User Act.",
    "E-bikes are now a thing.",
    "E-scooters are now a thing.",
    "One more lane won't fix it.",
    "More cars aren't the answer."
    "It was 47.5c in Lytton in 2021.",
    "Climate change is upon us now.",
    "cc @bcndp",
    "There needs to be a safe passing distance for cyclists",
    "Electric cars won't save us.",
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
text += " %s #bcpoli" % choice(suffix)
print("::set-output name=date::", text) 
print(text)
 
