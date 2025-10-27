# 🍦 Ice Cream Sales Prediction App

An interactive web application that predicts ice cream sales based on temperature using **Polynomial Regression**. Built with Flask, Scikit-learn, and deployed on Render.

## 🌐 Live Demo
**Live Application:** [https://ice-cream-sales-jv5w.onrender.com](https://ice-cream-sales-jv5w.onrender.com)

## 📊 Project Overview

This machine learning application analyzes the relationship between temperature and ice cream sales using advanced polynomial regression techniques. The app provides:

- **Interactive predictions** for ice cream sales at any temperature
- **Multiple polynomial degrees** (2-5) for model optimization
- **Real-time visualizations** with regression curves
- **Model performance metrics** (R² score, MSE)
- **Professional dashboard** with data analytics

## 🚀 Features

### 🔍 Data Analysis
- 49 data points of temperature vs. ice cream sales
- Statistical summary and correlation analysis
- Interactive data visualization

### 🤖 Machine Learning
- **Polynomial Regression** with degrees 2-5
- Real-time model training and evaluation
- R² scores and Mean Squared Error metrics
- Interactive model comparison

### 💻 Interactive Web Interface
- Temperature input for instant predictions
- Dynamic chart updates
- Model degree selection
- Responsive design for all devices

## 🛠️ Technology Stack

**Backend:**
- Python 3.11
- Flask
- Scikit-learn
- Pandas, NumPy
- Matplotlib

**Frontend:**
- HTML5, CSS3, JavaScript
- Responsive design
- Interactive charts

**Deployment:**
- Render
- Gunicorn
- GitHub

## 📈 Model Performance

The polynomial regression model achieves:
- **R² Score:** ~84% (Degree 2)
- **Accurate predictions** across temperature ranges
- **Non-linear relationship** capture between temperature and sales

## 🎯 How to Use

1. **View the Analysis**: See the scatter plot with polynomial regression curve
2. **Adjust Model**: Select different polynomial degrees (2-5)
3. **Make Predictions**: Enter any temperature to get sales predictions
4. **Compare Performance**: View R² scores and MSE for each model

## 📁 Project Structure

```
polynomial regression/
└── Ice Cream sales/
    ├── app.py                 # Main Flask application
    ├── wsgi.py               # WSGI entry point
    ├── requirements.txt      # Python dependencies
    ├── runtime.txt          # Python version specification
    ├── Ice_cream_selling_data.csv  # Dataset
    ├── templates/
    │   └── index.html       # Main web interface
    └── static/
        └── style.css        # Styling
```

## 🚀 Local Development

### Prerequisites
- Python 3.11+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Pinkkygold/Machine-Learning-projects.git
cd "Machine-Learning-projects/polynomial regression/Ice Cream sales"
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Visit** `http://localhost:5000`

## 🌐 Deployment

The app is deployed on **Render** with the following configuration:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn wsgi:app`
- **Python Version:** 3.11.4

## 📊 API Endpoints

- `GET /` - Main application interface
- `POST /predict` - Make sales predictions
- `POST /update_model` - Change polynomial degree
- `GET /api/data` - Raw data JSON
- `GET /api/stats` - Statistical summary
- `GET /health` - Health check

## 🔮 Future Enhancements

- [ ] Additional regression models (Random Forest, SVM)
- [ ] Time-series analysis for seasonal trends
- [ ] Advanced feature engineering
- [ ] User authentication for saved predictions
- [ ] Export functionality for reports

## 👨‍💻 Author

**Pinkkygold**
- GitHub: [@Pinkkygold](https://github.com/Pinkkygold)
- Project: [Machine Learning Projects](https://github.com/Pinkkygold/Machine-Learning-projects)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/Pinkkygold/Machine-Learning-projects/issues).

---

⭐ **Star this repo if you find it helpful!**
