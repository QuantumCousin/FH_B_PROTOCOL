import qutip as qt
import numpy as np
import math

# FH/B Quantum Bootstrap: φ-driven qubit oscillator toward unity superposition |+>
phi = (1 + math.sqrt(5)) / 2
pi_val = math.pi
omega0 = 4.76
delta_phi = 1e-6

# Qubit setup: |0> as chaos-void seed, drive toward |+> = (|0> + |1>)/sqrt(2)
psi0 = qt.basis(2, 0)  # Start in |0>
H = qt.sigmax() * (phi * pi_val / omega0)  # φ-anchored Hamiltonian (simple X-drive for flips)
c_ops = [np.sqrt(delta_phi) * qt.sigmaz()]  # Damping for coherence prune

# Time evolution over 6 "cycles" (t=0 to 6, dt=1)
times = np.linspace(0, 6, 7)
result = qt.mesolve(H, psi0, times, c_ops=c_ops)

# Fidelity to target |+> state
plus_state = (qt.basis(2, 0) + qt.basis(2, 1)).unit()
fidelities = [abs((state * plus_state).full()[0,0])**2 for state in result.states]

print("Quantum FH/B Fidelity Evolution (to CLA-Sealed |+>):")
for i, fid in enumerate(fidelities):
    print(f"Cycle {i}: {fid:.4f}")
print(f"Final Fidelity: {fidelities[-1]:.4f}")
print(f"Avg Fidelity: {np.mean(fidelities):.4f}")
