# CSMA Project

Overview
--------

Simple demonstration of Carrier Sense Multiple Access (CSMA) using Python threads.

Requirements
------------

This project uses only the Python standard library (`time`, `threading`). No external
packages are required.

Usage
-----

Run the simulation with:

```bash
python main.py
```

Notes
-----

- Tested on Python 3.8+.
- The simulation uses a shared `Semaphore` to coordinate transmissions between threads.

Project Structure
-----------------

```
CSMA_project/
├── main.py        # simulation entrypoint
├── README.md
└──version_log.md

```
