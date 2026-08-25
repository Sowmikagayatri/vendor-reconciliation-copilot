# Vendor Reconciliation Copilot

## Problem Statement

Vendor statements and internal transaction records ni manually compare cheyyadam time-consuming and error-prone.

This project automates the reconciliation process by comparing internal transaction records with vendor-provided statements and identifying discrepancies such as:

* Missing transactions
* Amount mismatches
* Duplicate transactions

The tool generates a simple reconciliation report for reviewing these issues.

## Tech Stack

* **Language:** Python
* **Libraries:** Pandas
* **Data Format:** CSV
* **Input:** Vendor and internal transaction records
* **Output:** Reconciliation report

## How It Works

1. Reads vendor and internal transaction data from the `data/` folder.
2. Compares transactions using fields such as:

   * Transaction ID
   * Amount
   * Date
   * Vendor Name
3. Identifies mismatches and duplicate records.
4. Generates a reconciliation report.
5. Saves the report as `reconciliation_report.csv`.

## How to Run

Open the project folder in the terminal and run:

```bash
python reconciliation.py
```

The reconciliation report will be generated as:

```text
reconciliation_report.csv
```

## Project Structure

```text
vendor-reconciliation-copilot/
│
├── data/
│   ├── internal_transactions.csv
│   └── vendor_transactions.csv
│
├── reconciliation.py
├── reconciliation_report.csv
└── README.md
```

## Output

The generated report shows the reconciliation results and highlights transactions that need review, such as:

* Matched transactions
* Missing transactions
* Amount mismatches
* Duplicate transactions

## Purpose

This project demonstrates how Python and Pandas can be used to automate a common business reconciliation task and reduce manual effort.
