
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import glob

# Cargar CSVs
csv_files = sorted(glob.glob("ddatos_agrupados_sem*.csv"))
df = pd.concat([pd.read_csv(f, parse_dates=["semana_epi"]) for f in csv_files], ignore_index=True)

# Crear app
app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H2("Serie temporal por variable y estación"),

    dcc.Dropdown(
        id='variable-dropdown',
        options=[{'label': var, 'value': var} for var in sorted(df['variable'].dropna().unique())],
        value=sorted(df['variable'].dropna().unique())[0],
        style={'width': '60%', 'margin-bottom': '15px'}
    ),

    dcc.Dropdown(
        id='estacion-dropdown',
        options=[{'label': est, 'value': est} for est in sorted(df['estacion'].dropna().unique())],
        value=[],
        multi=True,
        placeholder='Selecciona una o más estaciones...',
        style={'width': '60%', 'margin-bottom': '25px'}
    ),

    dcc.Graph(id='serie-temporal')
])

# Callback
@app.callback(
    Output('serie-temporal', 'figure'),
    [Input('variable-dropdown', 'value'),
     Input('estacion-dropdown', 'value')]
)
def actualizar_grafico(variable, estaciones):
    df_filtrado = df[df['variable'] == variable]

    if estaciones:
        df_filtrado = df_filtrado[df_filtrado['estacion'].isin(estaciones)]

    fig = px.line(
        df_filtrado,
        x='semana_epi',
        y='valor_mean',
        color='estacion',
        title=f"Serie temporal - {variable}",
        labels={'semana_epi': 'Semana Epidemiológica', 'valor_mean': 'Valor Promedio', 'estacion': 'Estación'}
    )
    fig.update_layout(height=600)
    return fig

# Ejecutar
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8050)
