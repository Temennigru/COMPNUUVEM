# Calculate local cost

def calc_cycle_cost_local(
	n_servers,
	n_switches,
	adm_server_ratio,
	watt_per_sq_ft,
	server_price,
	switch_price,
	personel_cost,
	floor_cost,
	power_cost,
	CPU_util,
	CPU_freq,
	server_lifespan,
	switch_lifespan,
	server_power_peak,
	server_power_idle,
	power_usage_efficiency):

	return ((calc_server_cost(server_price, n_servers, server_lifespan) +
			calc_energy_cost(server_power_peak, server_power_idle, CPU_util, power_usage_efficiency, power_cost) +
			calc_service_cost(n_servers, adm_server_ratio, personel_cost) +
			calc_network_cost(switch_price, n_switches, switch_lifespan) +
			calc_floor_cost(floor_cost, server_power_peak, CPU_util, server_power_idle, power_usage_efficiency, watt_per_sq_ft)) /
		calc_total_cycles(CPU_util, CPU_freq, n_servers))


def calc_server_cost(server_price, n_servers, server_lifespan):
	return server_price * (n_servers / server_lifespan)

def calc_energy_cost(server_power_peak, server_power_idle, CPU_util, power_usage_efficiency, power_cost):
	return ((server_power_peak * CPU_util) + (server_power_idle * (1 - CPU_util))) * power_usage_efficiency * power_cost

def calc_service_cost(n_servers, adm_server_ratio, personel_cost):
	return (n_servers / adm_server_ratio) * personel_cost

def calc_network_cost(switch_price, n_switches, switch_lifespan):
	return switch_price * (n_switches / switch_lifespan)

def calc_floor_cost(floor_cost, server_power_peak, CPU_util, server_power_idle, power_usage_efficiency, watt_per_sq_ft):
	return floor_cost * (((server_power_peak * CPU_util) + (server_power_idle * (1 - CPU_util)) * power_usage_efficiency) / watt_per_sq_ft)

def calc_total_cycles(CPU_util, CPU_freq, n_servers):
	return CPU_util * CPU_freq * n_servers

# Calc Savings

def calc_savings(cycles_source, cycle_cost_source, cycles_dest, cycle_cost_dest, trans_cost):
	return (cycles_source * cycle_cost_source) - (cycles_dest * cycle_cost_dest) - trans_costs

# Calculate learning curve

def calc_learning_curve









print calc_cycle_cost_local(10, 10, 0.01, 250, 10000, 2000, 3000, 3000, 10, 0.1, 2000000000, 5, 5, 500, 250, 1.3)


