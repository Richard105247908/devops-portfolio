# fleet-report

Reads a CSV of vehicles, validates each row, and prints the fleet data.

## Usage
python fleet_report.py

```bash
python fleet_report.py
```

## Example output

```
vin: TMX20122
make: AnyCompany Motors
...
-----
```

## What I learned
- Reading CSVs with `csv.DictReader`
- Converting types and handling bad rows without crashing

