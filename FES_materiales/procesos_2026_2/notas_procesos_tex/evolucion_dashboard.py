import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State

# ── Cadena de géneros musicales ──────────────────────────────────────────────
# Estados: 0 = Pop, 1 = Rock, 2 = Jazz
# Filas de P: distribución de transición desde cada estado
P_MATRIX = np.array([
    [0.50, 0.50, 0.00],  # desde Pop
    [0.25, 0.50, 0.25],  # desde Rock
    [0.50, 0.00, 0.50],  # desde Jazz
])
STATES = ["Pop", "Rock", "Jazz"]
COLORS = ["#636EFA", "#EF553B", "#00CC96"]


def simulate(N: int, n: int, pi0: np.ndarray) -> np.ndarray:
    """Simula N trayectorias de longitud n+1. Devuelve array (N, n+1)."""
    traj = np.empty((N, n + 1), dtype=np.int8)
    traj[:, 0] = np.random.choice(3, size=N, p=pi0)
    for t in range(n):
        cumP = P_MATRIX[traj[:, t]].cumsum(axis=1)
        r = np.random.rand(N, 1)
        traj[:, t + 1] = (r > cumP).sum(axis=1)
    return traj


def empty_fig(title, yaxis_title=""):
    fig = go.Figure()
    fig.update_layout(
        title=title,
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(l=65, r=10, t=50, b=50),
        height=460,
        yaxis_title=yaxis_title,
    )
    return fig


# ── App ───────────────────────────────────────────────────────────────────────
app = Dash(__name__)
_ctrl = {"fontFamily": "sans-serif"}

app.layout = html.Div(
    [
        html.H3(
            "Evolución de la distribución de Xₙ — Géneros musicales",
            style={"fontFamily": "sans-serif", "textAlign": "center", "marginBottom": "8px"},
        ),
        html.Div(
            [
                # ── Panel de controles ────────────────────────────────────────
                html.Div(
                    [
                        html.H4("Parámetros", style={"marginTop": 0, **_ctrl}),

                        html.Label("Tiempo n", style={"fontWeight": "bold", **_ctrl}),
                        dcc.Slider(
                            id="sl-n", min=1, max=50, step=1, value=10,
                            marks={v: str(v) for v in [1, 5, 10, 20, 30, 50]},
                            tooltip={"placement": "bottom", "always_visible": True},
                        ),
                        html.Br(),

                        html.Label("Trayectorias N", style={"fontWeight": "bold", **_ctrl}),
                        dcc.Slider(
                            id="sl-N", min=20, max=1000, step=20, value=200,
                            marks={v: str(v) for v in [20, 100, 200, 500, 1000]},
                            tooltip={"placement": "bottom", "always_visible": True},
                        ),
                        html.Br(),

                        html.Label("Distribución inicial π⁽⁰⁾", style={"fontWeight": "bold", **_ctrl}),
                        html.Div(
                            [
                                html.Div([
                                    html.Label("Pop", style=_ctrl),
                                    dcc.Input(id="pi0", type="number", value=1.0,
                                              min=0, max=1, step=0.05, style={"width": "50px"}),
                                ]),
                                html.Div([
                                    html.Label("Rock", style=_ctrl),
                                    dcc.Input(id="pi1", type="number", value=0.0,
                                              min=0, max=1, step=0.05, style={"width": "50px"}),
                                ]),
                                html.Div([
                                    html.Label("Jazz", style=_ctrl),
                                    dcc.Input(id="pi2", type="number", value=0.0,
                                              min=0, max=1, step=0.05, style={"width": "50px"}),
                                ]),
                            ],
                            style={"display": "flex", "gap": "10px",
                                   "marginTop": "6px", "alignItems": "flex-end"},
                        ),
                        html.Small("(Se normalizan automáticamente)",
                                   style={"color": "#888", "fontFamily": "sans-serif"}),
                        html.Br(), html.Br(),

                        html.Button(
                            "▶  Generar trayectorias",
                            id="btn", n_clicks=0,
                            style={
                                "backgroundColor": "#4CAF50", "color": "white",
                                "padding": "10px 16px", "border": "none",
                                "borderRadius": "6px", "cursor": "pointer",
                                "fontSize": "14px", "width": "100%",
                                "fontFamily": "sans-serif",
                            },
                        ),
                        html.Div(id="info", style={"marginTop": "8px", "color": "#555",
                                                    "fontSize": "13px", "fontFamily": "sans-serif"}),
                        html.Hr(),

                        # Tabla de la matriz P
                        html.H5("Matriz P", style={"marginBottom": "4px", **_ctrl}),
                        html.Table(
                            [
                                html.Thead(html.Tr(
                                    [html.Th("")] +
                                    [html.Th(s, style={"textAlign": "center", "padding": "2px 8px"})
                                     for s in STATES]
                                )),
                                html.Tbody([
                                    html.Tr(
                                        [html.Td(STATES[i],
                                                 style={"fontWeight": "bold", "padding": "2px 8px"})] +
                                        [html.Td(f"{P_MATRIX[i, j]:.2f}",
                                                 style={"textAlign": "center", "padding": "2px 8px"})
                                         for j in range(3)]
                                    )
                                    for i in range(3)
                                ]),
                            ],
                            style={"fontSize": "13px", "borderCollapse": "collapse",
                                   "fontFamily": "sans-serif"},
                        ),
                    ],
                    style={
                        "width": "240px", "padding": "16px", "flexShrink": "0",
                        "backgroundColor": "#f8f9fa", "borderRadius": "8px",
                        "boxSizing": "border-box",
                    },
                ),

                # ── Gráfica de trayectorias ───────────────────────────────────
                html.Div(
                    [dcc.Graph(id="g-traj",
                               figure=empty_fig("Trayectorias (presiona ▶ Generar)", "Estado"))],
                    style={"flex": "3", "minWidth": 0},
                ),

                # ── Histograma ────────────────────────────────────────────────
                html.Div(
                    [dcc.Graph(id="g-hist",
                               figure=empty_fig("Distribución estimada de Xₙ", "Probabilidad"))],
                    style={"flex": "1.6", "minWidth": 0},
                ),
            ],
            style={"display": "flex", "gap": "14px", "alignItems": "flex-start"},
        ),
    ],
    style={"padding": "16px", "maxWidth": "1500px", "margin": "0 auto"},
)


@app.callback(
    Output("g-traj", "figure"),
    Output("g-hist", "figure"),
    Output("info", "children"),
    Input("btn", "n_clicks"),
    State("sl-n", "value"),
    State("sl-N", "value"),
    State("pi0", "value"),
    State("pi1", "value"),
    State("pi2", "value"),
    prevent_initial_call=True,
)
def update(_, n, N, p0, p1, p2):
    # Normalizar distribución inicial
    pi0 = np.array([p0 or 0.0, p1 or 0.0, p2 or 0.0], dtype=float)
    s = pi0.sum()
    pi0 = pi0 / s if s > 0 else np.ones(3) / 3

    traj = simulate(N, n, pi0)
    time_steps = list(range(n + 1))
    alpha = round(max(0.04, min(0.45, 25 / N)), 3)

    # ── Trayectorias ─────────────────────────────────────────────────────────
    fig_t = go.Figure()

    jitter_scale = 0.18
    jitter = np.random.uniform(-jitter_scale, jitter_scale, size=(N, n + 1))
    traj_j = traj.astype(float) + jitter

    for i in range(N):
        fig_t.add_trace(go.Scatter(
            x=time_steps,
            y=traj_j[i].tolist(),
            mode="lines",
            line=dict(width=0.9, color=f"rgba(80,100,200,{alpha})"),
            showlegend=False,
            hoverinfo="skip",
        ))

    # Puntos en t=n coloreados por estado
    for j, (state, color) in enumerate(zip(STATES, COLORS)):
        mask = traj[:, n] == j
        if mask.any():
            fig_t.add_trace(go.Scatter(
                x=[n] * int(mask.sum()),
                y=[j] * int(mask.sum()),
                mode="markers",
                marker=dict(color=color, size=6, opacity=0.8),
                name=state,
                legendgroup=state,
            ))

    fig_t.update_layout(
        title=f"N = {N} trayectorias  |  π⁽⁰⁾ = ({pi0[0]:.2f}, {pi0[1]:.2f}, {pi0[2]:.2f})",
        xaxis_title="Tiempo",
        yaxis=dict(tickvals=[0, 1, 2], ticktext=STATES,
                   title="Estado", range=[-0.4, 2.4]),
        plot_bgcolor="white", paper_bgcolor="white",
        margin=dict(l=65, r=10, t=55, b=50),
        height=460,
        legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="right", x=1),
    )

    # ── Histograma en t = n ───────────────────────────────────────────────────
    counts = np.bincount(traj[:, n], minlength=3)
    props = counts / N

    # Distribución teórica: pi^(0) P^n
    exact = np.linalg.matrix_power(P_MATRIX, n).T @ pi0  # shape (3,)

    fig_h = go.Figure([
        # Barras Monte Carlo (rellenas)
        go.Bar(
            x=STATES,
            y=props,
            marker_color=COLORS,
            name="Simulación MC",
            text=[f"{p:.3f}" for p in props],
            textposition="outside",
            textfont=dict(size=12),
        ),
        # Barras teóricas (solo borde, sin relleno)
        go.Bar(
            x=STATES,
            y=exact,
            marker=dict(
                color="rgba(0,0,0,0)",
                line=dict(color="black", width=3),
            ),
            name="Teórica π⁽⁰⁾Pⁿ",
            text=[f"{p:.3f}" for p in exact],
            textposition="inside",
            textfont=dict(size=11, color="black"),
        ),
    ])
    fig_h.update_layout(
        title=f"P̂(X_{n} = ·)  vs  distribución teórica",
        xaxis_title="Estado",
        yaxis=dict(range=[0, 1.12], title="Probabilidad"),
        barmode="overlay",
        plot_bgcolor="white", paper_bgcolor="white",
        margin=dict(l=65, r=10, t=80, b=50),
        height=460,
        legend=dict(orientation="h", yanchor="top", y=1.12, xanchor="right", x=1),
    )

    info = f"✓ {N} trayectorias simuladas hasta t = {n}."
    return fig_t, fig_h, info


if __name__ == "__main__":
    app.run(debug=True, port=8050)
