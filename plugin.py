# %%
import gradio as gr

def calculate_time(epochs, seconds_per_epoch):
    total_time = epochs * seconds_per_epoch
    hours = total_time // 3600
    minutes = (total_time % 3600) // 60
    seconds = total_time % 60
    if hours == 0:
        return f"{int(minutes)} minutes."
    elif hours == 1:
        return f"{int(hours)} and {int(minutes)} minutes."
    else:
        return f"{int(hours)} hours and {int(minutes)} minutes."

def applio_plugin():
    gr.Markdown(value="Calculate the total amount of time for a training session.")
    with gr.Blocks() as app:
        with gr.Column():
            epochs_input = gr.Number(label="Number of epochs.")
            seconds_input = gr.Number(label="Seconds per epoch.")
            calculate_button = gr.Button("Calculate time remaining")
            remaining_time_output = gr.Textbox(label="Remaining time", interactive=False)

            calculate_button.click(calculate_time, inputs=[epochs_input, seconds_input], outputs=[remaining_time_output])


