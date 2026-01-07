### **Project Title**

**E-Commerce Customer Retention & Churn Analysis**

---

## **1. Objective**

The primary goal of this project is to analyze historical e-commerce transaction data and build a data-driven foundation for identifying customers who are at risk of churn. The project focuses on transforming raw order-level data into meaningful customer-level insights using SQL and Python, followed by predictive modeling and interactive visualization.

---

## **2. Dataset**

This project utilizes the **Olist Brazilian E-Commerce Dataset**, which contains multiple normalized CSV files representing different aspects of an online marketplace.

### Tables Used

| Table       | Description                           |
| ----------- | ------------------------------------- |
| `orders`    | Information about each order placed   |
| `customers` | Customer identifiers linked to orders |
| `payments`  | Payment transactions per order        |
| `reviews`   | Customer feedback and ratings         |

The analysis is centered around **`customer_unique_id`**, which represents an individual real-world customer.

---

## **3. Methodology**

### 3.1 Data Ingestion

* Loaded raw CSV files using pandas
* Verified structure and consistency
* Inserted data into SQLite database for relational operations

---

### 3.2 SQL-Based Data Modeling

* Created a lightweight SQLite database (`ecommerce.db`)
* Performed relational joins across orders, payments, and reviews
* Aggregated data to produce a **customer-level analytical base table**

**Customer Base Table Features**

* `frequency` – total number of orders
* `monetary` – total amount spent
* `recency_days` – days since last purchase
* `avg_review_score` – average review rating
* `churn` – target label

Outcome:
Successfully transformed ~99k orders into ~96k unique customers.

---

### 3.3 Feature Engineering (RFM)

Engineered core analytics features to capture customer engagement:

| Feature       | Meaning                                 |
| ------------- | --------------------------------------- |
| **Recency**   | How recently the customer purchased     |
| **Frequency** | How often the customer purchased        |
| **Monetary**  | Total value contributed by the customer |

* Added behavioral indicators such as repeat-customer flags
* Handled missing values using median/zero imputation
* Validated final dataset distributions

---

### 3.4 Churn Labeling & Baseline Modeling

* Defined churn as a dataset-appropriate proxy variable
* Split data into training and testing sets
* Trained baseline models using **Scikit-Learn**

  * Logistic Regression
  * Random Forest
* Evaluated models using:

  * Confusion Matrix
  * F1-Score

---

### 3.5 Visualization Layer

* Built an **interactive KPI dashboard using Streamlit**
* Implemented Python-based charts with matplotlib
* Displayed:

  * Total customers
  * Churn rate
  * Review distributions
  * Recency and monetary trends

---

## **4. Results**

Key insights obtained from the analysis:

* Most customers are **one-time buyers**, indicating high churn potential
* A small segment of repeat customers drives most revenue
* Long recency gaps strongly correlate with churn risk
* Random Forest performs better than linear baseline for imbalanced churn prediction

---

## **5. How to Run the Project**

1. Clone the repository from GitHub
2. Install dependencies from `requirements.txt`
3. Run the Streamlit dashboard:

```
streamlit run app/dashboard.py
```

---

## **6. Folder Structure**

```
ecommerce-retention-system/
│ ecommerce.db
│ requirements.txt
│ notebooks/
│ app/
│    └ dashboard.py
└ src/
```

---

## **7. Tools & Skills Demonstrated**

**Technical Skills**

* Python (Pandas, NumPy)
* SQL (SQLite)
* Feature Engineering (RFM)
* Machine Learning (Scikit-Learn)
* Data Validation
* Streamlit Dashboard Development
* Python Visualization (Matplotlib)

**Analytical Skills**

* Customer behavior analysis
* Relational data modeling
* Translating data → business decisions
* Understanding class imbalance and churn risk

---

## **8. Conclusion**

This project successfully implements an end-to-end analytics pipeline integrating SQL, Python, machine learning, and dashboarding. The current system provides a strong foundation for further improvements in retention modeling and business simulations.

---

### **Author**

**Ananya Ravikumar**

---

