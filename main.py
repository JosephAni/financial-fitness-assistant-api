# Import the necessary packages
from fastapi import FastAPI
from datetime import datetime, timedelta

# Create an instance of the FastAPI application
app = FastAPI()

# A function to calculate daily savings goal
def calculate_daily_savings_goal(income, expenses, savings_goal, time_frame_months):
    monthly_income = income * 12
    total_expenses = expenses * 12
    total_savings_goal = savings_goal
    months_remaining = time_frame_months - datetime.now().month

    # Calculate daily savings goal
    daily_savings_goal = (total_savings_goal + total_expenses - monthly_income) / (months_remaining * 30)
    return daily_savings_goal

@app.get("/")
def read_root():
    return {"Hello": "Welcome to the Financial Fitness Assistant API!"}

@app.post("/calculate_daily_savings_goal")
def calculate_daily_savings_goal(income: float, expenses: float, savings_goal: float, time_frame_months: int):
    daily_savings_goal = calculate_daily_savings_goal(income, expenses, savings_goal, time_frame_months)
    return {"daily_savings_goal": daily_savings_goal}