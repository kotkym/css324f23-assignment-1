def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return (s[0] == 4 and s[1] == 4)

def successors(s):
  x, y, z = s
  
  t = 5-y
  if t > 0 and x > 0:
    if x > t:
      yield ((x-t, 5, z), t)
    else:
      yield ((0, y+x, z), x)

  t = 8-x
  if t > 0 and y > 0:
    if y > t:
      yield ((8, y-t, z), t)
    else:
      yield ((x+y, 0, z), y)

  t = 3-z
  if t > 0 and y > 0:
    if y > t:
      yield ((x, y-t, 3), t)
    else:
      yield ((x, 0, z+y), y)

  t = 8-x
  if t > 0 and z > 0:
    if z > t:
      yield((8, y, z-t), t)
    else:
      yield((x+z, y, 0), z)
      
  t = 5-y
  if t > 0 and z > 0:
    if z > t:
      yield((x, 5, z-t), t)
    else:
      yield((x, y+z, 0), z)

