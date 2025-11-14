import wiplpy
import pkgutil

print("wiplpy modules:")
for m in pkgutil.iter_modules(wiplpy.__path__):
    print(" -", m.name)
