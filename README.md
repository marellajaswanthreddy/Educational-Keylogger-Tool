
# Educational Keylogger Tool (Basic) — Safe Demonstration

A small Python endpoint-logging project demonstrating keyboard event handling, timestamped append-only local logs, and basic log analysis.

## Safety design

This project captures keyboard events **only inside its own visible Tkinter text box**. It does not use global keyboard hooks, run invisibly, capture other applications, or record typed character values. Do not enter passwords or sensitive information.

The requested topic often uses `pynput` for global keyboard hooks. This portfolio-safe implementation deliberately avoids global capture and demonstrates the same core logging concepts within a controlled application.

## Requirements

- Python 3.10 or newer
- Tkinter (usually included with standard Python distributions)

No third-party packages are required.

## Run

From this folder:

```bash
python keylogger_demo.py
```

Click **Start Logging**, type sample text into the visible box, then click **Stop Logging**. Events are appended to `keyboard_demo_log.txt` with local timezone-aware timestamps.

Analyze the log:

```bash
python analyze_log.py
```

## Files

- `keylogger_demo.py` — visible keyboard-event logging demo
- `analyze_log.py` — counts event types in the generated log
- `requirements.txt` — documents dependencies
- `.gitignore` — excludes generated logs and Python cache files

## Concepts demonstrated

1. Keyboard event callbacks within a focused application widget
2. Timestamped append-mode file I/O
3. Session start/stop markers
4. Separating event collection from log analysis
5. Privacy-conscious data minimization

## Limitations

- This is a controlled demonstration, not a system-wide keylogger.
- It records key names, not actual typed characters.
- Tkinter availability depends on the Python installation.
- The log file is plain text; avoid storing sensitive data and delete demo logs when no longer needed.

## Responsible use

Use only on your own device and with informed consent. Do not adapt this project to covertly monitor people or capture credentials.
