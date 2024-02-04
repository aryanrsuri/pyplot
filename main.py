import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import os
import pandas as pd

LABELS = ["angle", "intensity"]
plt.figure(figsize=(6,6))
for fn in os.listdir("./xrd"):
    try:
        df = pd.read_csv(os.path.join("./xrd", fn), sep=" ", names=LABELS)
        with plt.style.context('science'):
            plt.plot(df["angle"], df["intensity"],   label=fn[:-4])
    except:
        print("error reading csv")

plt.legend()
plt.tight_layout()
plt.xlabel(r"Angle $2\theta$")
plt.ylabel(r"Intensity")
plt.savefig("./out/Diffractogram.svg")
plt.show()

