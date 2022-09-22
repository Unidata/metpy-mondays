# Metpy Monday
# 221 - Adding Interactivity with Dash Callbacks
# https://www.youtube.com/watch?v=W059p7ogK_g

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from siphon.simplewebservice.ndbc import NDBC

app = Dash(__name__)

df = NDBC.latest_observations()

print(df.columns)


@app.callback(
	Output('buoy-correlations', 'figure'),
	Input('xvar-dropdown', 'value'),
	Input('yvar-dropdown', 'value'),
	Input('cvar-dropdown', 'value')
)
def update_figure(xvar, yvar, cvar):
	fig = px.scatter(df, x = xvar, y = yvar, color = cvar, hover_name = 'station')
	fig.update_layout(transition_duration = 1000)
	return fig

app.layout = html.Div([
	html.Div([
		html.H1('NDBC Network Data', style = {'textAlign': 'center'})
		]),
	html.Div([
		html.Div([], style = {'width': '10%'}),
		html.Div([
			html.Label('X Variable'),
			html.Br(),
			dcc.Dropdown(df.columns, 'water_temperature', id = 'xvar-dropdown')
			], style = {'width': '20%'}),
		html.Div([], style = {'width': '10%'}),
		html.Div([
			html.Label('Y Variable'),
			html.Br(),
			dcc.Dropdown(df.columns, 'air_temperature', id = 'yvar-dropdown')
			], style = {'width': '20%'}),
		html.Div([], style = {'width': '10%'}),
		html.Div([
			html.Label('Color Variable'),
			html.Br(),
			dcc.Dropdown(df.columns, 'pressure', id = 'cvar-dropdown')
			], style = {'width': '20%'})
		], style = {'display': 'flex', 'flex-direction': 'row'}),
	html.Div([
		dcc.Graph(id = 'buoy-correlations')
		])
	])


if __name__ == '__main__':
	app.run_server(debug = True)

