# Checklist

- Does each failure point to the scenario that failed?
- Are `got` and `want` clear and ordered consistently?
- Are table rows cohesive and named?
- Are helpers using `t.Helper()`?
- Is setup scoped to the tests that need it?
- Does the test avoid depending on real time, randomness, network, or ordering?
- Is `t.Fatal` used only when continuing is invalid?
- Does the benchmark exclude setup from the measured section?
