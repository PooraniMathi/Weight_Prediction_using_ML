# Weight Prediction Using Linear Regression Machine Learning Algorithm
<img width="952" height="623" alt="image" src="https://github.com/user-attachments/assets/0ce4299a-00a8-48ff-989d-56a682d3ce31" />

________________________________________
Objective:
Developed a machine learning model to predict a person’s weight (in kilograms) based on their height (in centimeters) using simple linear regression.
________________________________________
Dataset:
The dataset consisted of height and weight measurements collected from Kaggle. The height values were recorded in centimeters and the corresponding weights in kilograms.
________________________________________
Data Processing:
The data was cleaned and normalized. Height values were validated to ensure they fall within a reasonable human range (0–300 cm). Weight values were converted to kilograms when needed.
________________________________________
Model Development:
Used simple linear regression to model the relationship between height and weight. The dataset was split into training and testing sets with an 80/20 ratio. The model was trained on the training set and evaluated on the test set using metrics such as mean squared error (MSE) .
________________________________________
Results:
Predictions made on new height inputs provide estimated weights with reasonable accuracy.
________________________________________
Deployment / Frontend:
If you built a frontend or API, mention it.
Developed a Flask-based web application with a clean and responsive UI, allowing users to input height values and receive predicted weight results instantly. The input form includes validation to ensure heights are within valid ranges.
________________________________________
Technologies Used:
•	Python, scikit-learn (for modeling)
•	Flask (for backend API)
•	HTML, CSS, JavaScript (for frontend)
•	Jupyter Notebook (for data exploration)
________________________________________
Summary Paragraph:
This project implements a simple linear regression model to predict human weight based on height measurements. After preprocessing the dataset to ensure data quality, the model was trained and evaluated achieving good predictive performance. A user-friendly Flask web app was developed to allow real-time weight prediction with built-in form validation to enhance user experience. This project demonstrates foundational skills in machine learning, data preprocessing, and web development.
