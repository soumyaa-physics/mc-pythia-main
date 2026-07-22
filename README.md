# MG5 SUSY Stau Pair Production Workflow

This guide explains how to generate **stau pair production events** in the **MSSM** using:

- **MadGraph5_aMC@NLO (MG5)** → matrix element generation
- **Pythia8** → particle showering and stau decay simulation

The process considered is:

```text
e+ e- → ~tau1- ~tau1+
```

---

# Step-by-Step Workflow

## 1. Start MadGraph5

Go to the MG5 directory and start MG5:

```bash
cd /path/to/MG5_aMC_v2_9_18
./bin/mg5_aMC
```

---

## 2. Generate the Stau Pair Production Process

Inside the MG5 prompt:

```bash
import model MSSM_SLHA2
generate e+ e- > ta1- ta1+
```

Create the process folder:

```bash
output FCCee_mass_stau_lifetime_ctau_ecm_com
```

Exit MG5:

```bash
exit
```

---

## 3. Configure the Run

Edit the files inside:

```
FCCee_mass_stau_lifetime_ctau_ecm_com/Cards/
```

### `run_card.dat`

Set:

- Beam energy
- Number of generated events

Example for FCC-ee at 240 GeV:

```text
ebeam1 = 120 GeV
ebeam2 = 120 GeV
```

### `param_card.dat`

Set:

- Stau mass
- Gravitino mass
- Stau decay width
- Decay channel

The decay width is calculated from the stau lifetime (`cτ`):

```bash
python3 lifetime.py
```

Provide the lifetime in meters and insert the resulting width into the stau decay section.

Example:

```text
DECAY 1000015 9.8731e-18  # ~tau^-_1
    1.000000e+00 2 15 1000049  # ~tau^-_1 -> tau^- grv
```

### `pythia8_card.dat`

Pythia8 also needs the stau lifetime (`cτ`) to simulate the displaced decay correctly. Use the example:

```
MG5_aMC_v3_6_6/FCCee_100_stau_2m_ctau_ecm_240/Cards/pythia8_card.dat
```

Set the stau proper decay length in **mm**:

```text
PartonLevel:ISR = on
PartonLevel:FSR = on

SUSY:all = on

1000015:tau0 = 20000   # stau cτ in mm (20 m)
1000015:mayDecay = on
```

The value of `tau0` must match the lifetime used when calculating the decay width in `param_card.dat`.

For example:

- `cτ = 20 m`
- `tau0 = 20000 mm`

---

## 4. Run the Simulation

Start MG5:

```bash
./bin/mg5_aMC
```

Launch the generated process:

```bash
launch FCCee_mass_stau_lifetime_ctau_ecm_com
```

Set the Pythia8 path:

```bash
export PYTHIA8DATA=/path/to/MG5_aMC_v3_6_6/HEPTools/pythia8/share/Pythia8/xmldoc
```

In the MG5 menu:

1. Enable Pythia8 (`1`)
2. Press Enter to start the run

---

## 5. Output Files

After completion:

```
unweighted_events.lhe
```

MadGraph generated events.

```
pythia8_events.hepmc
```

Pythia8 showered and decayed events.

---

## Example Setup

A complete working example:

```
FCCee_100_stau_20m_ctau_ecm_240/
```

with:

- Stau mass: 100 GeV
- Lifetime: 20 m
- Collision energy: 240 GeV