```markdown
# CSMA Project

## 📖 Overview
This project is a simple simulation of **Carrier Sense Multiple Access (CSMA)** using Python’s threading and semaphores.  
It demonstrates how multiple senders can transmit messages concurrently while avoiding collisions by coordinating access to a shared channel.

Version **1.1** focuses on **file organization** and adding a basic test setup with `pytest`.

---

## 📂 Project Structure
```
CSMA_project/
├── src/
│   └── main.py          # Core simulation code
├── tests/
│   └── test_main.py     # Basic pytest checks
├── .gitignore           # Ignore cache, venv, editor files
├── README.md            # Project documentation
└── version_log.md       # Version history
```

---

## ▶️ How to Run

### Run the simulation
```bash
python src/main.py
```

### Run tests
```bash
python -m pytest
```

---

## 🛠 Requirements
- Python 3.11+
- pytest (for testing)

Install pytest if needed:
```bash
pip install pytest
```

---

## 📝 Version Log
- **v1.0** → Initial simulation with threading and semaphores.
- **v1.1** → Reorganized files into `src/` and `tests/`, added `.gitignore`, introduced pytest testing.

---

## 🚀 Next Steps
Planned improvements for future versions:
- Separate client and server logic.
- Expand tests to cover concurrency scenarios.
- Add documentation and examples of CSMA behavior.

---

## 👨‍💻 Author
Developed by **Sadman** as part of a learning journey into Python concurrency, project organization, and testing practices.
```

---

This README gives you:
- A clear **overview** of the project.
- Instructions to **run and test**.
- A **version log** so you can track upgrades.
- A roadmap for **future versions**.

