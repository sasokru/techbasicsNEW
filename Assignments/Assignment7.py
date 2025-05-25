import csv
import random
import statistics

INPUT_FILE = 'Technical Basics I_2025 - Sheet1.csv'
OUTPUT_FILE = 'grades_calculated.csv'

def get_week_columns(headers):
    return [col for col in headers if col.startswith("week") and col.lower() != "week6"]

def read_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            week_columns = get_week_columns(reader.fieldnames)
            return data, reader.fieldnames, week_columns
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None, None, None

def fill_missing_with_random(data, week_columns):
    for row in data:
        for week in week_columns:
            value = row.get(week, "").strip()
            if value == '' or value == '-' or value.lower() == 'nan':
                row[week] = str(random.randint(0, 3))
    return data

def calculate_scores(data, week_columns):
    for row in data:
        scores = []
        for week in week_columns:
            try:
                points = int(float(row[week]))
                scores.append(points)
            except:
                continue
        best_10 = sorted(scores, reverse=True)[:10]
        row["Total Points"] = sum(best_10)
        row["Average Points"] = round(statistics.mean(scores), 2) if scores else 0.0
    return data

def write_csv(filename, fieldnames, data):
    if "Total Points" not in fieldnames:
        fieldnames += ["Total Points", "Average Points"]
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def print_averages(data, week_columns):
    streams = {'A': [], 'B': []}
    weekly_scores = {week: [] for week in week_columns}

    for row in data:
        stream = row.get("Stream", "").strip().upper()
        avg = float(row.get("Average Points", 0))
        if stream in streams:
            streams[stream].append(avg)

        for week in week_columns:
            try:
                value = int(float(row[week]))
                weekly_scores[week].append(value)
            except:
                continue

    print("\nAverage Points per Stream:")
    for s, averages in streams.items():
        if averages:
            avg_stream = sum(averages) / len(averages)
            print(f"Stream {s}: {avg_stream:.2f}")
        else:
            print(f"Stream {s}: No data")

    print("\nAverage Points per Week:")
    for week, scores in weekly_scores.items():
        if scores:
            avg_week = sum(scores) / len(scores)
            print(f"{week}: {avg_week:.2f}")
        else:
            print(f"{week}: No data")
