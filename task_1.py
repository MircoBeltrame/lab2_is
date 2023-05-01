def generate_leg_err():
  E = [0,1,2,4,8,16,32,64]
  e = np.random.choice(np.array(E,dtype='int32'))
  e = str(bin(e))[2:]
  e = '0'*(7-len(e))+e
  e = [int(i) for i in e]
  return np.array(e, dtype='int32')

def generate_unique(n,max):
  x = set()
  if (n <= max):
    while len(x)<n:
      e = np.random.randint(max)
      x.add(e)
  return [i for i in x]

def generate_eve_err():
  e = np.zeros(7,dtype='int32')
  n_errors = np.random.choice(np.array([0,1,2,3]),p = np.array([1/64,7/64,21/64,35/64]))
  bits = generate_unique(n_errors,7)
  for b in bits:
    e[b]+=1
  return e
  
def string_to_array(s):
  l = [int(i) for i in s]
  return np.array(l,dtype='int32')

def array_to_string(a):
  s = ''
  for i in a:
    s+=str(i)
  return s

def wiretrap(x):
  y = array_to_string(np.mod(x+generate_leg_err(),2*np.ones(7,dtype='int32')))
  z = array_to_string(np.mod(x+generate_eve_err(),2*np.ones(7,dtype='int32')))
  return(y,z)

def count_only_one(l,y,index):#0 for y 1 for z
  count = 0
  for i in l:
    if i[index]==y:
      count+=1
  return count
  
def task_1(x,n_iter=10000):
  YZ = []
  Y_unique = set()
  Z_unique = set()
  #n_iter = 10000
  for i in range(n_iter):
    y,z = wiretrap(x)
    YZ.append((y,z))
    Y_unique.add(y)
    Z_unique.add(z)

  count_y = dict()
  for y in Y_unique:
    count_y.update({y:count_only_one(YZ,y,0)})

  count_z = dict()
  for z in Z_unique:
    count_z.update({z:count_only_one(YZ,z,1)})
  print('z:')
  for z in Z_unique:
    print('probability of',z,'=',count_z[z]/n_iter)
  print('-------------------')
  print('y:')
  for y in Y_unique:
    print('probability of',y,'=',count_y[y]/n_iter)

  labels = list(count_z.keys())
  values = [e/n_iter for e in list(count_z.values())]
  values
  plt.figure(figsize=(12,5))
  plt.bar(range(len(labels)), values, width=0.5, tick_label=labels)
  plt.xticks(rotation='vertical')
  plt.show()
