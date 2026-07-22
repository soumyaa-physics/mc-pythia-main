hbar_GeV_s = 6.582119569e-25   # ħ in GeV*s
c = 3e8                        # m/s
ctau_m = 0.2   # meters

tau_s = ctau_m / c
width_GeV = hbar_GeV_s / tau_s
print(f"for lifetime {ctau_m} (in m) the decay width is {width_GeV}") 


