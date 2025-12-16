# MG5 SUSY Stau Pair Production Workflow

This README documents the workflow for generating and analyzing **stau pair production** in the **MSSM** using **MadGraph5_aMC@NLO (MG5)**, **Pythia8**, and **Delphes**.

Theory reference:
https://arxiv.org/pdf/hep-ph/0512197
---

## 🧩 Step-by-Step Workflow

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
output Pol_p80_m30_500_242stauD1p7
```
Edit the configuration files:
1. run_card.dat: set the beam energies, beam polarization and the number of events (N)
2. param_card.dat: set
    - Stau and neutralino masses
    - Mixing angles
    - Neutralino mixing (bino vs higgsino LSP)

3. Calculate the stau decay width using:

```bash
python3 decay.py
```

Provide neutralino type, stau mass, Δm, and mixing angles to compute the decay width and add it to the param_card under decay of stau (10000015)

4. pythia_card.dat: Refer to example;
```bash
MG5_aMC_v2_9_18/Pol_p80_m30_500_200stauD1p7/Cards/pythia8_card.dat
```

### 4. Launch the Run
```bash
launch
```

1. In the interactive prompt, enable Pythia by pressing 1

2. Recheck all cards (run_card.dat, param_card.dat, pythia8_card.dat)

3. Press Enter to start the run

4. After completion, you will get:
    - unweighted_events.lhe → LHE file with N events
    - pythia.hepmc → HepMC file with Pythia events



### 5.Run Delphes (Outside MG5)
In a separate directory, run Delphes on the Pythia output:

```bash
./DelphesHepMC3 cards/delphes_card_ILD.tcl output/output_delphes.root madgraph/.../pythia.hepmc

```
This produces a ROOT file containing the fast detector simulation of your events.