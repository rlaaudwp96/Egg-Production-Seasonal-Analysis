# 🥚 2023 US Egg Production: Seasonal Variance & Statistical Testing

## Business Problem & Context
In 2023, the US agricultural sector experienced significant fluctuations in retail egg prices and consumer demand. A critical question for supply chain managers, agricultural distributors, and policy planners is whether raw production output experiences natural seasonal drop-offs (e.g., severe winter cold or summer heat stress) or if commercial production remains stable year-round.

This project analyzes 2023 USDA table egg production data to test if total egg volume varies significantly across meteorological seasons.

---

## Key Findings & Supply Chain Impact
* **Statistical Verdict:** One-Way ANOVA yielded an **$F$-statistic of 0.017** with a **$p$-value of 0.997** ($\alpha = 0.05$).
* **Conclusion:** Failed to reject the null hypothesis. There is **no statistically significant difference** in average monthly egg production across Spring, Summer, Fall, and Winter in 2023.
* **Business Takeaway:** Commercial layer egg output is remarkably stable across calendar seasons (~278M to ~311M eggs/month on average). Retail price spikes in 2023 were likely driven by demand spikes, avian flu disruptions, or feed cost inflation—not baseline seasonal production drops.

---

## Data & Preprocessing
* **Source:** USDA National Agricultural Statistics Service (NASS) table egg production dataset (2023).
* **Data Cleaning Steps:**
  1. Filtered data strictly for the year 2023 and stripped non-geographic/administrative metadata.
  2. Imputed/removed restricted privacy entries marked as `(D)`.
  3. Cleaned string values and formatted output variables into numeric values.
  4. Mapped months into 4 meteorological seasons (`Winter`: Dec–Feb, `Spring`: Mar–May, `Summer`: Jun–Aug, `Fall`: Sep–Nov).

---

## Methodology & Statistical Testing

### 1. Descriptive Summary
| Season | Observations ($n$) | Mean Monthly Egg Count | Std. Deviation |
| :--- | :---: | :---: | :---: |
| **Spring** | 54 | 286,409,259 | 311,831,916 |
| **Summer** | 54 | 288,750,000 | 313,247,303 |
| **Fall** | 54 | 290,801,852 | 311,770,421 |
| **Winter** | 54 | 278,461,111 | 298,083,870 |

### 2. Assumption Checks
* **Normality Check:** Visualized residual distributions via Normal Q-Q plots. The data showed right-skewness due to high-output producer states (e.g., Iowa, Indiana). Because the sample size ($N = 216$) is sufficiently large, ANOVA was applied per the Central Limit Theorem.

### 3. Hypothesis Test
* **$H_0$:** $\mu_{\text{Spring}} = \mu_{\text{Summer}} = \mu_{\text{Fall}} = \mu_{\text{Winter}}$
* **$H_1$:** At least one seasonal mean differs significantly.
* **ANOVA Results:** $Df = 3$, $\text{Sum Sq} = 4.729 \times 10^{15}$, $F = 0.017$, $p = 0.997$.

---

## Project Structure
```text
├── data/                  # USDA Table Egg production CSV
├── scripts/
│   └── analysis.R         # R script for data cleaning, EDA, and ANOVA testing
├── README.md              # Project documentation
