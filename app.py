import dash
import dash_bootstrap_components as dbc
from layout import create_layout
from callbacks import register_callbacks

# Create Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

# Set the layout
app.layout = create_layout()

# Register all callbacks
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True) 