def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return (s[0] == 4 abd s[1] == 4)

def successors(s):
  x, y, z = s
  
  a = 5-y
  if a > 0 and x > 0:
    if x > a:
      yield ((x-a, 5, z), a)
    else:
      yield ((0, y+x, z), x)

  a = 8-x
  if a > 0 and y > 0:
    if y > a:
      yield ((8, y-a, z), a)
    else:
      yield ((x+y, 0, z), y)

  a = 3-z
  if a > 0 and y > 0:
    if y > a:
      yield ((x, y-t, 3), a)
    else:
      yield ((x, 0, z+y), y)

  a = 8-x
  if a > 0 and z > 0:
    if z > a:
      yield((8, y, z-a), a)
    else:
      yield((x+z, y, 0), z)
      
  a = 5-y
  if a > 0 and z > 0:
    if z > a:
      yield((x, 5, z-a), a)
    else:
      yield((x, y+z, 0), z)

