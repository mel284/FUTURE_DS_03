# 🛒 E-Commerce Conversion & Revenue Performance Analysis

An end-to-end data analytics project analyzing e-commerce user behavior to uncover conversion funnel drop-offs, revenue performance, and cart abandonment insights using **Python** and **Power BI**.

---

## 📌 Overview

This project analyzes real-world e-commerce event data from a multi-category online store. The goal is to help a business understand where users are dropping off in the purchase funnel, which products and brands drive revenue, and how to improve overall conversion rates.

---

## 🎯 Business Questions Answered

- Where are users dropping off in the funnel?
- Which channels bring high-quality leads?
- How can conversion rates be improved?
- Which stages need optimization?
- Which product categories and brands drive the most revenue?
- What is the cart abandonment rate and what does it mean for the business?

---

## 📁 Dataset

- **Source:** [Kaggle — E-Commerce Behavior Data from Multi-Category Store](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
- **Coverage:** November 2019
- **Events tracked:** Views, Cart Additions, Purchases
- **Size:** 771K+ unique visitors | 1.18M sessions

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| Python (Pandas) | Data cleaning, category standardization, funnel aggregation |
| Power BI | Dashboard design, DAX measures, interactive visuals |

---

## 📊 Dashboard Preview

![E-Commerce Dashboard](E-Commerce%20Dashboard.png)

---

## 🔑 Key Findings

| Metric | Value |
|---|---|
| Total Visitors | 771.31K |
| Total Sessions | 1.18M |
| Overall Conversion Rate | 2.38% |
| Total Purchases | 18,356 |
| Total Revenue | $5.46M |
| Cart Abandonment Rate | 69.66% |

- **Conversion funnel:** 1.27M views → 0.06M cart additions → 0.02M purchases — massive drop-off at every stage
- **69.66% cart abandonment** — recovering even 10% of abandoned carts could significantly boost revenue
- **Electronics** dominates revenue (~200M) with the highest conversion rate (~3.5%)
- **Apple and Xiaomi** lead in purchase volume among all brands
- Traffic spike on **Nov 15–16** suggests a promotional event drove a temporary surge

---

## 💡 Recommendations

1. **Reduce cart abandonment** — implement cart recovery emails or exit-intent popups targeting the 69.66% who abandon
2. **Optimize view-to-cart stage** — only 4.7% of viewers add to cart; improve product pages, pricing visibility, and CTAs
3. **Focus on Electronics** — highest revenue and conversion rate; invest more in this category
4. **Investigate Nov 15–16 spike** — identify what caused the traffic surge and replicate it

---

## 🛠️ Skills Demonstrated

- Data cleaning and transformation with **Pandas**
- Funnel analysis and drop-off calculation
- Category label standardization
- **DAX measures** in Power BI
- Business storytelling through data visualization
- Domain knowledge in **E-Commerce analytics**
