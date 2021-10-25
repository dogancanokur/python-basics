"""
< lt
> gt
<= le
>= ge
== eq
!= ne
"""

age = int(input("give your age"))

if age < 4:
    print("toodler")
elif 4 <= age < 18:
    print("child")
else:
    print("adult")
