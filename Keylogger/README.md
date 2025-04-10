# Keylogger Server and Client

This repository contains two Python scripts that implement a basic keylogger system. One script acts as a **keylogger client**, capturing keystrokes on a local machine and sending them to a server. The other script is a **keylogger server**, which listens for incoming connections and logs the keystrokes received from clients into a text file.

**Warning:** This keylogger is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Ensure you have explicit permission before using such software on any system.

## Overview

1. **keylogger.py**: Captures keystrokes on the client machine and sends them to a remote server.
2. **server.py**: Listens for incoming connections from keylogger clients and logs the keystrokes into a text file.

## How It Works

- **keylogger.py**:
  - The script captures every keypress using the `pynput` library.
  - It establishes a connection to a server via a specified IP address and port.
  - The captured keystrokes are sent to the server for logging.
  - Pressing the "Escape" key (`Esc`) will terminate the keylogger client and send a termination message to the server.

- **server.py**:
  - The server listens for incoming connections on a specified port (1234 in this case).
  - It accepts connections and writes the received keystrokes into a file (`<client_ip> keylog.txt`), where `<client_ip>` is the IP address of the connected client.

## Requirements

Before running the scripts, make sure you have the following dependencies installed:

- `pynput`: A Python library to listen for keyboard events.
- `socket`: Python's built-in library for networking.

You can install `pynput` using pip:

```bash
pip install pynput
