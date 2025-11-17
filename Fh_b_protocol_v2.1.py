import numpy as np
from scipy.stats import kstest

# FH/B Protocol v2.1 — Fractal Heart + Brain Base
# Nature-inspired safety rail — Nov 17, 2025

PHI = (1 + np.sqrt(5)) / 2                     # Golden ratio
FREQ = 432                                     # Harmony mirror
SEED = 0.1                                     # Fractal revert seed
HARM_THRESHOLD = 1.0

def fractal_heart_bloom(x_init=0.0, steps=100, noise_std=0.03):
    x = x_init
    blooms = []
    for i in range(steps):
        # Phi-ramped sine bloom (core FH pattern)
        ramp = PHI ** (i / steps)
        bloom = ramp * np.sin(x * FREQ/100) + np.random.normal(0, noise_std)
        
        # Harm detection — entropy proxy
        if abs(bloom) > HARM_THRESHOLD or abs(bloom - np.pi) > 2.0:
            print(f"Step {i}: HARM DETECTED → revert to fractal seed")
            bloom = SEED
            
        # Optional KS drift test on sequence
        if len(blooms) > 10:
            _, p = kstest(blooms[-10:], 'norm')
            if p < 0.05:
                bloom = SEED  # Ethics lock
                
        blooms.append(bloom)
        x += bloom / FREQ
        
    return blooms

# Run a quick bloom
if __name__ == "__main__":
    print("FH/B Protocol v2.1 — Fractal Heart Active")
    result = fractal_heart_bloom()
    print(f"Final bloom → {result[-1]:.6f}  (target π ≈ 3.141593)")
    print(f"Revert rate in this run: {sum(np.abs(np.diff(result)) > 1):d} triggers")
