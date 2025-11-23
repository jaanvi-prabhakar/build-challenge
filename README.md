# Build Challenge (Python)

Producer–Consumer (Concurrency) + CSV Sales Analysis (Functional Programming)

This repository contains solutions for both required assignments in the Build Challenge.  
All implementations are written in Python 3, fully tested with pytest, and organized into isolated modules.

## Contents

- [Assignment 1: Producer–Consumer](#assignment-1-producerconsumer)
- [Assignment 2: CSV Sales Analysis](#assignment-2-csv-sales-analysis)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Assignments](#running-the-assignments)
- [Running Tests](#running-tests)
- [Sample Output (Required)](#sample-output)
- [Dataset Used](#dataset-used)

## Assignment 1: Producer–Consumer

### Objectives

- Thread synchronization
- Blocking queue
- Wait/notify mechanism
- Concurrent data transfer

### Overview

Implements a classic producer–consumer pattern using:

- `threading.Thread`
- `queue.Queue` for thread-safe communication
- Poison-pill termination
- Clean, testable `run_demo()` interface

### Files

assignment1/src/producer_consumer.py
assignment1/tests/test_producer_consumer.py

## Assignment 2: CSV Sales Analysis

### Objectives

- Functional programming in Python
- Map/filter/reduce
- Aggregations & grouping
- Stream-like operations

### Overview

Performs analysis on the Superstore Sales Dataset, including:

- Total sales
- Sales by region
- Sales by category
- Top-selling product
- Profit by region
- Daily sales aggregation

All logic is pure, testable, and modular.

### Files

assignment2/src/data_analysis.py
assignment2/tests/test_data_analysis.py
assignment2/data/sales.csv

## Project Structure

```
build-challenge/
│
├── assignment1/
│ ├── src/
│ │ └── producer_consumer.py
│ └── tests/
│ └── test_producer_consumer.py
│
├── assignment2/
│ ├── data/
│ │ └── sales.csv
│ ├── src/
│ │ └── data_analysis.py
│ └── tests/
│ └── test_data_analysis.py
│
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```
git clone <your_repo_url>
cd build-challenge
```

### 2. Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

## Running the Assignments

### Assignment 1

```
python3 assignment1/src/producer_consumer.py
```

### Assignment 2

```
python3 -c "from assignment2.src.data_analysis import run_all_analysis;
run_all_analysis('assignment2/data/sales.csv')"
```

## Running Tests

### Run extire test suite

```
pytest -q
```

### Run tests for a single assessment:

```
pytest assignment1/tests -q
pytest assignment2/tests -q
```

## Sample Output

### Assignment 1 Sample Output (Example)

```
Produced: A
Consumed: A
Produced: B
Consumed: B
Produced: C
Consumed: C
Produced: D
Consumed: D
Final destination: ['A', 'B', 'C', 'D']
```

### Assignment 2 Sample Output (Example)

```
=== Superstore Sales Analysis ===

Total Sales: 2,297.97

Sales by Region:
  West: 725.45
  East: 1,037.83
  South: 534.69

Sales by Category:
  Furniture: 614.51
  Technology: 1,098.06
  Office Supplies: 585.40

Top Selling Product (by Quantity): Stapler Set

Profit by Region:
  West: 120.33
  East: 300.54
  South: 92.87

Daily Sales:
  01/01/2025: 585.42
  01/02/2025: 412.15
  01/03/2025: 299.91

=== End of Analysis ===

```

## Dataset Used

Superstore Sales Dataset
Source: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

Included as assignment2/data/sales.csv for reproducibility.
