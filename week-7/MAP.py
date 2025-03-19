import numpy as np
import random
import matplotlib.pyplot as plt


def simulate_slotted_aloha(n_nodes, p, n_slots):
    """Simulate Slotted ALOHA: successful slot if exactly one node transmits."""
    successes = 0
    for _ in range(n_slots):
        # Each node transmits with probability p in a slot
        transmissions = sum(1 for _ in range(n_nodes) if random.random() < p)
        if transmissions == 1:
            successes += 1
    efficiency = successes / n_slots
    return efficiency

def simulate_pure_aloha(n_nodes, p, n_slots):
   
    successes = 0
    prev_transmission = False
    for _ in range(n_slots):
        transmissions = sum(1 for _ in range(n_nodes) if random.random() < p)
        if transmissions == 1 and not prev_transmission:
            successes += 1
        prev_transmission = (transmissions > 0)
    efficiency = successes / n_slots
    return efficiency

def simulate_csma_cd(n_nodes, p, n_slots):
    
    successes = 0
    channel_busy = False
    for _ in range(n_slots):
        if channel_busy:
            transmissions = 0
            channel_busy = False  
        else:
            transmissions = sum(1 for _ in range(n_nodes) if random.random() < p)
        if transmissions == 1:
            successes += 1
            channel_busy = False
        elif transmissions > 1:
            channel_busy = True
        else:
            channel_busy = False
    efficiency = successes / n_slots
    return efficiency

# parameters
n_nodes = 50
n_slots = 10000
ps = np.linspace(0, 1, 50)

# run simulations
eff_slotted = [simulate_slotted_aloha(n_nodes, p, n_slots) for p in ps]
eff_pure = [simulate_pure_aloha(n_nodes, p, n_slots) for p in ps]
eff_csma = [simulate_csma_cd(n_nodes, p, n_slots) for p in ps]

# plotting the efficiencies on the same graph
plt.figure(figsize=(8, 6))
plt.plot(ps, eff_slotted, marker='o', label='Slotted ALOHA')
plt.plot(ps, eff_pure, marker='s', label='Pure ALOHA (approx.)')
plt.plot(ps, eff_csma, marker='^', label='CSMA/CD (simplified)')
plt.xlabel('Transmission Probability (p)')
plt.ylabel('Efficiency (Throughput)')
plt.title('Comparison of Multiple Access Protocols')
plt.legend()
plt.grid(True)
plt.show()
