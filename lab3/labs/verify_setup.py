from pathlib import Path

import polars as pl
import pyarrow.parquet as pq


root = Path(__file__).parent / "data"
for month in range(1, 13):
    source = root / f"yellow_tripdata_2024-{month:02}.parquet"
    target = root / f"{month}.parquet"
    if source.exists() and not target.exists():
        source.rename(target)


for month in range(1, 13):
    path = root / f"{month}.parquet"
    metadata = pq.read_metadata(path)
    print(f"{path.name}: {metadata.num_rows:,} rows")
print("Taxi zones:", pl.read_csv(root / "taxi_zone_lookup.csv").height)
print("Polars:", pl.__version__)
print("Total data MB:", sum(p.stat().st_size for p in root.iterdir()) // 1024**2)
