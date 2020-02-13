import datetime
import sys
import csv
from dateutil import tz


def timestamp_normalizer(ts):
    ts_bits = ts.split(" ")

    date_bits = list(map(int, ts_bits[0].split("/")))
    date_bits[2] = date_bits[2] + 2000

    time_bits = list(map(int, ts_bits[1].split(":")))
    if ts_bits[2] == "PM" and time_bits[0] != 12:
        time_bits[0] = time_bits[0] + 12
    if ts_bits[2] == "AM" and time_bits[0] == 12:
        time_bits[0] = 0

    rfc_format = "%Y-%m-%dT%H:%M:%S%z"
    tz_pst = tz.gettz('PST+8')
    tz_est = tz.gettz('EST+5')

    pst = datetime.datetime(year=date_bits[2], month=date_bits[0], day=date_bits[1], hour=time_bits[0],
                            minute=time_bits[1], second=time_bits[2], tzinfo=tz_pst)
    est = pst.astimezone(tz_est)
    return est.strftime(rfc_format)


def zip_normalizer(z):
    normalized_zip = z
    if len(normalized_zip) >= 5:
        normalized_zip = z[:5]
    else:
        while len(normalized_zip) < 5:
            normalized_zip = "0" + normalized_zip
    return normalized_zip


def name_normalizer(name):
    return name.upper()


def duration_to_seconds(d):
    bits = list(map(float, d.split(":")))
    return bits[0] * 3600 + bits[1] * 60 + bits[2]


def main():
    with sys.stdin as csv_file_in:
        with sys.stdout as csv_file_out:
            csv_reader = csv.DictReader(csv_file_in.readlines())
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    csv_writer = csv.DictWriter(csv_file_out, fieldnames=csv_reader.fieldnames)
                    csv_writer.writeheader()
                    line_count += 1
                row["Timestamp"] = timestamp_normalizer(row["Timestamp"])
                row["ZIP"] = zip_normalizer(row["ZIP"])
                row["FullName"] = name_normalizer(row["FullName"])
                row["FooDuration"] = duration_to_seconds(row["FooDuration"])
                row["BarDuration"] = duration_to_seconds(row["BarDuration"])
                row["TotalDuration"] = row["FooDuration"] + row["BarDuration"]
                csv_writer.writerow(row)
                line_count += 1
            csv_file_in.close()
            csv_file_out.close()


if __name__ == "__main__":
    main()
