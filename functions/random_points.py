import numpy as np
import plotly.graph_objects as go


def random_points(nb_points):

    latitude_range = (48.8167, 48.9026)  # Approximate latitude range for Paris
    longitude_range = (2.25, 2.41)   # Approximate longitude range for Paris

    random_coordinates = []
    for _ in range(nb_points):
        latitude = np.random.uniform(latitude_range[0], latitude_range[1])
        longitude = np.random.uniform(longitude_range[0], longitude_range[1])
        random_coordinates.append((latitude, longitude))

    fig = go.Figure(go.Scattermapbox(
            customdata=[f"Point {i+1}" for i in range(nb_points)],
            lat=[coord[0] for coord in random_coordinates],
            lon=[coord[1] for coord in random_coordinates],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=8
            ),
            hoverinfo="text",
            hovertemplate='%{customdata}',
        ))

    fig.update_layout(
        mapbox_style="open-street-map",
        hovermode='closest',
        mapbox=dict(
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=latitude_range[0] + (latitude_range[1] - latitude_range[0]) / 2,
                lon=longitude_range[0] + (longitude_range[1] - longitude_range[0]) / 2
            ),
            pitch=0,
            zoom=11
        ),
    )

    return fig
