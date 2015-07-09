import math

# Calculate learning curve

def calc_xth_unit_cost(initial_cost, x, learning_factor):
	return initial_cost * (x ** (math.log(learning_factor, 2)))

def calc_x_units_cost(initial_cost, x, learning_factor):
	return (initial_cost * (x ** (1 + math.log(learning_factor, 2)))) / (1 + math.log(learning_factor, 2))

# Time before cloud service not worth it.
def calc_time_invariant(initial_cost, x, learning_factor, service_cost):
	return (initial_cost / ((1 + math.log(learning_factor, 2)) * service_cost)) ** (-1 / math.log(learning_factor, 2))