from pyspark import SparkContext
import csv
from io import StringIO

# --------------------
# Helper: Parse a CSV line safely
# --------------------
def parse_csv(line):
    reader = csv.reader(StringIO(line))
    return next(reader)

# --------------------
# Step 1.1: Extract VIN key-value pairs
# --------------------
def extract_vin_key_value(line):
    try:
        fields = parse_csv(line)
        incident_type = fields[1]
        vin = fields[2]
        make = fields[3]
        year = fields[5]
        return (vin, (incident_type, make, year, fields))
    except Exception as e:
        return ("INVALID", ("E", "", "", []))

# --------------------
# Step 1.2: Propagate make/year to all records per VIN
# --------------------

def populate_make(records):
    records = list(records)
    master_make, master_year = "", ""

    for rec in records:
        if rec[0] == "I":
            master_make = rec[1]
            master_year = rec[2]
            break

    enriched = []
    for rec in records:
        if rec[0] == "A":
            if master_make and master_year:
                fields = rec[3]
                fields[3] = master_make
                fields[5] = master_year
                enriched.append(fields)
            else:
                # DEBUG: log unfilled accident
                print(f"Missing make/year for VIN accident: {rec}")
    return enriched


# --------------------
# Step 2.1: Map make-year to 1
# --------------------
def extract_make_key_value(fields):
    make = fields[3].strip()
    year = fields[5].strip()
    if make and year:
        return (f"{make}-{year}", 1)
    else:
        return ("INVALID", 0)

# --------------------
# Main Spark Job
# --------------------
if __name__ == "__main__":
    sc = SparkContext("local", "AutoInc Spark App")
    raw_rdd = sc.textFile("data.csv")

    vin_kv = raw_rdd.map(lambda x: extract_vin_key_value(x))
    enhance_make = vin_kv.groupByKey().flatMap(lambda kv: populate_make(kv[1]))

    make_kv = enhance_make.map(lambda x: extract_make_key_value(x))
    result = make_kv.filter(lambda x: x[0] != "INVALID").reduceByKey(lambda x, y: x + y)


    result.map(lambda x: f"{x[0]},{x[1]}").saveAsTextFile("output")
    print("✅ Output written to ./output/")
    
    sc.stop()
