try:
    from .__init__ import solve
except SystemError:
    from __init__ import solve

print(solve(input('Eq: ')))
