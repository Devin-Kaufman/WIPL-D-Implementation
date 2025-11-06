import wiplpy.WiplInterface
import wiplpy.WSymbols
import WCM
import os

WIPLDSuitePath = r"C:\\WIPL-D Pro CAD 2024 DEMO"
base_dir = os.path.dirname(__file__)
ProjectPath = os.path.join(base_dir, "Diplow")
SymbolsPath = os.path.join(base_dir, "Diplow.wsmb")

if not os.path.exists(ProjectPath + ".wcm"):
    WCM.WriteWCM(ProjectPath) # This must happen before loading the project
if not os.path.exists(SymbolsPath):
    with open(SymbolsPath, "w") as output_wsmb:
        output_wsmb.write("> 0 1 2 1 2\n")
try:
    CAD = wiplpy.WiplInterface.InitializeWIPLDSuite(WIPLDSuitePath,
    SuiteName="wipldprocad")
    print("WIPL-D Suite initialized successfully.")
except Exception as e:
    print(f"Error initializing WIPL-D Suite: {e}")
    exit()