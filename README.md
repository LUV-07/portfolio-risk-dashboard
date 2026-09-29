# Financial Portfolio & Risk Analytics Dashboard

Hey! This is a personal project where I built an end-to-end dashboard to track investment portfolio performance and risk metrics. 

I wanted something that could pull real market data, calculate risk automatically, and present everything in clean, professional visualizations just like a financial analyst would use.

---

### What it Does
* **Tracks Performance & Risk:** Monitors asset prices, daily returns, drawdowns, and Value-at-Risk (VaR) against market benchmarks.
* **Automates Data Prep:** Uses a Python script to fetch historical data via the `yFinance` API and feed it into the database.
* **Calculates Metrics on the Fly:** Uses custom DAX measures inside Power BI to handle complex financial ratios and year-to-date calculations.
* **Relational Database Model:** Structured using a clean star-schema in PostgreSQL so users can easily slice and dice data across different filters and drill-down views.

---

### Tech Stack
* **Visualization:** Power BI (DAX, Power Query)
* **Data Automation:** Python (Pandas, yFinance)
* **Database:** PostgreSQL

---

### How to Explore
1. Clone the repo or download the `.pbix` file.
2. Open it in Power BI Desktop to interact with the filters, risk metrics, and performance tables.
3. Check out the Python script folder if you want to see how the market data is automatically pulled and structured.
