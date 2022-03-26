from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, csv, os, statistics

stock = input("Enter stock ticker: ")

s = Service("/Users/kushgoswami/Documents/PythonPrograms/chromedriver")

driver = webdriver.Chrome(service = s)

driver.get(f"https://query1.finance.yahoo.com/v7/finance/download/{stock.upper()}?period1=1490400000&period2=1648166400&interval=1mo&events=history&includeAdjustedClose=true")

time.sleep(1)

driver.quit()

with open(f'/Users/kushgoswami/Downloads/{stock.upper()}.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    monthly_close_prices = []

    for line in csv_reader:
        if line[4] != 'Close':
            monthly_close_prices.append(float(line[4]))

os.remove(f"/Users/kushgoswami/Downloads/{stock.upper()}.csv")

diff_list = [0]
for i in range(len(monthly_close_prices) - 1):
    diff = (monthly_close_prices[i+1]/monthly_close_prices[i] - 1) * 100
    diff_list.append(diff)

expected_monthly_return = sum(diff_list[1:])/(len(diff_list) - 1)
monthly_standard_deviation = statistics.pstdev(diff_list[1:])

expected_yearly_return = expected_monthly_return * 12
yearly_standard_deviation = monthly_standard_deviation * (12 ** .5)

print(f"Expected Yearly Return: {expected_yearly_return} %")
print(f"Unsystematic Risk: {yearly_standard_deviation} %")




    

