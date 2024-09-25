import plotly.express as px
import pandas as pd

# Data
categories = [
    'Significant other', 'Family', 'Friendship',
    'Physical health/sports', 'Mental health/mindfulness', 'Spirituality/faith',
    'Community/citizenship', 'Societal engagement',
    'Job/career', 'Educational/learning', 'Finances',
    'Hobbies/interests', 'Online entertainment', 'Offline entertainment',
    'Physiological needs', 'Activities of daily living'
]

hours = [
    48, 1, 12,
    2, 0.67, 0,
    0, 1,
    32, 21, 1,
    20, 21, 0,
    5.2, 5.2
]

importance = [
    9, 10, 8,
    8, 8, 3,
    3, 3,
    9, 10, 6,
    4, 1, 5,
    9, 6
]

satisfaction = [
    8, 8, 10,
    5, 8, 6,
    2, 4,
    7, 6, 5,
    9, 4, 5,
    7, 2
]

# Convert importance and satisfaction to a range of -5 to 5
importance = [i - 5 for i in importance]
satisfaction = [s - 5 for s in satisfaction]

# Create a DataFrame
df = pd.DataFrame({
    'Category': categories,
    'Hours': hours,
    'Importance': importance,
    'Satisfaction': satisfaction
})

# Plot using Plotly
fig = px.scatter(df, x='Satisfaction', y='Importance', size='Hours', color='Category',
                 labels={'Satisfaction': 'Satisfaction', 'Importance': 'Importance'},
                 title='Importance vs Satisfaction with Hours Spent as Size of Points',
                 size_max=60, template='plotly_dark')

# Set axis range
fig.update_layout(
    xaxis=dict(range=[-5, 5], dtick=1, zeroline=True, zerolinewidth=2, zerolinecolor='black'),
    yaxis=dict(range=[-5, 5], dtick=1, zeroline=True, zerolinewidth=2, zerolinecolor='black')
)

# Show plot
fig.show()

