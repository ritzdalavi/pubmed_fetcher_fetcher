# 🧬 PubMed Fetcher

A command-line Python tool to fetch and filter research papers from **PubMed** based on custom search queries — specifically identifying papers with at least one **non-academic author** from **pharmaceutical or biotech companies**.

---

## 💡 About This Project

This tool was created to assist in automated research paper mining with a focus on industry collaborations. It makes use of PubMed’s public API to fetch articles and then filters authors using affiliation-based heuristics.

Developed with ❤️ by **Ritesh Dalvi** (MCA - 2025)

---

## 📦 Features

- 🔍 Fetches papers using PubMed’s E-utilities API
- 🧪 Filters authors affiliated with **non-academic institutions**
- 🏢 Extracts company names and email addresses from affiliations
- 📁 Exports filtered data to **CSV**
- 💻 Command-line tool with **Poetry** CLI integration
- 🛠️ Modular code structure (CLI + core logic)

---

## 🚀 Quick Start

### 🖥️ Step 1: Clone this repo

```bash
git clone https://github.com/ritzdalavi/pubmed_fetcher_fetcher.git
cd pubmed_fetcher_fetcher
