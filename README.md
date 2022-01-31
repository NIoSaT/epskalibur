# epskalibur
This repository contains example code for the ESORICS 2022 submission eps-kalibur: Weaknesses of two popular covert channel detection methods and a remedy by S. Zillien & S. Wendzel.

## Usage
Each script contains the relevant functions and a simple usage example.

Example run:

    python epssim.py

### compress.py
This script expects a list of packet times (like wireshark would generate) and calculates the compressibility scores for a windowsize of 2000.

### epssim.py
This script expects a list of packet times (like wireshark would generate) and calculates the epsilon-similarity scores for a windowsize of 2000 for 6 different epsilon-thresholds

### inject_fuzzy.py
This script expects a list of inter arrival times and calculates the modified inter arrival times for eps-kalibur
