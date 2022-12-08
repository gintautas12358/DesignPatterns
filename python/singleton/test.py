from Parameter_singleton import ParameterSingleton

ps0 = ParameterSingleton()
ps1 = ParameterSingleton()
ps2 = ParameterSingleton()

print(ps0)
print(ps1)
print(ps2)

print(ps0.port_mappings)
ps0.port_mappings["5000"] = "9000"

print(ps0.port_mappings)
print(ps1.port_mappings)
print(ps2.port_mappings)

