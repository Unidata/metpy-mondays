# Metpy Monday
# 220 - Laying out Dash Apps with DIVs
# https://www.youtube.com/watch?v=zGWY-NfzD9s

from dash import Dash, dcc, html
import plotly.express as px
from siphon.simplewebservice.ndbc import NDBC

app = Dash(__name__)

df = NDBC.latest_observations()

print(df.columns)

fig = px.scatter(df, x = 'water_temperature', y = 'air_temperature', color = 'pressure', hover_name = 'station')

app.layout = html.Div([
	html.Div([
		html.H1('NDBC Network Data', style = {'textAlign': 'center'})
		]),
	html.Div([
		html.Div([], style = {'width': '10%'}),
		html.Div([
			html.Label('X Variable'),
			html.Br(),
			dcc.Dropdown(df.columns, 'water_temperature')
			], style = {'width': '20%'}),
		html.Div([], style = {'width': '10%'}),
		html.Div([
			html.Label('Y Variable'),
			html.Br(),
			dcc.Dropdown(df.columns, 'air_temperature')
			], style = {'width': '20%'}),
		html.Div([], style = {'width': '10%'}),
		html.Div([
			html.Label('Color Variable'),
			html.Br(),
			dcc.Dropdown(df.columns, 'pressure')
			], style = {'width': '20%'})
		], style = {'display': 'flex', 'flex-direction': 'row'}),
	html.Div([
		dcc.Graph(id = 'buoy-correlations', figure = fig)
		])
	])


if __name__ == '__main__':
	app.run_server(debug = True)

