# Expense Ledger

## Documentation & Project Notes
* [Database Architecture](docs/ARCHITECTURE.md)
* [Development Log](docs/LOG.md)

A monolithic financial ledger and expenditure tracking web application built with **Django 5** and **HTMX**. This project processes synthetic expenditure data, automatically categorizes mock transactions via rule matching, and delivers dynamic dashboard analytics without full page reloads.

> **Privacy Note:** This application operates exclusively on synthetic/mock data or manual user inputs. No real-world PII or personal financial statement data is stored or processed.

## Core Features

- **Synthetic Data Ingestion:** Process generated sample CSV statements (fake vendors, randomized amounts).
- **Rule-Based Categorization:** Automatic merchant-to-category mapping using regex patterns and keyword rules.
- **HTMX Reactive UI:** Live filtering by category, date, and merchant without SPA framework overhead.
- **Inline Editing:** Update transaction categories directly in table views using server-driven HTML swaps.
- **Budget Metrics:** Monthly spending summaries, category threshold meters, and burn rate stats.

## Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3.11+, Django 5.x | Web framework, routing, and ORM |
| **Database** | SQLite (Dev) / PostgreSQL | Relational transaction store |
| **Frontend** | Django Templates, HTMX | Server-driven dynamic UI components |
| **Styling** | Tailwind CSS | Utility-first dashboard styling |
| **Data Engine** | Pandas | Vectorized CSV processing and aggregation |
| **Tooling** | Pytest, Mocking, Ruff | Unit testing, synthetic data generation, linting |

<!-- ## Development Roadmap

- [ ] **Phase 1: Project Setup & Data Models**
  - [x] Initialize Django project and app structure
  - [x] Define `Transaction`, `Category`, and `Rule` ORM models
  - [ ] Configure Django Admin panel for manual testing
- [ ] **Phase 2: Synthetic Ingestion & Categorization Engine**
  - [x] Generate mock CSV dataset generator script (`generate_mock_data.py`)
  - [ ] Pandas ingestion pipeline with hash-based deduplication
  - [ ] Pattern-based auto-categorization processor
- [ ] **Phase 3: Interactive HTMX Frontend**
  - [ ] Base dashboard layout with Tailwind CSS integration
  - [ ] Dynamic transaction list with live search and category dropdown filters
  - [ ] HTMX inline category updates on transaction rows
- [ ] **Phase 4: Analytics & Test Suite**
  - [ ] Monthly budget vs. actual spending meters
  - [ ] Pytest test coverage for models, views, and ingestion logic -->

## Development Roadmap

### Phase 1: Project Setup & Data Models
- [x] ~~**Initialize Django project (`config`) and app structure (`expenses`)**~~
- [x] ~~**Define core ORM models (`Transaction`, `Category`)**~~
- [ ] ⏳ **Configure Django Admin panel for manual testing**
- [ ] ⏳ **Define auto-categorization `Rule` ORM model**

### Phase 2: Synthetic Ingestion & Categorization Engine
- [x] ~~**Generate mock CSV dataset generator script (`generate_mock_data.py`)**~~
- [ ] ⏳ **Build Pandas ingestion pipeline with hash-based deduplication**
- [ ] ⏳ **Implement pattern-based auto-categorization processor**

### Phase 3: Interactive HTMX Frontend
- [ ] ⏳ **Set up base dashboard layout with Tailwind CSS integration**
- [ ] ⏳ **Build dynamic transaction list with live search and filters**
- [ ] ⏳ **Enable HTMX inline category updates on transaction rows**

### Phase 4: Analytics & Test Suite
- [ ] ⏳ **Build monthly budget vs. actual spending meters**
- [ ] ⏳ **Write Pytest coverage for models, views, and ingestion logic**