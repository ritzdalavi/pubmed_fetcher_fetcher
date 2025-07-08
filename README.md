# PubMed Fetcher

A command-line tool to fetch PubMed research papers with at least one non-academic author (from pharmaceutical/biotech companies).

## 📦 Features

- Uses PubMed's API
- Filters authors based on non-academic affiliation
- Outputs data to CSV or console

## 🚀 Usage

```bash
poetry install
poetry run get-papers-list "diabetes treatment" -f results.csv
```

## 🧰 Options

- `-h`, `--help`: Show help message
- `-d`, `--debug`: Enable debug logging
- `-f`, `--file`: Save output to CSV file

## 🧠 Heuristics

- Authors with affiliations that **do not** include: university, college, institute, school, hospital
- Email parsing via regex from affiliation strings
