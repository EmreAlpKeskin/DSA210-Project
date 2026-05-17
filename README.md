# What Factors Affects Movies Success Analysis (DSA210 Project)

---

## 1. Motivation

As someone who enjoys watching movies, I’ve always wondered why some films become extremely successful while others fail despite having high budgets.

The main research question of this project is:

What factors determine whether a movie becomes financially successful?

---

## 2. Data Source

The dataset used in this project is the TMDB 5000 Movies Dataset, which contains detailed information about movies including financial performance, popularity, and audience-related metrics.

### Data Preprocessing

Before analysis, the dataset was cleaned and preprocessed to ensure consistency and usability. This included handling missing values, selecting relevant variables, and focusing on numerical features suitable for statistical and machine learning analysis.

After preprocessing:

- Total observations: **~3229 movies**
- Selected features:
  - **budget** → production cost of the movie
  - **revenue** → total revenue generated
  - **popularity** → popularity score provided by TMDB
  - **vote_average** → average rating of the movie
  - **vote_count** → number of votes (audience engagement)

---

### Definition of Success

In this project, a movie is defined as **successful if its revenue exceeds its budget (revenue > budget)** for making classification easier.

---

## 3. Exploratory Data Analysis (EDA)

---

### 3.1 Budget vs Revenue Relationship

![Revenue vs Budget](RevenuevsBudget_Realationship.png)

**Findings:**
- Strong positive relationship observed
- Correlation ≈ **0.70**
- Movies with larger budgets generally tend to generate more revenue

**Interpretation:**

This graph shows that movies with higher budgets usually earn more money at the box office. In many cases, expensive movies have larger productions, stronger marketing, better visual effects, and wider releases, which may help them reach larger audiences.

However, the graph also shows that budget alone does not fully determine success. Some high-budget movies still earn relatively low revenue, while some lower-budget movies perform surprisingly well. This suggests that movie success depends on many different factors such as audience interest, marketing, timing, reviews, and popularity.

The wide spread of the points in the graph is important because it shows that financial investment alone is not enough to guarantee success.

---

### 3.2 Correlation Matrix

![Correlation Between Variables](CorrelationMatrix.png)

**Key Values:**
- budget vs revenue → **0.71**
- revenue vs vote_count → **0.76**
- popularity vs vote_count → **0.69**
- vote_average has relatively weaker relationships

**Interpretation:**

The correlation matrix helps show which variables tend to move together. The strongest relationship in the matrix is between revenue and vote_count. This may indicate that movies receiving more audience attention and interaction also tend to generate more revenue.

Budget also has a strong relationship with revenue, but not as strong as vote_count. This suggests that audience engagement may be even more important than production cost when discussing movie success.

At the same time, correlation values only show relationships between variables. They do not prove that one variable directly causes another.

---

### 3.3 Revenue Distribution

![Revenue Distribution](Revenue_Distribution.png)

**Findings:**
- Highly right-skewed distribution
- Most movies generate relatively low revenue
- A small number of movies generate extremely high revenue

**Interpretation:**

This graph shows that movie revenue is distributed very unevenly. Most movies earn relatively small amounts of revenue, while only a small number of movies become extremely successful and generate very large profits.

This creates a right-skewed distribution, meaning that a few very successful movies pull the distribution toward higher values. This is important because many statistical methods work better when data is more balanced or normally distributed.

Because of this skewness, the results of the analysis should be interpreted carefully. Extremely successful movies may influence averages and correlations more strongly than typical movies.

---

### 3.4 Genre Analysis

I also briefly looked at movie genres to see if different genres showed different success patterns.

Genres such as Action, Drama, and Comedy appeared more frequently in the dataset compared to others. I also noticed that some genres seemed to have higher success rates than others.

However, genre analysis was not the main focus of this project, since the analysis mainly concentrated on numerical variables like budget, revenue, popularity, and vote-related features. A more detailed genre-based analysis could be done in future work.

---

## 4. Machine Learning Analysis

---

### 4.1 Linear Regression

Used to predict movie revenue using numerical variables.

**Results:**
- R² score: **0.657**
- RMSE: **~131 million**

**Interpretation:**

The regression model explains around 65% of the variation in movie revenue. This means the selected variables provide useful information about financial performance, but they still cannot fully explain why movies succeed or fail.

A large amount of variation remains unexplained, which suggests that other important factors are missing from the dataset. For example, marketing campaigns, release timing, competition with other movies, social media trends, or critic reviews may also strongly influence revenue.

Overall, the model performs reasonably well, but movie success appears to be a more complex problem than can be explained by a few numerical variables alone.

---

### 4.2 Decision Tree Classification

Used to classify movies as successful or unsuccessful.

**Results:**
- Accuracy: **~79.8%**

**Interpretation:**

The decision tree model achieved relatively strong classification performance. This suggests that combining multiple variables gives more useful information than relying on only one feature.

At the same time, the model may also be influenced by the imbalance in the dataset, since successful movies are much more common than unsuccessful ones. Because of this, accuracy alone may not fully represent model performance.

---

### 4.3 Cross-Validation and Hyperparameter Tuning

To improve model reliability, cross-validation and hyperparameter tuning were applied to the Decision Tree model.

**Methods Used:**
- 5-fold cross-validation
- GridSearchCV for tuning maximum tree depth

**Results:**
- Average cross-validation score: approximately **0.79**
- Best parameter found: **max_depth = 4**

**Interpretation:**

Cross-validation helps evaluate whether the model performs consistently across different subsets of the dataset. The results suggest that the Decision Tree model remains relatively stable and generalizes reasonably well.

Hyperparameter tuning was used to test multiple tree depths and identify the most suitable model complexity. The results indicate that a moderate tree depth provides the best balance between learning useful patterns and avoiding overfitting.

---

### 4.4 Feature Importance

![Feature Importance](Decision_Tree_Importance_of_Feature.png)

**Results:**
- vote_count → **~0.77**
- budget → **~0.18**
- vote_average → **~0.03**
- popularity → **~0.009**

**Interpretation:**

The feature importance results show that vote_count is by far the strongest variable associated with movie success. This may suggest that audience attention and interaction are closely related to financial performance.

Budget is still an important factor, but its contribution appears much smaller compared to audience-related features. This finding supports the idea that audience engagement may play a larger role than production cost alone.

---

## 5. Hypothesis Testing

---

### Hypothesis:

- H0: Budget has no effect on revenue
- H1: Budget affects revenue

---

### 5.1 Statistical Evidence

- Pearson correlation ≈ **0.70**
- Strong positive linear association observed

**Decision:**
The null hypothesis (H0) is rejected.

**Interpretation:**

The hypothesis test suggests that movies with larger budgets generally tend to generate higher revenue. In other words, there is a strong positive relationship between budget and revenue in the dataset.

However, this does not mean that increasing a movie’s budget will automatically make it successful. The analysis only shows that these variables are associated with each other.

In addition, the revenue distribution is highly skewed, meaning that a small number of extremely successful movies may influence the statistical results more strongly than average movies. Because of this, the findings should be interpreted carefully rather than as direct cause-and-effect conclusions.

---

### 5.2 Budget Distribution by Success

![Budget Distribussion by Succes Boxplot](Budget_Distribussion_by_Succes.png)

**Findings:**
- Successful movies have higher median budgets
- Unsuccessful movies concentrated at lower budgets
- Overlap exists

**Interpretation:**

The boxplot shows that successful movies generally tend to have larger budgets compared to unsuccessful movies. However, there is still a noticeable overlap between the two groups.

This overlap is important because it suggests that budget alone cannot perfectly separate successful and unsuccessful movies. Some lower-budget movies still become successful, while some expensive movies fail financially.

---

### 5.3 Success Distribution

![Success vs Failure](Successful_vs_Unsuccessful_movies.png)

**Results:**
- Successful: **2438 (~75.5%)**
- Unsuccessful: **791 (~24.5%)**

**Interpretation:**

The dataset contains a much larger number of successful movies compared to unsuccessful ones. This imbalance is important because machine learning models may become biased toward the majority class.

As a result, model accuracy should be interpreted carefully, since predicting the majority class becomes easier in imbalanced datasets.

---

## 6. Results & Discussion

- The overall analysis suggests that movie success is influenced by multiple factors rather than a single variable.

- Budget is strongly associated with revenue, and movies with larger budgets generally tend to earn more money. However, the analysis also shows that budget alone cannot fully explain success. Many high-budget movies still perform poorly, while some lower-budget movies perform much better than expected.

- One of the most important findings in this project is the role of audience engagement. Variables such as vote_count showed stronger relationships with revenue than some other features. This may suggest that audience attention and interaction are closely connected to financial success.

- The machine learning models also support these findings. Both the regression and classification models achieved reasonable performance, but neither model could perfectly explain or predict movie success. This further suggests that movie performance depends on many complex and unpredictable factors.

**Key Insight:**
Audience engagement is more important than budget alone.

---

## 7. Conclusion

This project analyzed the key factors influencing movie success using both statistical methods and machine learning techniques.

The results consistently indicate that budget has a strong positive relationship with revenue, supported by correlation (~0.70) and visual analysis. However, budget alone does not fully explain success due to high variability.

The linear regression model (R² ≈ 0.65) shows moderate predictive power, indicating that additional variables influence outcomes. The decision tree model (accuracy ≈ 79.8%) confirms that combining features improves classification performance.

The most important finding is that **vote_count (~0.77 importance)** is the dominant feature. This suggests that **audience engagement plays a larger role than budget** in determining success.

Overall:
- Budget matters
- Audience matters more
- Success is multi-factorial

---

## 8. Limitations & Future Work

### Limitations:
- Dataset size (~3000 movies)
- Missing variables (marketing, timing)
- Simplified success definition (revenue > budget)
- The results in this project show relationships between variables, but they should not be interpreted as direct cause-and-effect conclusions.
- In future work, more factors such as genre, runtime, release timing, and production companies could be included to better understand what makes a movie successful.

---

## 9. AI Assistance

AI assistance tools were used during some parts of the project for debugging code, improving and correcting writing, organizing the notebook structure, and getting suggestions about possible model choices and analysis improvements.