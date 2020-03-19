import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go
import pandas as pd

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

day2day = pd.read_csv('day2day.csv')
df_day2day = day2day.apply(pd.to_numeric, errors="ignore")
df_bar_day2day = df_day2day.head(25)
trace_cases = go.Scatter(
    x=df_bar_day2day['Date'],
    y=df_bar_day2day['Cases'],
    name="Cases",
    mode="lines+markers",
    marker=dict(size=10, opacity=0.5),
    line=dict(color='#17BECF'),
    opacity=0.9
)
trace_deaths = go.Scatter(
    x=df_bar_day2day['Date'],
    y=df_bar_day2day['Deaths'],
    name="Deaths",
    mode="lines+markers",
    marker=dict(size=10, opacity=0.5),
    line=dict(color='#FF0000'),
    opacity=0.9
)
trace_recoveries = go.Scatter(
    x=df_bar_day2day['Date'],
    y=df_bar_day2day['Recoveries'],
    name="Recoveries",
    mode="lines+markers",
    marker=dict(size=10, opacity=0.5),
    line=dict(color='#00FF00'),
    opacity=0.9
)

data1 = [trace_cases, trace_deaths, trace_recoveries]
layout1 = dict(title="Day to Day Analysis Of Coronavirus in India")

fig1 = dict(data=data1, layout=layout1)

cvirus = pd.read_csv('covid19-india.csv')
df_cvirus = cvirus.apply(pd.to_numeric, errors="ignore")
df_new_cvirus = df_cvirus.head(20)

trace1 = go.Bar(
    x=df_new_cvirus['state_name'],
    y=df_new_cvirus['total_cases'],
    name="Confirmed"
)
trace2 = go.Bar(
    x=df_new_cvirus['state_name'],
    y=df_new_cvirus['total_cured'],
    name="Recovered"
)
trace3 = go.Bar(
    x=df_new_cvirus['state_name'],
    y=df_new_cvirus['total_deaths'],
    name="Deaths"
)
data2 = [trace1, trace2, trace3]
colors = ["blue", "green", "red"]
layout2 = go.Layout(
    barmode="group"
)

fig2 = go.Figure(data=data2, layout=layout2)

external_stylesheets = ['https://codepen.io/criddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
        html.H1(children="CV19 App"),
        html.Img(src="/assets/cv19.jpg")
    ], className="banner"),

    html.Div([
        dcc.Graph(id="Daily Trend",
                  figure=fig1)
    ], className="okay okay1"),
    html.Div([
        dcc.Graph(id="Bar Graph",
                  figure=fig2)
    ], className="okay okay2"),
])


if __name__ == "__main__":
    app.run_server(debug=True)

