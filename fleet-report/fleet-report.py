import csv
import sys
from pathlib import Path

CSV_PATH = Path(__file__).with_name("car_fleet.csv")

def load_fleet(path: Path) -> list[dict]:
    """Read the fleet CSV into a list of typed dictionaries."""
    vehicles =[]
    try:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            for line_no,row in enumerate(reader, start=2):
                try:
                    vehicles.append({
                        "vin": row["vin"],
                        "make": row["make"],
                        "model": row["model"],
                        

                    })