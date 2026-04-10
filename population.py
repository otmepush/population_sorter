"""
Population Sorter
Format of input file: country name, area, population
"""
def read_population_file(filepath: str) -> list[dict]:
    if not filepath.endswith(".txt"):
        raise ValueError(
            f"File must have .txt extension, got: {filepath}"
        )
 
    records = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 3:
                raise ValueError(
                    f"Line {line_num} has wrong format: '{line}'. "
                    "Expected: country, area, population"
                )
            country, area_str, population_str = parts
            try:
                area = float(area_str)
                population = int(population_str)
            except ValueError:
                raise ValueError(
                    f"Line {line_num}: area and population must be "
                    f"numbers, got area='{area_str}', "
                    f"population='{population_str}'"
                )
            records.append({
                "country": country,
                "area": area,
                "population": population,
            })
    return records


def sort_by_area(records: list[dict], ascending: bool = True) -> list[dict]:
    return sorted(records, key=lambda r: r["area"], reverse=not ascending)
 
def sort_by_population(
    records: list[dict], ascending: bool = True
) -> list[dict]:
    return sorted(
        records, key=lambda r: r["population"], reverse=not ascending
    )