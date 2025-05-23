
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import glob

# 🔁 Cargar y consolidar todos los CSV
csv_files = sorted(glob.glob("ddatos_agrupados_sem*.csv"))
df = pd.concat([pd.read_csv(f, parse_dates=["semana_epi"]) for f in csv_files], ignore_index=True)


# Crear app
app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H2("DAGMA - Serie temporal por variable"),
    dcc.Dropdown(
        id='variable-dropdown',
        options=[{'label': var, 'value': var} for var in sorted(df['variable'].dropna().unique())],
        value=sorted(df['variable'].dropna().unique())[0],
        style={'width': '70%', 'margin-bottom': '20px'}
    ),
    dcc.Graph(id='serie-temporal')
])

# Callback
@app.callback(
    Output('serie-temporal', 'figure'),
    Input('variable-dropdown', 'value')
)
def actualizar_grafico(variable):
    df_filtrado = df[df['variable'] == variable]
    fig = px.line(
        df_filtrado,
        x='semana_epi',
        y='valor_mean',
        color='estacion',
        title=f"Serie temporal - {variable}",
        labels={'semana_epi': 'Fecha Semana', 'valor_mean': 'Valor Promedio', 'estacion': 'Estación'}
    )
    fig.update_layout(height=600)
    return fig

# Ejecutar
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8050)
