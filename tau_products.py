#!/usr/bin/env python3
import sys
import math
from collections import Counter
import pyhepmc_ng as hep

if len(sys.argv) != 2:
    print("Usage: python count_tau_decay_products.py path/to/events.hepmc")
    sys.exit(1)

fname = sys.argv[1]
reader = hep.ReaderAscii(fname)

# PDG codes
PDG_TAU = 15
PDG_E    = 11
PDG_MU   = 13
PDG_PI   = 211

counts = Counter()
total_taus = 0

def is_final(p):
    return p.status == 1

def trace_from_tau_to_final(tau):
    """Return a set of PDG codes (final-state) that descend from this tau."""
    out = []
    # Do a BFS over vertices starting from tau's end vertex (if any)
    v_end = tau.end_vertex
    if v_end is None:
        return out
    stack = list(v_end.particles_out)
    visited = set()
    while stack:
        p = stack.pop()
        if p in visited:
            continue
        visited.add(p)
        if p.status == 1:
            out.append(p.pid)
        else:
            # push descendants (particles_out of its end vertex)
            if p.end_vertex is not None:
                stack.extend(p.end_vertex.particles_out)
    return out

while True:
    evt = reader.read()
    if evt is None:
        break
    # find all taus in the event that are from stau decays or primary
    for p in evt.particles:
        if p.pid == PDG_TAU and p.status != 4:  # status filters may vary; include taus
            total_taus += 1
            final_daughters = trace_from_tau_to_final(p)
            # classify
            if any(abs(pid) == PDG_E for pid in final_daughters):
                counts['e'] += 1
            if any(abs(pid) == PDG_MU for pid in final_daughters):
                counts['mu'] += 1
            if any(abs(pid) == PDG_PI for pid in final_daughters):
                counts['pi'] += 1
            # optionally count hadronic (any charged pion or kaon)
            if any(abs(pid) in (211, -211, 321, -321) for pid in final_daughters):
                counts['hadron'] += 1

print("Total taus considered:", total_taus)
print("Counts (a tau may contribute to multiple categories if decays to, e.g., e + pi):")
for k in ['e','mu','pi','hadron']:
    print(f"  {k}: {counts[k]}")
