import sys
import importlib
import matplotlib.pyplot as plt


def check_package(name):
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - ready")
        return module
    except ImportError:
        print(f"[MISSING] {name} - not installed")
        return None


print("LOADING STATUS: Loading programs...")
print("Checking dependencies:")

pandas = check_package("pandas")
numpy = check_package("numpy")
matplotlib = check_package("matplotlib")
requests = check_package("requests")

# Se faltar algo essencial
if not all([pandas, numpy, matplotlib]):
    print("\nERROR: Missing core dependencies.")
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("Or with Poetry:")
    print("  poetry install")
    sys.exit(1)


print("\nAnalyzing Matrix data...")

data = numpy.random.normal(loc=0, scale=1, size=1000)

print("Processing 1000 data points...")

df = pandas.DataFrame(data, columns=["signal"])
stats = df.describe()

print("\nData Summary:")
print(stats)

print("\nGenerating visualization...")

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color="green", alpha=0.7)
plt.title("Matrix Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

output_file = "matrix_analysis.png"
plt.savefig(output_file)

print("\nAnalysis complete!")
print(f"Results saved to: {output_file}")

print("\nPackage versions:")
for pkg in ["pandas", "numpy", "matplotlib"]:
    mod = importlib.import_module(pkg)
    print(f"{pkg}: {getattr(mod, '__version__', 'unknown')}")
