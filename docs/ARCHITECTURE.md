# Database Architecture & Models

## Core Schema

### 1. Category
* **name** (`CharField`, unique): name of the budget category.
* **is_income** (`BooleanField`): distinguishes income from expenses.

### 2. Transaction
* **date** (`DateField`): Transaction date.
* **amount** (`DecimalField`): Monetary value.
* **description** (`CharField`): Transaction narrative/merchant.
* **category** (`ForeignKey` -> `Category`): Related category (set to NULL on delete).
* **is_synthetic** (`BooleanField`): Flag to isolate privacy-first test data from live data.