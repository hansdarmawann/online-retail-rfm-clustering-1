from ucimlrepo import fetch_ucirepo
from pathlib import Path
import pandas as pd

# =========================
# Resolve PROJECT ROOT
# =========================
PROJECT_ROOT = Path.cwd()
DATASET_DIR = PROJECT_ROOT / "datasets"
DATASET_DIR.mkdir(exist_ok=True)

RAW_CSV_GZ = DATASET_DIR / "online_retail_raw.csv.gz"

# =========================
# Step 1: Download ONCE
# =========================
if not RAW_CSV_GZ.exists():
    print("⬇️ Downloading dataset from UCI (first time only)...")
    
    online_retail = fetch_ucirepo(id=352)
    df_raw = online_retail.data.features

    df_raw.to_csv(
        RAW_CSV_GZ,
        index=False,
        compression="gzip"
    )

    print("✅ CSV.GZ downloaded & saved locally")
else:
    print("📁 Local CSV.GZ found, skipping download")

# =========================
# Step 2: Load from local
# =========================
df_raw = pd.read_csv(
    RAW_CSV_GZ,
    compression="gzip"
)

print("📍", RAW_CSV_GZ.resolve())
print("📊 Shape:", df_raw.shape)