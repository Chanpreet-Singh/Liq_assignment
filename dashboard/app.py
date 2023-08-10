import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback

from dashboard.helper import Dashboard_helper
helper_obj = Dashboard_helper()
all_salesperson = helper_obj.get_all_salesperson_data()
app = Dash(__name__)

title = "Monthly sales"

app.layout = html.Div([
                                html.H1("View monthly sales of employees"),
                                dcc.Graph(id='bar-graph'),
                                dcc.Dropdown(
                                                id='salesperson_id',
                                                options=all_salesperson,
                                                value=all_salesperson[0]["value"],
                                                placeholder="Which employee?",
                                            )
                                    ]
                    )
@callback(Output("bar-graph", "figure"), Input("salesperson_id", "value"))
def update_output(value):
    output_df = helper_obj.get_salesperson_data(value)
    fig = px.bar(output_df, x='month', y='Total_Amount')
    return fig




if __name__ == '__main__':
    app.run(debug=True)