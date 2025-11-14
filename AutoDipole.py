import os
import wiplpy.WiplInterface as WiplInterface
import wiplpy.WGeometry as WGeometry
import wiplpy.WResults as WResults


# ============================================================
# USER SETTINGS
# ============================================================
WIPLD_DIR = r"C:\WIPL-D Pro CAD 2024 DEMO"     # your WIPL-D installation
ProjectPath = r"C:\Users\dikin\Desktop\Projects\WIPL-D\GITImplementation\AutoDipole"  # without extension
freq_GHz = 3.0
length_m = 0.5
radius_m = 0.001
# ============================================================


# ============================================================
# STEP 1 — Create Geometry
# ============================================================
print("Creating dipole geometry...")

proj_dir = os.path.dirname(ProjectPath)
os.makedirs(proj_dir, exist_ok=True)

# Start geometry object
geo = WGeometry.InitializeGeometry(ProjectPath, WIPLD_DIR)

# Frequency
geo.Frequency = freq_GHz

# Nodes at the ends of dipole
z1 = -length_m / 2
z2 =  length_m / 2

n1 = geo.AddNode(0, 0, z1)
n2 = geo.AddNode(0, 0, z2)

# Create the wire
wire_id = geo.AddWire(n1, n2, radius_m)

# Add generator (feed) at center of wire
gen_id = geo.AddGenerator(wire_id, 0.5)

geo.CloseGeometry()

print("Dipole geometry created.")


# ============================================================
# STEP 2 — Run WIPL-D Pro
# ============================================================
print("Running simulation...")

pro = WiplInterface.InitializeWIPLDSuite(WIPLD_DIR, "wipldpro")
pro.Run(ProjectPath)

print("Simulation complete.")


# ============================================================
# STEP 3 — Extract S11
# ============================================================
print("Extracting S11...")

yzs = WResults.InitializeYZSResults(ProjectPath)

freqs = yzs.GetXData("Frequency")
raw = yzs.GetYData("Sparameter", "RI", "Frequency", {"i": 1, "j": 1})

# Normalize different possible formats
if isinstance(raw[0], complex):
    s11 = list(raw)
elif isinstance(raw[0], (list, tuple)):
    s11 = [complex(r[0], r[1]) for r in raw]
else:
    s11 = [complex(raw[2*i], raw[2*i+1]) for i in range(len(freqs))]

print("S11 extracted.")
for f, s in zip(freqs[:5], s11[:5]):
    print(f"{f:.3f} GHz : {s}")

print("Dipole project complete.")
