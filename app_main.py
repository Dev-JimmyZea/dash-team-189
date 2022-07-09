
import dash
import dash_bootstrap_components as dbc
# from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
# from dash import dash_table
# from dash.exceptions import PreventUpdate
import dash_labs as dl
import pathlib
import pandas as pd
import os

workspace_user = os.getenv('JUPYTERHUB_USER')
request_path_prefix = '/'
if workspace_user:
    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'

APP_PATH = str(pathlib.Path(__file__).parent.resolve())

# df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data\datasets","completedf.csv")),low_memory=False)
df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data/datasets","db_final.csv")),low_memory=False)

df_bibiana = pd.read_csv(os.path.join(APP_PATH, os.path.join("data/datasets","db_final_bibiana.csv")),low_memory=False)

app = dash.Dash(__name__, external_stylesheets=[
                dbc.themes.FLATLY], requests_pathname_prefix=request_path_prefix, plugins=[dl.plugins.pages])

app.config["suppress_callback_exceptions"] = True

items_bar = [
    dbc.NavItem(dbc.NavLink("Inicio", href=request_path_prefix, className="nav-link1")),

    dbc.NavItem(dbc.NavLink("Page-1", href=request_path_prefix+"page1", className="nav-link2")),
    
    dbc.NavItem(dbc.NavLink("Page-2", href=request_path_prefix+"page2", className="nav-link3")),
]

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src=app.get_asset_url('imgs/logo.png'), height="30px"),
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
            ),

            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    items_bar,
                    className="ml-auto",
                    navbar=True,
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),

        ],
        className="navbar-nav",
        fluid=True,

    ),
    className="mb-2 fixed-top container-fluid",
    color="#A9BA18",
    dark=True,
)


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    pass
    if n:
        return not is_open
    return is_open

# main layout
app.layout = html.Div(
    [
        navbar,
        dl.plugins.page_container,
    ],
)

server = app.server

# if __name__ == '__main__':
#     app.run_server(host="0.0.0.0", port="8050", debug=True)

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050, debug=True, dev_tools_ui=False)
    # app.run_server(debug=False,dev_tools_ui=False,dev_tools_props_check=False)