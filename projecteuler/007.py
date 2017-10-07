"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?

http://www.solipsys.co.uk/new/SieveOfEratosthenesInPython.html


The essence is that having decided a number pp is prime, we print it (or in this case, return or
"yield" it) and suspend the flagging until we need it. We remember that p2p2 is a composite and has
pp as a factor, but we don't run forward from there until we need to. So we maintain a "dictionary of
composites" which is indexed by the numbers we know to be composite. Each entry in the dictionary holds
a list of known factors for the number. Thus in the entry for v2v2 we store v.v. Then we increment v.v.

When we look at the next candidate, v,v, we see if it is in our dictionary of composites. If so
then we do not return it, because we know it's not prime. Instead, we look at all the factors ff
we know of it, and for each we insert into our dictionary that v+fv+f has ff as a factor. Having
done so we can delete vv from our dictionary, thus saving space (and time for subsequent lookups).

We continue until we find a number that is not in our dictionary of
composites, and realise that it must be prime. Thus we return it.
"""

from collections import defaultdict

composites = defaultdict(list)


def genprimes():
    v = 2
    while True:
        yield v
        composites[v * v] = [v]
        v += 1
        while v in composites:
            for f in composites[v]:
                composites[v + f].append(f)
            del composites[v]
            v += 1

count = 0

for prime in genprimes():
    count +=1
    if count == 10001:
        print prime
        break
