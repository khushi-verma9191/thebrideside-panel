# 🤖 AI Logic for Call Suggestion

We implemented an AI-powered feature in our call scheduler to suggest the **best time to call a lead**, based on their city.

## Logic Used

```python
def suggest_call_time(city):
    india_cities = ['Delhi', 'Mumbai', 'Bangalore']
    if city in india_cities:
        return "10AM–1PM or 5PM–7PM IST"
    else:
        return "7PM–10PM IST"
