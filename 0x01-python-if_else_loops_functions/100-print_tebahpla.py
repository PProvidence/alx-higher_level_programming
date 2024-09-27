#!/usr/bin/python3
for alpha in range(ord('z'), ord('a') - 1, -1):
    print('{:c}'.format(alpha) if alpha % 2 == 0 else chr(alpha-32), end='')
