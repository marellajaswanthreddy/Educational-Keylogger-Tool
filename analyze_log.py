"""Summarize the safe educational keyboard demo log."""
from collections import Counter
from pathlib import Path
import re

LOG_PATH = Path("keyboard_demo_log.txt")

def main() -> None:
    if not LOG_PATH.exists():
        print(f"No log found at {LOG_PATH.resolve()}")
        print("Run keylogger_demo.py and create a short demo session first.")
        return

    counts: Counter[str] = Counter()
    total_lines = 0
    timestamp_pattern = re.compile(r"^(\S+) \| (.*)$")

    with LOG_PATH.open("r", encoding="utf-8") as log_file:
        for raw_line in log_file:
            line = raw_line.rstrip("\n")
            if not line:
                continue
            total_lines += 1
            match = timestamp_pattern.match(line)
            if not match:
                counts["MALFORMED_LINE"] += 1
                continue
            event = match.group(2)
            if event.startswith("KEY_PRESS"):
                counts["KEY_PRESS"] += 1
            elif event == "SESSION STARTED":
                counts["SESSION STARTED"] += 1
            elif event == "SESSION STOPPED":
                counts["SESSION STOPPED"] += 1
            else:
                counts["OTHER"] += 1

    print("EDUCATIONAL KEYBOARD DEMO — LOG SUMMARY")
    print("=" * 42)
    print(f"Log file: {LOG_PATH.resolve()}")
    print(f"Non-empty lines: {total_lines}")
    for label, count in sorted(counts.items()):
        print(f"{label}: {count}")
    print("\nPrivacy note: this demo logs key names only and redacts character values.")

if __name__ == "__main__":
    main()
