import gradio as gr

from functions.plank_session import generate_plank_session
from functions.random_points import random_points
from functions.week_end import generate_weekend_program

with gr.Blocks() as demo:
    with gr.Tab(label="Random Points"):
        with gr.Column():
            with gr.Row():
                nb_points = gr.Number(value=2, label="Number of points")
                btn = gr.Button(value="Draw")
            map = gr.Plot()
        btn.click(random_points, [nb_points], map)
    with gr.Tab(label="Plank session"):
        btn = gr.Button(value="Generate plank session")
        session = gr.Markdown()
        btn.click(generate_plank_session, [], session)
    with gr.Tab(label="Generate week-end program"):
        btn = gr.Button(value="Generate week-end program")
        program = gr.Markdown()
        btn.click(generate_weekend_program, [], program)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
