# Climate-change-Impact-analysis

This project presents a comprehensive climate trend analysis of the Kharar–Ludhiana region, Punjab, India using 35 years (1990–2024) of NASA POWER monthly meteorological data. The study applies Python-based statistical methods, data preprocessing, regression analysis, seasonal decomposition, correlation analysis, and visualization to identify long-term regional climate patterns.

The project was developed as a Bachelor of Engineering (AIT-CSE Big Data Analytics) final-year academic project at Chandigarh University.

Objectives
Analyse 35 years of climate data (1990–2024)
Study 10 meteorological parameters
Detect long-term temperature and rainfall trends
Perform seasonal decomposition using IMD season classification
Generate correlation matrix for inter-variable analysis
Build publication-style visualizations
Create a reproducible Python climate analytics pipeline
Dataset Source

NASA POWER (Prediction of Worldwide Energy Resources)

Coordinates: 30.91°N, 75.81°E (Kharar–Ludhiana Corridor)
Temporal Resolution: Monthly
Duration: January 1990 – December 2024
Parameters Used:
T2M (Mean Temperature)
T2M_MAX (Maximum Temperature)
T2M_MIN (Minimum Temperature)
T2MDEW (Dew Point)
RH2M (Relative Humidity)
PRECTOTCORR (Precipitation)
SFC_SW_DWN (Solar Irradiance)
SFC_UV_INDEX (UV Index)
WS10M_MAX (Max Wind Speed)
WS10M_MIN (Min Wind Speed)
Tools & Technologies
Programming Language:
Python 3.x
Libraries:
Pandas
NumPy
Matplotlib
Seaborn
SciPy
Development Environment:
Jupyter Notebook / VS Code
Methodology
1. Data Collection

Downloaded NASA POWER monthly point data for Kharar–Ludhiana.

2. Data Preprocessing
Removed metadata rows
Replaced missing values (-999 → NaN)
Reshaped dataset into time-series format
Annual and seasonal aggregation
3. Statistical Analysis
Linear Regression
Pearson Correlation
Seasonal Trend Analysis
Monthly Climatology
4. Visualization

Generated:

Annual Average Temperature Trend
Annual Maximum Temperature Trend
Annual Rainfall Trend
Seasonal Temperature Trends
Monthly Temperature Profile
Correlation Heatmap
Monthly Heatmap Distribution
Key Findings
Temperature:
Annual Mean Temperature Trend: −0.040°C/year
Annual Maximum Temperature Trend: −0.053°C/year
Rainfall:
Annual Rainfall Trend: +8.2 mm/year
Wettest Year: 2023
Seasonal:
Strongest cooling observed in Winter
Monsoon remained relatively stable
Correlation:
Solar Irradiance ↔ Maximum Temperature: r = 0.92
Humidity ↔ Rainfall: r = 0.65
Major Conclusion

The Kharar–Ludhiana region shows a localized cooling–wetting climate trend, contrasting with generalized global warming narratives. Increased rainfall, cloud cover, and monsoon intensity may be moderating regional temperatures.

Project Structure
Climate-Change-Impact-Analysis/
│── data/
│   └── NASA_POWER_dataset.csv
│── notebooks/
│   └── climate_analysis.ipynb
│── outputs/
│   ├── temp_trend.png
│   ├── rainfall_trend.png
│   ├── seasonal_analysis.png
│   ├── correlation_heatmap.png
│   └── monthly_heatmap.png
│── report/
│   └── Final_Project_Report.pdf
│── README.md
How to Run
Clone Repository:
git clone https://github.com/your-username/Climate-Change-Impact-Analysis.git
cd Climate-Change-Impact-Analysis
Install Dependencies:
pip install pandas numpy matplotlib seaborn scipy
Run Notebook:
jupyter notebook

Open:

climate_analysis.ipynb
Future Scope
Punjab-wide climate grid analysis
Mann-Kendall trend validation
Change-point detection
Machine Learning forecasting (LSTM / Prophet)
Agricultural productivity correlation
Authors

Ranvir Saini
Royal Singh Rana
Satyam Singh
Anish Sharma

Bachelor of Engineering
AIT-CSE (Big Data Analytics)
Chandigarh University

Acknowledgement

Special thanks to Er. Monica Luthra for academic guidance and mentorship throughout this project.
