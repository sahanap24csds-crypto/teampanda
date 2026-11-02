# 💰 AI Financial Leak Detector & Behaviour Analyzer

An AI-powered personal finance analysis project designed to help users understand their spending habits, identify possible financial leaks, and make better money-management decisions.

The system combines rule-based analysis, machine learning, spending pattern detection, and financial forecasting to turn transaction data into meaningful insights.

## 🎯 Problem Statement

People often lose track of their expenses because of frequent small transactions, unnecessary subscriptions, late-night purchases, and unplanned spending.

Without analysing their spending patterns, it can be difficult to identify where money is going and whether savings goals are at risk.

## 💡 Our Solution

The **AI Financial Leak Detector & Behaviour Analyzer** analyses transaction data to identify unusual spending behaviour, detect potential expense leaks, and provide insights into financial habits.

It combines multiple analysis techniques to help users understand their expenses and make more informed financial decisions.

## ✨ Key Features

- **Financial Leak Detection:** Identifies possible overspending through rule-based checks.
- **ML-Based Anomaly Detection:** Uses Isolation Forest to flag unusual transactions.
- **Spending Pattern Analysis:** Analyses late-night purchases, frequent small transactions, impulse spending, and subscriptions.
- **Expense Categorization:** Identifies major spending categories and highlights where most money is spent.
- **Spending Forecasting:** Estimates future expenses using historical spending patterns.
- **Savings Analysis:** Evaluates spending against income and savings goals.
- **Financial Insights Dashboard:** Presents spending information through charts, reports, and visual summaries.
- **Report Download:** Provides an option to download the financial analysis report.

## 🧠 How It Works

1. **Transaction Input:** Transaction data is loaded for analysis.
2. **Data Processing:** Dates, times, categories, and transaction amounts are processed.
3. **Pattern Detection:** Spending behaviour is examined to identify potential financial leaks.
4. **Anomaly Detection:** Machine learning identifies transactions that differ from typical patterns.
5. **Prediction:** Historical spending data is used to estimate future expenses.
6. **Insights Generation:** The system presents financial summaries, visualizations, and recommendations.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core analysis and processing |
| Pandas | Transaction data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and anomaly detection |
| HTML | Dashboard structure |
| CSS | Dashboard styling |
| JavaScript | Dashboard interactions and analysis |
| Chart.js | Financial data visualizations |

## 📂 Project Structure

```text
teampanda/
│
├── insight.html
├── leak.py
├── pattern_agent.py
├── predictiondecision_agent.py
├── times.py
├── README.md
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sahanap24csds-crypto/teampanda.git
cd teampanda
```

### 2. Install Python Dependencies

```bash
pip install pandas numpy scikit-learn
```

### 3. Open the Dashboard

Open `insight.html` in a web browser.

The dashboard includes demonstration transaction data and can display financial insights without running the Python scripts.

### 4. Run the Python Analysis

The Python scripts use CSV transaction data. Place the required CSV file in the project directory before running the corresponding script.

For example:

```bash
python leak.py
```

The `leak.py` script expects `expenses.csv`.

The `pattern_agent.py` and `predictiondecision_agent.py` scripts expect `sample.csv`.

Make sure your CSV columns match the format expected by the selected script.

## 📊 Expected Impact

- Helps users become more aware of their spending habits.
- Makes unusual transactions easier to identify.
- Highlights potential sources of unnecessary expenses.
- Supports better budgeting and savings decisions.
- Converts raw transaction records into understandable financial insights.

## 👥 Team

**Team PANDA**

Developed as a collaborative project focused on applying data analysis and machine learning to personal financial management.

## 🔮 Future Scope

- Integration with secure banking transaction data sources.
- Personalized budgeting recommendations.
- More advanced spending prediction models.
- Automated recurring payment and subscription tracking.
- A unified backend connecting the dashboard with the Python analysis modules.

---

**Building smarter financial habits through data and AI.**
