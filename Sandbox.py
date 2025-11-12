import wiplpy.WiplInterface
import wiplpy.WSymbols
import WCMPATCH as WCM  # This will import the patch antenna version of WriteWCM
import os
import subprocess

WIPLDSuitePath = r"C:\\WIPL-D Pro CAD 2024 DEMO"
base_dir = os.path.dirname(__file__)
ProjectPath = os.path.join(base_dir, "Patch")
SymbolsPath = os.path.join(base_dir, "Patch.wsmb")

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

#This opens the project path me thinks
try:
    Project = wiplpy.WiplInterface.WProject(ProjectPath)
    #CAD.Run(ProjectPath)
    print("Project loaded successfully.")
except Exception as e:
    print(f"Error loading project: {e}")
    #CAD.Close()
    exit()

# "gets" the symbols, but seems more like we are setting them
try:
    Symbols = wiplpy.WSymbols.GetSymbols(SymbolsPath)
    print("Symbols loaded successfully.")
    print("Setting symbols...")
    Symbols.AddSymbolByName("StartFrequency", 2.0)
    Symbols.AddSymbolByName("StopFrequency", 3.5)
    Symbols.AddSymbolByName("NumFrequencies", 15)
    print("Symbols set.")
except Exception as e:
    print(f"Error setting symbols: {e}")

Symbols.PrintSymbols()
CAD.Run(ProjectPath)