import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
from dash import Dash
import app_main
register_page(__name__, path="")
d = Dash(__name__)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(

                    html.Img(
                        src=d.get_asset_url("imgs/home.jpg"),                        
                    ),
                    className="card",
                ),
                dbc.Col(

                    dbc.Jumbotron(
                        [
                            html.H1("Tráfico 80/20"),
                            html.P(
                                "El Tráfico 80/20 está dirigido a identificar los tramos de la carretera en los que la gente pasa el 80% de su tiempo viajando el 20% del total del viaje."
                            ),

                            dbc.Button(
                                "Comencemos",
                                # color="#879225",
                                href="/page1",
                                className="mr-1 button-get-started",
                            ),
                        ],
                        className="test text-center d-flex align-items-center justify-content-center flex-column",
                        style={"backgroundColor": "#4C531E",
                               "color": "white", "height": "100%"},

                    ),
                ),
            ],

        ),

    ],
    fluid=True,
    className="container-home",
)
