# example_extract_sparams.py
import csv
import math
import wiplpy.WiplInterface as WiplInterface
import wiplpy.WResults as WResults

# --- user edit these paths ---
WIPLDInstallDirectory = r"C:\WIPL-D Pro CAD 2024 DEMO"      # WIPL-D install folder
ProjectPath = r"C:\Users\dikin\Desktop\Projects\WIPL-D\GITImplementation\Patch"      # project path WITHOUT extension
# -------------------------------

# (1) optionally run the project (comment out if results are already present)
pro = WiplInterface.InitializeWIPLDSuite(WIPLDInstallDirectory, "wipldprocad")
pro.Run(ProjectPath)   # runs then closes WIPL-D suite

# (2) open YZS results
yzs = WResults.InitializeYZSResults(ProjectPath)

# (3) get frequency axis
freqs = yzs.GetXData("Frequency")   # X-axis in GHz by default; see GetXUnit()
print("frequencies:", freqs)

def read_sparam(i, j):
    cuts = {"i": i, "j": j}

    raw = yzs.GetYData("Sparameter", "RI", "Frequency", cuts)
    if raw is None:
        return []

    # case A: already complex
    if isinstance(raw[0], complex):
        return list(raw)

    # case B: list of (Re,Im)
    if isinstance(raw[0], (list, tuple)) and len(raw[0]) == 2:
        return [complex(r[0], r[1]) for r in raw]

    # case C: flat interleaved list
    if isinstance(raw[0], (float, int)):
        re = raw[0::2]
        im = raw[1::2]
        return [complex(r, ip) for r, ip in zip(re, im)]

    raise RuntimeError("Unknown format for RI data")
print("Rows:", yzs.GetRows())
print("Cols:", yzs.GetColumns())

# (4) example: read s11 and s21
s11 = read_sparam(1, 1)
   # change indices as appropriate for your port ordering

# (5) compute mag, phase, magdB and write CSV
def write_csv(filename, freqs, complex_list):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["freq_GHz", "Re", "Im", "mag", "phase_deg", "mag_dB"])
        for fr, c in zip(freqs, complex_list):
            mag = abs(c)
            phase = math.degrees(math.atan2(c.imag, c.real))
            magdB = 20.0 * math.log10(mag) if mag > 0.0 else -9999.0
            writer.writerow([fr, c.real, c.imag, mag, phase, magdB])

if s11:
    write_csv("s11.csv", freqs, s11)
    print("Wrote s11.csv")
else:
    print("s11 empty")


