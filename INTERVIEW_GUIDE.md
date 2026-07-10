Q1. Why didn't isnull() detect the missing values initially?
Answer:
Because the missing values were stored as blank strings (" "), not actual NaN values. isnull() only identifies NaN values.

Q2. Why use errors='coerce'?
Answer:
errors='coerce' converts invalid values (such as blank strings or non-numeric text) into NaN, making them easy to detect and handle.

Q3. Why did we drop only 11 rows?
Answer:
The dataset has over 7,000 records, so removing 11 rows has a negligible effect (<0.2%). Dropping them is simpler and safer than imputing TotalCharges.

Q4.Is this dataset imbalanced?
Answer:
No. Although the classes are unequal (73% vs 27%), the imbalance is moderate. Models like Logistic Regression and Random Forest can usually handle this distribution without techniques such as SMOTE. We should first evaluate the model before deciding whether imbalance handling is necessary.

Q5. Why is Accuracy not the best metric here?
Answer
Because customer churn is not equally distributed (about 73% stay and 27% leave). A model can achieve decent accuracy while still missing many churning customers. Precision, Recall, F1-score, and ROC-AUC provide a better evaluation.

Q6. Which metric should the company focus on?
Answer
If the objective is to prevent customer loss, Recall is more important because missing a customer who is about to churn is usually more expensive than contacting a customer who would have stayed.

Q7. Why do we still keep Logistic Regression?
Answer
It is simple and interpretable.
It provides a strong baseline.
Its coefficients help explain feature effects.
More complex models should be compared against it to justify their added complexity.

Q8. Why did Logistic Regression outperform Random Forest?
Answer:
The churn patterns in this dataset are relatively simple and close to linear. Logistic Regression captured these relationships effectively. Random Forest, with default parameters, did not gain enough from modeling nonlinear interactions and therefore achieved lower performance.

Q9. Should we always choose Random Forest?
Answer:
No. The best model should be selected based on validation metrics, not algorithm complexity. Simpler models often generalize better and are easier to interpret.cc

Q10. Why did we use RandomizedSearchCV instead of GridSearchCV?
Answer:
RandomizedSearchCV evaluates only a random subset of parameter combinations, making it much faster when the search space is large. It often finds near-optimal parameters while requiring significantly less computation than GridSearchCV.

Q11. Why did we use scoring="f1" instead of "accuracy"?
Answer:
The churn dataset is imbalanced (about 73% non-churn and 27% churn). Accuracy can be misleading because a model may achieve high accuracy by predicting the majority class. F1-score balances precision and recall, making it more suitable for evaluating churn prediction.

Q12. What does cv=5 mean?
Answer:
It performs 5-fold cross-validation. The training data is split into five parts. In each iteration, four parts are used for training and one part for validation. The final score is the average across all five folds, providing a more reliable estimate of model performance.

Q13. Why did hyperparameter tuning not dramatically improve performance?
Answer:
Hyperparameter tuning can only optimize the existing learning algorithm. If the underlying data patterns are relatively linear or the chosen algorithm is not the best fit, tuning provides only incremental improvements rather than dramatic gains.

Q14. Which model would you deploy?
Answer:
I would deploy Logistic Regression because it achieved the best balance of Recall, F1-score, and interpretability. Although the tuned Random Forest achieved a marginally higher ROC-AUC, Logistic Regression identified more churning customers and is easier to explain to business stakeholders.

Q51. Why not choose the model with the highest ROC-AUC?
Answer:
ROC-AUC measures ranking ability across all thresholds but does not directly reflect business objectives. In churn prediction, Recall and F1-score are often more important because missing customers likely to churn can be more costly than achieving a slightly higher ROC-AUC.

Q16. Why use .copy() instead of assigning directly?
Answer:
Using .copy() creates an independent DataFrame. Without it, both variables reference the same object, so changes made to one DataFrame will also affect the other unintentionally.

Q17. What could happen if .copy() is not used?
Answer:
The original test dataset may be modified by adding prediction-related columns, leading to incorrect analyses, feature mismatch errors during future predictions, and harder-to-debug code.

Q18. Why don't companies always use the default threshold of 0.5?
Answer:
The default threshold of 0.5 is not always optimal. Businesses choose thresholds based on their objectives. For churn prediction, lowering the threshold can increase recall, allowing the company to identify more at-risk customers even if it results in more false positives

Q19. Why calculate Revenue at Risk?
Answer:
Predicting churn alone is not enough. Revenue at Risk helps estimate the financial impact of customer churn and allows the company to prioritize retention efforts where the potential revenue loss is highest.

Q20. Why annual revenue instead of monthly revenue?
Answer:
Businesses generally plan retention strategies based on yearly revenue because it better reflects the long-term value of a customer.

ROI
ROI= (Revenue Saved - Campaign Cost ​×100)/ Campaingn Cost

Q1. Why perform ROI analysis?
Answer:
A machine learning model should support business decisions. ROI analysis estimates whether acting on the model's predictions generates more financial benefit than the campaign costs.

Q2. Why use assumptions?
Answer:
The dataset does not include marketing costs or campaign success rates. Reasonable assumptions allow us to demonstrate how predictive models can be translated into business value. In a real company, these values would come from finance and marketing teams.

Q21. What does a positive coefficient mean?
Answer:
A positive coefficient indicates that as the feature value increases (or the encoded category is present), the probability of churn also increases.

Q22. What does a negative coefficient mean?
Answer:
A negative coefficient indicates that the feature decreases the probability of churn and acts as a protective factor.

Q23. Why is Logistic Regression considered explainable?
Answer:
Unlike many complex models, Logistic Regression provides coefficients for every feature. These coefficients directly indicate whether a feature increases or decreases the likelihood of the target class, making the model easy to interpret.

Q1. Why save the model using Joblib?
Answer:
Joblib serializes the trained model so it can be reused later without retraining, making deployment faster and more efficient.

Q2. Why create predict.py?
Answer:
It separates model inference from notebook experimentation, making the project reusable, deployable, and easier to integrate into applications.

to install all requirements for this project you can run ---> pip install -r requirements.txt