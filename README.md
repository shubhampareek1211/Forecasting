# Electricity Consumption Forecasting

This project forecasts hourly electricity consumption using the UCI ElectricityLoadDiagrams2011–2014 dataset. The 15-minute readings were cleaned, converted to hourly values, and used to group 368 active clients into four load-profile clusters. Models were trained on 2011–2013 data and evaluated on 2014.

The analysis compares ARIMA, SARIMAX, Prophet, LSTM, XGBoost, and LightGBM. Tree-based models performed best overall: XGBoost achieved cluster MAPE values of about 3.8%–6.1%, while LightGBM achieved about 4.4%–13.3%. The notebook contains the forecasting analysis; the `n8n workflow` folder contains the database-chat workflow and setup files.

**Data source:** [UCI ElectricityLoadDiagrams2011–2014](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014)
