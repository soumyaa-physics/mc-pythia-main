# MG5 SUSY Stau Pair Production Workflow

This README documents the workflow for generating and analyzing **stau pair production** in the **MSSM** using **MadGraph5_aMC@NLO (MG5)**, **Pythia8**, and **Delphes**.

## Step-by-Step Workflow

### 1. Start MG5

Open a terminal and start MadGraph5:

```bash
cd /path/to/MG5_aMC_v2_9_18
./bin/mg5_aMC 
```

### 2. Import the MSSM Model and Generate the Process
Inside the MG5 interactive shell:
```bash
import model MSSM_SLHA2
generate e+ e- > ta1- ta1+
```

### 3. Create the Output Folder, Edit and launch the run

```bash
output FCCee_mass_stau_lifetime_ctau_ecm_com
```

You can exit the mg5 session here.

Edit the configuration files:
1. run_card.dat: set the beam energies and the number of events (N)
2. param_card.dat: set
    - Stau and gravitino masses
    - Stau decay width and its decay product

[For reference look at the example in FCCee_100_stau_20m_ctau_ecm_240]

Restart the mg5 session and:

```bash
launch FCCee_mass_stau_lifetime_ctau_ecm_com
```

3. Calculate the stau decay width using:

```bash
python3 lifetime.py
```

[comment]: <>  (Provide neutralino type, stau mass, Δm, and mixing angles to compute the decay width and add it to the param_card under decay of stau (10000015))

4. pythia_card.dat: Refer to example:
```bash
MG5_aMC_v3_6_6/FCCee_100_stau_2m_ctau_ecm_240/Cards/pythia8_card.dat
```

### 4. Launch the Run
```bash
launch
```
It is best to set the PYTHIA path:
```bash
export PYTHIA8DATA=/path/to/MG5_aMC_v3_6_6/HEPTools/pythia8/share/Pythia8/xmldoc
```

1. In the interactive prompt, enable Pythia by pressing 1
2. Press Enter to start the run
3. After completion, you will get:
    - unweighted_events.lhe → LHE file with N events
    - pythia.hepmc → HepMC file with Pythia events
