from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_advice(salary, expenses, savings, score):

    prompt = f"""
    User Financial Details:
    Salary: {salary}
    Expenses: {expenses}
    Savings: {savings}
    Health Score: {score}

    Give simple financial advice in 3-4 lines.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        # Fallback (VERY IMPORTANT FOR HACKATHON)
        return f"""
AI service temporarily unavailable.

Smart Suggestion:
- Try to maintain at least 30% savings
- Reduce unnecessary expenses
- Invest regularly in SIP or mutual funds
- Build an emergency fund for 6 months
"""
