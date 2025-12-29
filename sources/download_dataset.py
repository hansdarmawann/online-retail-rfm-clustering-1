from ucimlrepo import fetch_ucirepo
from pathlib import Path
import pandas as pd

# =========================
# Resolve PROJECT ROOT
# =========================
PROJECT_ROOT = Path.cwd()
DATASET_DIR = PROJECT_ROOT / "datasets"
DATASET_DIR.mkdir(exist_ok=True)

RAW_CSV = DATASET_DIR / "online_retail_raw.csv"
RAW_PARQUET = DATASET_DIR / "online_retail_raw.parquet"

# =========================
# Step 1: Download ONCE
# =========================
if not RAW_CSV.exists():
    print("⬇️ Downloading dataset from UCI (first time only)...")
    online_retail = fetch_ucirepo(id=352)
    df_raw = online_retail.data.features
    df_raw.to_csv(RAW_CSV, index=False)
    print("✅ CSV downloaded & saved locally")
else:
    print("📁 Local CSV found, skipping download")

# =========================
# Step 2: Load from local
# =========================
df_raw = pd.read_csv(RAW_CSV)

# =========================
# Step 3: Save as Parquet
# =========================
df_raw.to_parquet(
    RAW_PARQUET,
    index=False,
    compression="zstd"
)

print("✅ Parquet generated successfully")
print("📍", RAW_PARQUET.resolve())
print("📊 Shape:", df_raw.shape)
