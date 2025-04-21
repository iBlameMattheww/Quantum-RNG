#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 14:26:26 2025

@author: matthewobrien
"""

import sys
import time
import serial
import math
import random
import numpy as np

# === Config ===
baudrate = 115200
usbPort = '/dev/tty.usbmodem11101'
sampleMax = 1_000_000

# === Test Functions ===
def freq(z, o):
    return abs(z - o) / (z + o)

def entropy(z, o):
    total = z + o
    p0, p1 = z / total, o / total
    return -(p0 * math.log2(p0) + p1 * math.log2(p1))

def transition(bits):
    return sum(bits[i] != bits[i+1] for i in range(len(bits)-1)) / len(bits)

def largestStreak(bits):
    longest = current = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    return longest

def run_tests(name, bitstring):
    zeroCount = bitstring.count('0')
    oneCount = bitstring.count('1')
    print(f"\n Results for {name}")
    print(f"Total 0s: {zeroCount:,}")
    print(f"Total 1s: {oneCount:,}")
    print(f"Frequency imbalance: {freq(zeroCount, oneCount):.4%}")
    print(f"Shannon entropy: {entropy(zeroCount, oneCount):.6f} bits/bit")
    print(f"Bit transitions: {transition(bitstring) * 100:.2f}%")
    print(f"Longest repeated bit streak: {largestStreak(bitstring)}")

# === 1. Collect QRNG bits ===
print("Sampling QRNG from Pico...")
ser = serial.Serial(usbPort, baudrate, timeout=1)
i = 0
cleanBits = ''
start = time.time()

while i < sampleMax:
    chunk = ser.read(1024)
    text = chunk.decode(errors='ignore')
    validBits = ''.join(c for c in text if c in '01')
    cleanBits += validBits
    i += len(validBits)

    # progress bar
    percentage = i / sampleMax
    bar = '█' * int(30 * percentage) + '-' * (30 - int(30 * percentage))
    sys.stdout.write(f"\r[{bar}] {percentage * 100:.0f}% QRNG sampled")
    sys.stdout.flush()

end = time.time()
print(f"\nQRNG sampling time: {end - start:.2f} seconds")


# === 2. Generate Python RNG bits ===
pythonBits = ''.join(str(random.getrandbits(1)) for _ in range(sampleMax))

# === 3. Generate NumPy RNG bits ===
numpyBits = ''.join(str(x) for x in np.random.randint(0, 2, sampleMax))

# === 4. Run All Tests ===
run_tests("QRNG", cleanBits)
run_tests("Python random.getrandbits()", pythonBits)
run_tests("NumPy random.randint()", numpyBits)
