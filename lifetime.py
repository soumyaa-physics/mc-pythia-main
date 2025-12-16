hbar_GeV_s = 6.582119569e-25   # ħ in GeV*s
c = 3e8                        # m/s
ctau_m = 1e-2                  # 1 cm in meters

tau_s = ctau_m / c
width_GeV = hbar_GeV_s / tau_s
print(f"for lifetime {ctau_m} (in m) the decay width is {width_GeV}")   # -> 3.3333e-12 1.9746e-13
