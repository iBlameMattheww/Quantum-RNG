# QRNG Enclosure CAD Files

This folder contains all of the 3D design files for the enclosure used in the Quantum Random Number Generator project.

## 📦 What's Inside
- `QRNG_Enclosure.stl`: Ready-to-print STL file
- `QRNG_Enclosure.prt`: Original Creo file if you want to tweak or customize the design
- `QRNG_Enclosure.step`: Optional STEP file for compatibility with other CAD software

## 🧠 Why This Enclosure Matters
The enclosure was designed specifically for a breadboarded version of the QRNG circuit. It serves two main purposes:

- **Light isolation** – to block out external light that could mess with the photodiode and affect the randomness
- **Electromagnetic shielding** – to reduce interference from nearby electronics and make results more consistent

There's also a cutout so you can easily route out wires from the breadboard — whether for data output, power, or debugging.

## 🖨️ Printing Tips
- **Layer Height:** 0.2 mm
- **Infill:** 20%
- **Supports:** Not needed
- **Material:** PLA or PETG (your choice)

## ⚠️ Quick Heads-Up for OrcaSlicer (and maybe others)
This part was designed in **inches**, but when I imported the STL into **OrcaSlicer**, it assumed the units were in **millimeters**. As a result, the model came in way too small.

If that happens to you, just **scale the model by 25.4x on all axes** and you’ll be good to go.


