
-- -- Customer Churn Business Analysis

-- -- 1. Total Customers
-- SELECT COUNT(*) AS Total_Customers
-- FROM customer_churn;

-- -- 2. Overall Churn Rate
-- SELECT
--     ROUND(AVG(Churn) * 100,2) AS Churn_Rate_Percentage
-- FROM customer_churn;

-- -- 3. Contract-wise Customer Count
-- SELECT
--     Contract,
--     COUNT(*) AS Customers
-- FROM customer_churn
-- GROUP BY Contract
-- ORDER BY Customers DESC;

-- -- 4. Contract-wise Churn Rate
-- SELECT
--     Contract,
--     ROUND(AVG(Churn)*100,2) AS Churn_Rate
-- FROM customer_churn
-- GROUP BY Contract
-- ORDER BY Churn_Rate DESC;

-- -- 5. Internet Service-wise Churn
-- SELECT
--     InternetService,
--     ROUND(AVG(Churn)*100,2) AS Churn_Rate
-- FROM customer_churn
-- GROUP BY InternetService
-- ORDER BY Churn_Rate DESC;

-- -- 6. Payment Method-wise Churn
-- SELECT
--     PaymentMethod,
--     ROUND(AVG(Churn)*100,2) AS Churn_Rate
-- FROM customer_churn
-- GROUP BY PaymentMethod
-- ORDER BY Churn_Rate DESC;


-- -- 7. Average Monthly Charges by Churn
-- SELECT
--     Churn,
--     ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charges
-- FROM customer_churn
-- GROUP BY Churn;

-- -- 8. Average Tenure by Churn
-- SELECT
--     Churn,
--     ROUND(AVG(tenure),2) AS Avg_Tenure
-- FROM customer_churn
-- GROUP BY Churn;

-- -- 9. Senior Citizen Churn
-- SELECT
--     SeniorCitizen,
--     ROUND(AVG(Churn)*100,2) AS Churn_Rate
-- FROM customer_churn
-- GROUP BY SeniorCitizen;

-- -- 10. Partner vs Churn
-- SELECT
--     Partner,
--     ROUND(AVG(Churn)*100,2) AS Churn_Rate
-- FROM customer_churn
-- GROUP BY Partner;

-- -- 11. Dependents vs Churn
-- SELECT
--     Dependents,
--     ROUND(AVG(Churn)*100,2) AS Churn_Rate
-- FROM customer_churn
-- GROUP BY Dependents;

-- -- 12. Top 10 Highest Paying Customers
-- SELECT
--     tenure,
--     MonthlyCharges,
--     TotalCharges
-- FROM customer_churn
-- ORDER BY TotalCharges DESC
-- LIMIT 10;

-- -- 13. Customers Paying More Than Average
-- SELECT *
-- FROM customer_churn
-- WHERE MonthlyCharges >
-- (
-- SELECT AVG(MonthlyCharges)
-- FROM customer_churn
-- );


-- -- 14. High Risk Customers
-- SELECT *
-- FROM customer_churn
-- WHERE
-- Contract='Month-to-month'
-- AND InternetService='Fiber optic'
-- AND PaymentMethod='Electronic check';

-- -- 15. Monthly Charges Statistics
-- SELECT
-- MIN(MonthlyCharges) AS Minimum,
-- MAX(MonthlyCharges) AS Maximum,
-- ROUND(AVG(MonthlyCharges),2) AS Average
-- FROM customer_churn;

SELECT * FROM customer_churn LIMIT 5;