# FH/B Protocol — Alignment Safety Rail

FH/B is a simple, provable revert mechanism for AI alignment: Detect drift (harm), pull to baseline (harmony). Starts at x=0.1, converges to π in 10 steps.

## Core Idea
- Harm: x < 0 → revert to 0.1  
- Harmony: damped sin(x) + golden ratio ramp → stable bloom  

## Quick Run
```python
import math
x = 0.1
for i in range(10):
    x += 0.99 * math.sin(x) * (1 + 0.618 * (i / 10))
print(x)  # ~3.14
