# debug_log.md
# Author: Aayush Iyer

## Bug 1
Error type: KeyError
File + line: week8_buggy.py, line 12 (in get_total), called from line 21
What the error means: A dictionary lookup failed because the key 'amount' doesn't exist in one of the records
What I told the duck: I said ‘look up amount in each record’ and when I read the first record letter by letter, it said amout, not amount.
What I tried: Added a DEBUG print inside get_total() to show each record before the lookup. It printed only Taylor's record before crashing, so the first record seemed to be the problem.
How I fixed it: Changed the misspelled key 'amout' to 'amount' in the first record, then i removed the DEBUG print

## Bug 2
Error type: TypeError
File + line: week8_buggy.py, line 16 (in is_over_limit), called from line 23
What the error means: Python can't use > to compare an integer (5150) with a string ('1000'), because they're different types
How I fixed it: I removed the quotes around '1000' on line 16 so its the integer 1000. now both sides are integers and the comparison works

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records / True
Did pytest pass? Yes / No

## AI Literacy Reflection
Did I use AI? No
If yes -- exact prompt I used: 
What AI explained: 
What I changed myself: 
Can I explain every fixed line? Yes

## What I learned
I learned to read error messages from the bottom up to find what broke and where. Adding a print statement helped me see the actual data and spot the typo.