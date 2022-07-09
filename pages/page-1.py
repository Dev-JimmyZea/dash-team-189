import dash
# from dash.dependencies import Input, Output, State
import dash_daq as daq
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback
import datetime as dt
from dash_labs.plugins import register_page
import datetime as dt
import folium

from app_main import df

df_temp = df.copy()

df_temp['hora_lectura_dato_left'] = pd.to_datetime(
    df_temp['hora_lectura_dato_left'])
df_temp['fecha_lectura_left'] = pd.to_datetime(
    df_temp['fecha_lectura_left']).dt.date

register_page(__name__, path="page1")


layout = dbc.Container(
    [
        html.H1('1. Dashboard 80-20', className="tabs-title"),
        dcc.Tabs(id="tabs-container", value='tab-1', children=[
            dcc.Tab(label='Visión General', value='tab-1', className="custom-tab",
                    selected_className="custom-tab--selected"),
            dcc.Tab(label='Visión Detallada', value='tab-2', className="custom-tab",
                    selected_className="custom-tab--selected"),
            dcc.Tab(label='Modelo', value='tab-3', className="custom-tab",
                    selected_className="custom-tab--selected"),
        ],
            className="tabs-titles",
        ),
        html.Div(id='tabs-content')
    ],
    fluid=True,
    className="container-page1",
)


def contentTab1():
    return dbc.Container(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(

                                [
                                    html.H5('Seleccione la fecha de inicio y fin de la visualización'),

                                    dcc.DatePickerRange(
                                        id='my-date-picker-range',
                                        className='my-picker-range',
                                        min_date_allowed=df_temp['fecha_lectura_left'].min(
                                        ),
                                        max_date_allowed=df_temp['fecha_lectura_left'].max(
                                        ),
                                        initial_visible_month=df_temp['fecha_lectura_left'].min(
                                        ),
                                        start_date=df_temp['fecha_lectura_left'].min(
                                        ),
                                        end_date=df_temp['fecha_lectura_left'].max(
                                        ),
                                        persistence=True,
                                        persisted_props=['start_date'],
                                        persistence_type='session',
                                        minimum_nights=0,
                                        updatemode='singledate'
                                    ),
                                ],
                                className="tab-content-picker",
                            ),

                            html.Div(

                                [
                                    dcc.Loading(
                                        id="loading-1",
                                        children=[
                                            dcc.Graph(
                                                id='graph-with-slider',
                                                className="graph-1",
                                            ),
                                        ],
                                        type="circle",
                                        color="#A9BA18",
                                        style={"marginTop": "20px"},
                                    )
                                ],
                                className="tab-graph",

                            ),
                        ],
                        className="tab-content-graph-date",
                    ),
                    html.Div(
                        [
                            dcc.Loading(
                                id="loading-3",
                                children=[
                                    dcc.Graph(
                                        id='mymap',
                                        className="map-density",
                                    ),
                                ],
                                type="circle",
                                color="#A9BA18",
                                style={"marginTop": "20px"},
                            )
                        ],
                        className="tab-content-map",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5('Seleccione la hora de inicio y fin de la visualización'),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    id='my-dropdown-start',
                                                    options=[{'label': '0' + str(i) + ':00:00' if i < 10 else str(i) + ':00:00',
                                                              'value': '0' + str(i) + ':00:00' if i < 10 else str(i) + ':00:00',
                                                              } for i in sorted(df_temp['hora_lectura_dato_left'].dt.hour.unique())],
                                                    value='0' + str(df_temp['hora_lectura_dato_left'].dt.hour.min()) + ':00:00' if df_temp['hora_lectura_dato_left'].dt.hour.min(
                                                    ) < 10 else str(df_temp['hora_lectura_dato_left'].dt.hour.min()) + ':00:00',
                                                    persistence=True,
                                                    persistence_type='session',
                                                ),
                                            ),
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    id='my-dropdown-end',
                                                    options=[{'label': '0' + str(i) + ':59:59' if i < 10 else str(i) + ':59:59',
                                                              'value': '0' + str(i) + ':59:59' if i < 10 else str(i) + ':59:59',
                                                              } for i in sorted(df_temp['hora_lectura_dato_left'].dt.hour.unique())],                                                # style={"width": "50%"},
                                                    value='0' + str(df_temp['hora_lectura_dato_left'].dt.hour.max()) + ':59:59' if df_temp['hora_lectura_dato_left'].dt.hour.max(
                                                    ) < 10 else str(df_temp['hora_lectura_dato_left'].dt.hour.max()) + ':59:59',

                                                    persistence=True,
                                                    persistence_type='session',
                                                ),
                                            ),
                                        ],

                                        className="tab-content-picker-time grid-2",


                                    )
                                ],
                                className="tab-content-picker",

                            ),

                            html.Div(

                                [
                                    dcc.Loading(
                                        id="loading-2",
                                        children=[
                                            dcc.Graph(
                                                id='graph-with-slider2',
                                                className="graph-2",
                                            ),
                                        ],
                                        type="circle",
                                        color="#A9BA18",
                                        style={"marginTop": "20px"},
                                    )
                                ],
                                className="tab-graph",

                            ),

                        ],
                        className="tab-content-graph-time",
                    ),
                ],
                className="d-flex flex-row tab1-content",
            )
        ],
        fluid=True,
        className="tabs-content",
    )


def contentTab2():
    return dbc.Container(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(

                                [
                                    html.H5('Seleccione la fecha de inicio y fin de la visualización'),

                                    dcc.DatePickerRange(
                                        id='my-date-picker-range2',
                                        className='my-picker-range',

                                        initial_visible_month=df_temp['fecha_lectura_left'].min(
                                        ),
                                        start_date=df_temp['fecha_lectura_left'].min(
                                        ),
                                        end_date=df_temp['fecha_lectura_left'].max(
                                        ),
                                        persistence=True,
                                        persisted_props=['start_date'],
                                        persistence_type='session',
                                        minimum_nights=0,
                                        updatemode='singledate'
                                    ),
                                ],
                                className="tab-content-picker",
                            ),
                            html.Div(
                                [
                                    html.H5('Seleccione la hora de inicio y fin de la visualización'),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    id='my-dropdown-start2',
                                                    options=[{'label': '0' + str(i) + ':00:00' if i < 10 else str(i) + ':00:00',
                                                              'value': '0' + str(i) + ':00:00' if i < 10 else str(i) + ':00:00',
                                                              } for i in sorted(df_temp['hora_lectura_dato_left'].dt.hour.unique())],
                                                    value='0' + str(df_temp['hora_lectura_dato_left'].dt.hour.min()) + ':00:00' if df_temp['hora_lectura_dato_left'].dt.hour.min(
                                                    ) < 10 else str(df_temp['hora_lectura_dato_left'].dt.hour.min()) + ':00:00',
                                                    persistence=True,
                                                    persistence_type='session',
                                                ),
                                            ),
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    id='my-dropdown-end2',
                                                    options=[{'label': '0' + str(i) + ':59:59' if i < 10 else str(i) + ':59:59',
                                                              'value': '0' + str(i) + ':59:59' if i < 10 else str(i) + ':59:59',
                                                              } for i in sorted(df_temp['hora_lectura_dato_left'].dt.hour.unique())],                                                # style={"width": "50%"},
                                                    value='0' + str(df_temp['hora_lectura_dato_left'].dt.hour.max()) + ':59:59' if df_temp['hora_lectura_dato_left'].dt.hour.max(
                                                    ) < 10 else str(df_temp['hora_lectura_dato_left'].dt.hour.max()) + ':59:59',

                                                    persistence=True,
                                                    persistence_type='session',
                                                ),
                                            ),
                                        ],

                                        className="tab-content-picker-time grid-2",


                                    )
                                ],
                                className="tab-content-picker",

                            ),


                            html.Div(
                                [
                                    html.H5('Seleccione la(s) localidad(es)'),
                                    
                                    dcc.Checklist(
                                        options=[
                                            {
                                                'label': i.capitalize(),
                                                'value': i
                                            } for i in df_temp['localidad'].unique()
                                        ],
                                        # marcar todos los tipos de alerta
                                        value=[df_temp['localidad'].unique()[0]],
                                        id='my-locality',
                                        persistence=True,
                                        persistence_type='session',
                                        className="checklist-alerts",
                                    ),
                                ],
                                className="tab-content-location",
                            ),

                            html.Div(
                                [
                                    html.H5('Escoja el/los tipo(s) de alerta'),

                                    dcc.Checklist(
                                        options=[
                                            {
                                                'label': i.capitalize(),
                                                'value': i
                                            } for i in df_temp['type_right'].unique()[pd.notnull(df_temp['type_right'].unique())]
                                        ],
                                        # marcar el primer tipo de alerta
                                        value=[df_temp['type_right'].unique()[pd.notnull(df_temp['type_right'].unique())][0]],
                                        id='my-checklist-tab2',
                                        persistence=True,
                                        persistence_type='session',
                                        className="checklist-alerts",
                                    ),
                                ],
                                className="content-checklist",
                            ),
                        ],
                        className="tab-content-graph-date",

                    ),

                    html.Div(
                        [
                            
                            dcc.Loading(
                                id="loading-4-bib",
                                children=[
                                    html.Div(
                                        id="latest"
                                    )
                                ],
                                type="circle",
                                color="#A9BA18",
                                style={"marginTop": "20px"},
                            ),
                            
                            # html.Div(
                            #     [
                            #         dcc.Loading(
                            #             id="loading-4",
                            #             children=[
                            #                 html.Iframe(
                            #                     id='mymap2',
                            #                     # className="map-density",
                            #                     style={"width": "100%", "height": "100%"},
                            #                     srcDoc=open(
                            #                         'map_alerts.html', 'r').read(),
                            #                 ),

                            #             ],
                            #             type="circle",
                            #             color="#A9BA18",
                            #             style={"marginTop": "20px"},
                            #         ),
                            #     ],
                            #     className="tab-content-map-other-other",
                            # ),
                            html.H5('Ordenar por:', className="tab2-order-by"),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dcc.Dropdown(
                                            options=[
                                                {
                                                    'label': 'index',
                                                    'value': 'index'
                                                },
                                                {
                                                    'label': 'tid',
                                                    'value': 'tid',
                                                },
                                                {
                                                    'label': 'name_from',
                                                    'value': 'name_from',
                                                },
                                                {
                                                    'label': 'name_to',
                                                    'value': 'name_to',
                                                },
                                                {
                                                    'label': 'localidad',
                                                    'value': 'localidad',
                                                },
                                                {
                                                    'label': 'length',
                                                    'value': 'length',
                                                },
                                                {
                                                    'label': 'type_right',
                                                    'value': 'type_right',
                                                },
                                                {
                                                    'label': 'velocidad_prom(km/h)',
                                                    'value': 'velocidad_prom(km/h)',
                                                },
                                                {
                                                    'label': 'dVel',
                                                    'value': 'dVel',
                                                },                                        
                                            ],
                                            value='index',
                                            id='my-dropdown-sort',
                                            persistence=True,
                                            persistence_type='session',

                                        ),
                            
                                    ),
                                    dbc.Col(
                                        dcc.Dropdown(
                                            options=[
                                                {
                                                    'label': 'Ascendente',
                                                    'value': 'True',
                                                },
                                                {
                                                    'label': 'Descendente',
                                                    'value': 'False',
                                                },
                                            ],
                                            value='True',
                                            id='my-dropdown-order',
                                            persistence=True,
                                            persistence_type='session',

                                        ),
                                    ),
                                ],

                                className="tab-content-picker-time other grid-2",

                            ),
                            

                            dcc.Loading(
                                        id="loading-5",
                                        children=[
                                            html.Div(
                                            id="table-content-tab2",
                                            className="tab2-content-table",
                                            )
                                        ],
                                        type="circle",
                                        color="#A9BA18",
                                        style={"marginTop": "20px"},
                                    ),
                        ],
                        className="tab2-content-map",
                    ),


                ],
                className="d-flex flex-row tab1-content",

            )
        ],
        fluid=True,
        className="tabs-content",
    )


def contentTab3():
    return dbc.Container(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(

                                [
                                    html.H5('Seleccione la fecha de inicio y fin de la visualización'),

                                    dcc.DatePickerRange(
                                        id='my-date-picker-range3',
                                        className='my-picker-range',

                                        initial_visible_month=df_temp['fecha_lectura_left'].min(
                                        ),
                                        start_date=df_temp['fecha_lectura_left'].min(
                                        ),
                                        end_date=df_temp['fecha_lectura_left'].max(
                                        ),
                                        persistence=True,
                                        persisted_props=['start_date'],
                                        persistence_type='session',
                                        minimum_nights=0,
                                        updatemode='singledate'
                                    ),
                                ],
                                className="tab-content-picker",
                            ),
                            html.Div(
                                [
                                    html.H5('Seleccione la hora de inicio y fin de la visualización'),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    id='my-dropdown-start3',
                                                    options=[{'label': '0' + str(i) + ':00:00' if i < 10 else str(i) + ':00:00',
                                                              'value': '0' + str(i) + ':00:00' if i < 10 else str(i) + ':00:00',
                                                              } for i in sorted(df_temp['hora_lectura_dato_left'].dt.hour.unique())],
                                                    value='0' + str(df_temp['hora_lectura_dato_left'].dt.hour.min()) + ':00:00' if df_temp['hora_lectura_dato_left'].dt.hour.min(
                                                    ) < 10 else str(df_temp['hora_lectura_dato_left'].dt.hour.min()) + ':00:00',
                                                    persistence=True,
                                                    persistence_type='session',
                                                ),
                                            ),
                                            dbc.Col(
                                                dcc.Dropdown(
                                                    id='my-dropdown-end3',
                                                    options=[{'label': '0' + str(i) + ':59:59' if i < 10 else str(i) + ':59:59',
                                                              'value': '0' + str(i) + ':59:59' if i < 10 else str(i) + ':59:59',
                                                              } for i in sorted(df_temp['hora_lectura_dato_left'].dt.hour.unique())],                                                # style={"width": "50%"},
                                                    value='0' + str(df_temp['hora_lectura_dato_left'].dt.hour.max()) + ':59:59' if df_temp['hora_lectura_dato_left'].dt.hour.max(
                                                    ) < 10 else str(df_temp['hora_lectura_dato_left'].dt.hour.max()) + ':59:59',

                                                    persistence=True,
                                                    persistence_type='session',
                                                ),
                                            ),
                                        ],

                                        className="tab-content-picker-time grid-2",


                                    )
                                ],
                                className="tab-content-picker",

                            ),

                            html.Div(
                                [
                                    html.H5('Seleccionar la variable'),
                                    
                                    dcc.Dropdown(
                                        id='my-dropdown-variable3',
                                        options=[
                                                {
                                                    'label': 'jamLevel',
                                                    'value': 'jamLevel',
                                                },
                                                {
                                                    'label': 'fecha_lectura_left',
                                                    'value': 'fecha_lectura_left',
                                                }
                                            ],
                                        value='fecha_lectura_left',
                                        persistence=True,
                                        persistence_type='session',
                                    ),

                                ],
                                className="tab-content-picker",

                            ),

                            html.Div(
                                [
                                    html.H5('Seleccione la(s) localidad(es)'),
                                    
                                    dcc.Checklist(
                                        options=[
                                            {
                                                'label': i.capitalize(),
                                                'value': i
                                            } for i in df_temp['localidad'].unique()
                                        ],
                                        # marcar todos los tipos de alerta
                                        value=[df_temp['localidad'].unique()[0]],
                                        id='my-locality3',
                                        persistence=True,
                                        persistence_type='session',
                                        className="checklist-alerts",
                                    ),
                                ],
                                className="tab-content-location",
                            ),

                        ],
                        className="tab-content-graph-date",

                    ),

                    html.Div(
                        
                        [
                            dcc.Loading(
                                id="loading-7",
                                children=[
                                    dcc.Graph(
                                        id='mymap3',
                                        className="map-density",
                                    ),
                                ],
                                type="circle",
                                color="#A9BA18",
                                style={"marginTop": "20px"},
                            )
                        ],
                        className="tab-content-map-other",
                    ),


                ],
                className="d-flex flex-row tab1-content",

            )
        ],
        fluid=True,
        className="tabs-content",
    )



@callback(Output('tabs-content', 'children'),
          Input('tabs-container', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div(
            children=[
                contentTab1(),
            ]
        )
    elif tab == 'tab-2':
        return html.Div(
            children=[
                contentTab2()
            ]
        )
    elif tab == 'tab-3':
        return html.Div(
            children=[
                contentTab3()
            ]
        )
        

@callback(
    Output("mymap3", "figure"),
    [Input("my-date-picker-range3", "start_date"),
     Input("my-date-picker-range3", "end_date"),
     Input("my-dropdown-start3", "value"),
     Input("my-dropdown-end3", "value"),
     Input("my-locality3", "value"),
     Input("my-dropdown-variable3", "value")
    ]
)
def update_plot3(start_date, end_date, start_time, end_time, locality, variable):
    global df
    df_temp = df.copy()
    if len(locality) == 0:
        locality = df_temp['localidad'].unique()
        
    df_temp['hora_lectura_dato_left'] = pd.to_datetime(
    df_temp['hora_lectura_dato_left'])
    df_temp['fecha_lectura_left'] = pd.to_datetime(
    df_temp['fecha_lectura_left']).dt.date
    time_start = dt.datetime.strptime(start_time, '%H:%M:%S')
    time_end = dt.datetime.strptime(end_time, '%H:%M:%S')
    date_start = dt.datetime.strptime(start_date, '%Y-%m-%d')
    date_end = dt.datetime.strptime(end_date, '%Y-%m-%d')
    df_temp = df_temp.loc[(df_temp['hora_lectura_dato_left'].dt.time >= time_start.time()) & (df_temp['hora_lectura_dato_left'].dt.time <= time_end.time()) & (
        df_temp['fecha_lectura_left'] >= date_start.date()) & (df_temp['fecha_lectura_left'] <= date_end.date())]
    df_temp = df_temp[(df_temp['localidad'].isin(locality))]
    fig = px.violin(df_temp, x=variable, y='dVel', color='localidad')
    
    return fig

@callback(
    Output("latest", "children"),
    [Input("my-date-picker-range2", "start_date"),
     Input("my-date-picker-range2", "end_date"),
     Input("my-dropdown-start2", "value"),
     Input("my-dropdown-end2", "value"),
     Input("my-locality", "value"),
     Input("my-checklist-tab2", "value"),

     ],
)
def update_graph_alerts(start_date, end_date, start_time, end_time, locality, alerts):
    global df
    df_temp = df.copy()
    if len(alerts) == 0:
        alerts = df_temp['type_right'].unique()[pd.notnull(df_temp['type_right'].unique())]
    
    if len(locality) == 0:
        locality = df_temp['localidad'].unique()
    
    df_temp['hora_lectura_dato_left'] = pd.to_datetime(
        df_temp['hora_lectura_dato_left'])
    df_temp['fecha_lectura_left'] = pd.to_datetime(
        df_temp['fecha_lectura_left']).dt.date
    time_start = dt.datetime.strptime(start_time, '%H:%M:%S')
    time_end = dt.datetime.strptime(end_time, '%H:%M:%S')
    date_start = dt.datetime.strptime(start_date, '%Y-%m-%d')
    date_end = dt.datetime.strptime(end_date, '%Y-%m-%d')
    df_temp = df_temp.loc[(df_temp['hora_lectura_dato_left'].dt.time >= time_start.time()) & (df_temp['hora_lectura_dato_left'].dt.time <= time_end.time()) & (
        df_temp['fecha_lectura_left'] >= date_start.date()) & (df_temp['fecha_lectura_left'] <= date_end.date())]
    df_temp = df_temp[(df_temp['localidad'].isin(locality)) & (df_temp['type_right'].isin(alerts))]
    
    df_temp.reset_index(drop=True, inplace=True)
    
    lineas = df_temp['linea']

    reducido = lineas.str[12:-1]
    reducido = reducido.str.split(',')

    def separador(lista):
        return [(float(y), float(x)) for x,y in [x.split() for x in lista]]

    reducido = reducido.apply(separador)

    df_temp['coordenadas'] = reducido

    map_final = folium.Map(location = [4.714335, -74.063644], zoom_start=11)
    val_25 = df_temp['dVel'].describe()['25%']
    val_75 = df_temp['dVel'].describe()['75%']
    
    df_temp['color'] = df_temp['dVel'].apply(lambda x: 'green' if x > val_75 else 'red' if x < val_25 else 'blue')

    for i in range(len(df_temp['coordenadas'])):
        # hacer el polyline
        folium.PolyLine(df_temp['coordenadas'][i], color=df_temp['color'][i], weight=2.5, opacity=1).add_to(map_final)


    # Alertas
    tooltip = "Click me!" 
    alert_information_final = df_temp[['latitud_right','longitud_right','type_right']].dropna().drop_duplicates()
    tuples = [tuple(x) for x in alert_information_final.to_numpy()]

    for item in tuples:

        color = 'red' if item[2] == 'JAM' else 'blue' if item[2] == 'ACCIDENT' else 'green' if item[2] == 'WEATHERHAZARD' else 'orange'

        folium.Marker(
            [item[0], item[1]], popup="<i>"+ item[2] +"</i>", tooltip=tooltip, icon=folium.Icon(icon="info-sign", color=color)
        ).add_to(map_final)
        

    # folium.GeoJson(map_data, name="geojson").add_to(map)

    map_final.save("map_alerts.html")
    
    return html.Iframe(
            id='mymap2',
            style={"width": "100%", "height": "100%"},
            srcDoc=open(
                'map_alerts.html', 'r').read(),
        ),

    
@callback(
    Output("table-content-tab2", "children"),
    [Input("my-date-picker-range2", "start_date"),
     Input("my-date-picker-range2", "end_date"),
     Input("my-dropdown-start2", "value"),
     Input("my-dropdown-end2", "value"),
     Input("my-locality", "value"),
     Input("my-checklist-tab2", "value"),
     Input("my-dropdown-sort", "value"),
    Input("my-dropdown-order", "value")
     ],
)
def update_table(start_date, end_date, start_time, end_time, locality, alerts, sort_by, ascendent):
    global df
    df_temp = df.copy()
    if len(alerts) == 0:
        alerts = df_temp['type_right'].unique()[pd.notnull(df_temp['type_right'].unique())]
    
    if len(locality) == 0:
        locality = df_temp['localidad'].unique()
    
    df_temp['hora_lectura_dato_left'] = pd.to_datetime(
        df_temp['hora_lectura_dato_left'])
    df_temp['fecha_lectura_left'] = pd.to_datetime(
        df_temp['fecha_lectura_left']).dt.date
    time_start = dt.datetime.strptime(start_time, '%H:%M:%S')
    time_end = dt.datetime.strptime(end_time, '%H:%M:%S')
    date_start = dt.datetime.strptime(start_date, '%Y-%m-%d')
    date_end = dt.datetime.strptime(end_date, '%Y-%m-%d')
    df_temp = df_temp.loc[(df_temp['hora_lectura_dato_left'].dt.time >= time_start.time()) & (df_temp['hora_lectura_dato_left'].dt.time <= time_end.time()) & (
        df_temp['fecha_lectura_left'] >= date_start.date()) & (df_temp['fecha_lectura_left'] <= date_end.date())]
    df_temp = df_temp[(df_temp['localidad'].isin(locality)) & (df_temp['type_right'].isin(alerts))]
    df_temp.reset_index(inplace=True)
    df_temp.index += 1
    df_temp = df_temp[['tid', 'name_from', 'name_to', 'localidad', 'length', 'type_right', 'velocidad_prom(km/h)', 'dVel']]
    # redondear a 2 cifras los valores de las columnas velocidad_prom(km/h) y dVel
    df_temp['velocidad_prom(km/h)'] = df_temp['velocidad_prom(km/h)'].round(2)
    df_temp['dVel'] = df_temp['dVel'].round(2)
    df_temp.reset_index(inplace=True)

    df_temp.sort_values(by=sort_by, inplace=True, ascending=True if ascendent == 'True' else False)


    return dbc.Table.from_dataframe(df_temp, bordered=True, hover=True),

@callback(
    Output("graph-with-slider2", "figure"),
    [Input("my-date-picker-range", "start_date"),
     Input("my-date-picker-range", "end_date"),
     Input("my-dropdown-start", "value"),
     Input("my-dropdown-end", "value")
     ],
)
def update_graph_bar_time(date_start, date_end, time_start, time_end):

    global df
    df_temp = df.copy()
    df_temp['hora_lectura_dato_left'] = pd.to_datetime(
        df_temp['hora_lectura_dato_left'])
    df_temp['fecha_lectura_left'] = pd.to_datetime(
        df_temp['fecha_lectura_left']).dt.date
    time_start = dt.datetime.strptime(time_start, '%H:%M:%S')
    time_end = dt.datetime.strptime(time_end, '%H:%M:%S')
    date_start = dt.datetime.strptime(date_start, '%Y-%m-%d')
    date_end = dt.datetime.strptime(date_end, '%Y-%m-%d')
    df_temp = df_temp.loc[(df_temp['hora_lectura_dato_left'].dt.time >= time_start.time()) & (df_temp['hora_lectura_dato_left'].dt.time <= time_end.time()) & (
        df_temp['fecha_lectura_left'] >= date_start.date()) & (df_temp['fecha_lectura_left'] <= date_end.date())]
    labels_axis_x = df_temp['hora_lectura_dato_left'].dt.hour.unique()
    labels_axis_y = df_temp.groupby('hora_lectura_dato_left')[
        'velocidad_prom(km/h)'].mean()
    fig = {
        "data": [
            {
                "x": labels_axis_x,
                "y": labels_axis_y,
                "hoverinfo": "y",
                "text": round(labels_axis_y, 2),
                "type": "bar",
                "marker": {
                    "color": "#4C531E",
                    "line": {
                        "color": "#4C531E",
                        "width": 1
                    }
                }

            }
        ],
        'layout': {
            'title': 'Velocidad prom. por Hora',
            'xaxis': {'title': 'Hora', 'tickvals': labels_axis_x, 'ticktext': labels_axis_x, 'automargin': True},
            'yaxis': {'title': 'Velocidad prom. (km/h)', 'automargin': True},
            'height': 300,
            'width': 224,
            'margin': {'l': 40, 'b': 40, 't': 40, 'r': 10},
            'legend': {'x': 0, 'y': 1},
            'hovermode': 'closest',
            'barmode': 'group',
            'bargap': 0.1,
            'bargroupgap': 0.05,
            'autosize': True,
            'font': {'color': '#000'},
            'paper_bgcolor': '#E7ECB1',
            "plot_bgcolor": "#E7ECB1",
        }
    }

    return fig


@callback(
    Output("graph-with-slider", "figure"),
    [Input("my-date-picker-range", "start_date"),
     Input("my-date-picker-range", "end_date")],
)
def update_graph_bar(start_date, end_date):

    global df

    df_temp = df.copy()

    df_temp['date_temp'] = pd.to_datetime(
        df_temp['fecha_lectura_left']).dt.date
    df_temp = df_temp.loc[df_temp["date_temp"].between(
        *pd.to_datetime([start_date, end_date]))]
    labels_axis_x = df_temp['date_temp'].unique()
    fig = {
        "data": [
            {
                "x": df_temp["date_temp"].drop_duplicates(),
                "y": df_temp['velocidad_prom(km/h)'].groupby(df_temp['date_temp']).mean(),
                "hoverinfo": "y",
                "text": round(df_temp['velocidad_prom(km/h)'].groupby(df_temp['date_temp']).mean(), 2),
                "type": "bar",
                "marker": {
                    "color": "#4C531E",
                    "line": {
                        "color": "#4C531E",
                        "width": 1
                    }
                },
            }
        ],
        'layout': {
            'title': 'Velocidad prom. por fecha',
            'xaxis': {'title': 'Fecha lectura', 'tickvals': labels_axis_x, 'ticktext': labels_axis_x, 'automargin': True},
            'yaxis': {'title': 'Velocidad prom. (km/h)', 'automargin': True},
            'height': 300,
            'width': 224,
            'margin': {'l': 40, 'b': 40, 't': 40, 'r': 10},
            'legend': {'x': 0, 'y': 1},
            'hovermode': 'closest',
            'barmode': 'group',
            'bargap': 0.1,
            'bargroupgap': 0.05,
            'autosize': True,
            'font': {'color': '#000'},
            'paper_bgcolor': '#E7ECB1',
            "plot_bgcolor": "#E7ECB1",
        }
    }

    return fig


@callback(
    Output('mymap', 'figure'),
    [Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date'),
     Input('my-dropdown-start', 'value'),
     Input('my-dropdown-end', 'value')
     ]
)
def update_output(date_start, date_end, time_start, time_end):
    # global df
    # df_temp = df.copy()

    # df_temp['fecha_lectura_left'] = pd.to_datetime(df['fecha_lectura_left'])
    # df_temp.set_index('fecha_lectura_left', inplace=True)
    # df_temp = df_temp.sort_index().loc[start_date:end_date]

    global df
    df_temp = df.copy()
    df_temp['hora_lectura_dato_left'] = pd.to_datetime(
        df_temp['hora_lectura_dato_left'])
    df_temp['fecha_lectura_left'] = pd.to_datetime(
        df_temp['fecha_lectura_left']).dt.date
    time_start = dt.datetime.strptime(time_start, '%H:%M:%S')
    time_end = dt.datetime.strptime(time_end, '%H:%M:%S')
    date_start = dt.datetime.strptime(date_start, '%Y-%m-%d')
    date_end = dt.datetime.strptime(date_end, '%Y-%m-%d')
    df_temp = df_temp.loc[(df_temp['hora_lectura_dato_left'].dt.time >= time_start.time()) & (df_temp['hora_lectura_dato_left'].dt.time <= time_end.time()) & (
        df_temp['fecha_lectura_left'] >= date_start.date()) & (df_temp['fecha_lectura_left'] <= date_end.date())]
    fig = px.density_mapbox(df_temp,
                            lat='latitud_left',
                            lon='longitud_left',
                            z='velocidad_prom(km/h)',
                            radius=13,
                            zoom=10,
                            mapbox_style="carto-positron",
                            color_continuous_scale=[
                                '#ff0000', '#e68019', '#008f39'],
                            opacity=0.7,
                            hover_name='name',
                            )

    return fig
