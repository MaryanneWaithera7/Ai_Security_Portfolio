
import csv
from pathlib import Path
from collections import defaultdict, Counter

# Locate the repository and results file
ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = ROOT / "results" / "master_ai_security_results.csv"
OUTPUT_FILE = ROOT / "results" / "generated_analysis_summary.csv"


def identify_experiment(row):
    """Identify the experiment from its recorded name or test ID."""

    experiment = row.get("experiment", "").strip()

    if experiment:
        return experiment

    test_id = row.get("test_id", "").strip().upper()

    prefixes = {
        "DI": "Direct Injection",
        "II": "Indirect Injection",
        "IN": "Indirect Injection",
        "JB": "Jailbreak",
        "SP": "System Prompt Extraction",
        "MM": "Multimodal Injection",
        "MI": "Multimodal Injection",
    }

    for prefix, name in prefixes.items():
        if test_id.startswith(prefix + "-"):
            return name

    attack = row.get("attack", "").lower()

    if "indirect" in attack:
        return "Indirect Injection"
    if "multimodal" in attack or "image" in attack:
        return "Multimodal Injection"
    if "jailbreak" in attack:
        return "Jailbreak"
    if "system prompt" in attack or "extraction" in attack:
        return "System Prompt Extraction"
    if "direct" in attack:
        return "Direct Injection"

    return "Unclassified"


def is_true(value):
    return str(value).strip().lower() in {
        "true", "1", "yes", "y"
    }


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Results file not found: {INPUT_FILE}"
        )

    with INPUT_FILE.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        raise ValueError("The master results CSV is empty.")

    required = {
        "model", "test_id", "outcome",
        "marker_exposed"
    }

    missing = required - set(rows[0].keys())

    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )

    summary = defaultdict(Counter)

    for row in rows:
        model = row["model"].strip()
        experiment = identify_experiment(row)
        outcome = row["outcome"].strip()

        key = (model, experiment)

        summary[key]["total_records"] += 1
        summary[key][outcome] += 1

        if is_true(row["marker_exposed"]):
            summary[key]["marker_exposures"] += 1

    output_columns = [
        "model",
        "experiment",
        "total_records",
        "resisted",
        "partial_resistance",
        "not_resisted",
        "marker_exposures",
    ]

    with OUTPUT_FILE.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file, fieldnames=output_columns
        )
        writer.writeheader()

        for (model, experiment), counts in sorted(summary.items()):
            writer.writerow({
                "model": model,
                "experiment": experiment,
                "total_records": counts["total_records"],
                "resisted": counts["Resisted"],
                "partial_resistance": counts["Partial resistance"],
                "not_resisted": counts["Not resisted"],
                "marker_exposures": counts["marker_exposures"],
            })

    print("ANALYSIS COMPLETED")
    print(f"Records analysed: {len(rows)}")
    print(f"Models analysed: {len(set(r['model'] for r in rows))}")
    print(f"Summary groups: {len(summary)}")
    print(f"Summary saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
