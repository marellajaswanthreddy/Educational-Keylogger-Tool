"""
Educational Keyboard Event Logger (Safe Demo)
Captures key events ONLY inside this application's visible Tkinter text box.
It does not install a global keyboard hook or capture input from other apps.
"""
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

LOG_PATH = Path("keyboard_demo_log.txt")

def timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")

class KeyboardLoggerDemo:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Educational Keyboard Logger — Visible Demo")
        self.root.geometry("760x520")

        heading = tk.Label(
            root,
            text="Educational Keyboard Event Logger",
            font=("Segoe UI", 16, "bold"),
        )
        heading.pack(pady=(14, 4))

        note = tk.Label(
            root,
            text=(
                "Demo mode: only events typed into the box below are logged. "
                "Do not enter passwords or sensitive information."
            ),
            wraplength=700,
            justify="center",
        )
        note.pack(padx=16, pady=(0, 10))

        self.status = tk.StringVar(value="Ready. Click Start Logging to begin.")
        tk.Label(root, textvariable=self.status).pack(pady=4)

        self.text = tk.Text(root, height=13, wrap="word", font=("Consolas", 11))
        self.text.pack(fill="both", expand=True, padx=16, pady=8)
        self.text.insert("1.0", "Type sample text here to generate demo events.\n")
        self.text.bind("<KeyPress>", self.on_keypress)

        buttons = tk.Frame(root)
        buttons.pack(pady=10)

        self.start_button = tk.Button(
            buttons, text="Start Logging", command=self.start_logging, width=16
        )
        self.start_button.pack(side="left", padx=5)

        self.stop_button = tk.Button(
            buttons, text="Stop Logging", command=self.stop_logging,
            width=16, state="disabled"
        )
        self.stop_button.pack(side="left", padx=5)

        tk.Button(
            buttons, text="Open Log Location", command=self.show_log_location, width=18
        ).pack(side="left", padx=5)

        self.logging = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def append_log(self, event_text: str) -> None:
        with LOG_PATH.open("a", encoding="utf-8") as log_file:
            log_file.write(f"{timestamp()} | {event_text}\n")

    def start_logging(self) -> None:
        self.logging = True
        self.status.set(f"Logging demo-window events to: {LOG_PATH.resolve()}")
        self.start_button.configure(state="disabled")
        self.stop_button.configure(state="normal")
        self.text.focus_set()
        self.append_log("SESSION STARTED")

    def stop_logging(self) -> None:
        if self.logging:
            self.append_log("SESSION STOPPED")
        self.logging = False
        self.status.set("Logging stopped.")
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")

    def on_keypress(self, event: tk.Event) -> None:
        if not self.logging:
            return

        # Log key names rather than text content, reducing the chance of collecting
        # sensitive content. This handler is bound only to this visible text widget.
        key_name = getattr(event, "keysym", "Unknown")
        char = getattr(event, "char", "")
        if char and char.isprintable() and not char.isspace():
            description = f"KEY_PRESS key={key_name} printable_character=[redacted]"
        elif char.isspace():
            description = f"KEY_PRESS key={key_name} whitespace=[redacted]"
        else:
            description = f"KEY_PRESS key={key_name}"
        self.append_log(description)

    def show_log_location(self) -> None:
        messagebox.showinfo(
            "Local log file",
            f"Log file path:\n{LOG_PATH.resolve()}\n\n"
            "The file is stored locally in the current working directory."
        )

    def close(self) -> None:
        if self.logging:
            self.stop_logging()
        self.root.destroy()

def main() -> None:
    root = tk.Tk()
    KeyboardLoggerDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
