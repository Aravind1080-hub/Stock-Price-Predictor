from sklearn.linear_model import LinearRegression
import pandas as pd
import yfinance as yf

symbol=input("enter stock symbol:")
data=yf.download(symbol, period="5y")
data.reset_index(inplace=True)
X=data.drop(["Close","Date"],axis=1)
Y=data["Close"]

# model train
model=LinearRegression()
model.fit(X,Y)
Open=float(input("Enter Open value:"))
High=float(input("Enter High value:"))
Low=float(input("Enter Low value:"))
Volumn=float(input("Enter Volume value:"))


new_data = pd.DataFrame([[High,Low,Open,Volumn]], columns=X.columns)

print(f"predicted Closing:{model.predict(new_data)}")
