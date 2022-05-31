# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp):
  temp_C = (f_temp - 32) * 5/9
  return temp_C

f100_in_celsius = f_to_c(100) 

def c_to_f(c_temp):
  temp_f = c_temp * (9/5) + 32
  return temp_f


def get_force(mass, acceleration):
  return mass * acceleration

train_force = (get_force(train_mass, train_acceleration))
print("The GE train supplies ", train_force, " Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies X Joules. ", bomb_energy)


def get_work(mass, acceleration, distance):
  return mass * acceleration * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does ", train_work, " Joules of work over ", train_distance, " meters. ") 



        

