import gradio as gr
import pandas as pd
import joblib
import numpy as np

model = joblib.load('happiness-model.pkl')

def predict_happiness(economy, family, health, freedom, trust, generosity):
    input_data = pd.DataFrame({
        'Economy (GDP per Capita)': [economy],
        'Family': [family],
        'Health (Life Expectancy)': [health],
        'Freedom': [freedom],
        'Trust (Government Corruption)': [trust],
        'Generosity': [generosity]
    })
    
    prediction = model.predict(input_data)[0]
    predicted_rank = int(round(prediction))
    
    if predicted_rank <= 30:
        label = "Very High 😊"
    elif predicted_rank <= 60:
        label = "High 🙂"
    elif predicted_rank <= 90:
        label = "Medium 😐"
    elif predicted_rank <= 120:
        label = "Low 🙁"
    else:
        label = "Very Low 😞"
        
    plot_data = pd.DataFrame({
        'Factor': ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity'],
        'Value': [economy, family, health, freedom, trust, generosity]
    })

    return f"{predicted_rank}", label, plot_data

with gr.Blocks(theme=gr.themes.Soft(primary_hue="sky", secondary_hue="rose")) as demo:
    gr.Markdown(
        """
        # 😃 World Happiness Rank Predictor
        Adjust the sliders to see the predicted happiness rank for a country based on key socio-economic factors. 
        The prediction is powered by a Random Forest model.
        """
    )
    
    with gr.Row(variant="panel"):
        # Input controls
        with gr.Column(scale=1):
            gr.Markdown("### ⚙️ Input Factors")
            economy = gr.Slider(minimum=0.0, maximum=2.0, step=0.01, label="Economy (GDP per Capita)", value=1.0)
            family = gr.Slider(minimum=0.0, maximum=2.0, step=0.01, label="Family (Social Support)", value=1.0)
            health = gr.Slider(minimum=0.0, maximum=1.5, step=0.01, label="Health (Life Expectancy)", value=0.8)
            freedom = gr.Slider(minimum=0.0, maximum=1.0, step=0.01, label="Freedom to make life choices", value=0.5)
            trust = gr.Slider(minimum=0.0, maximum=1.0, step=0.01, label="Trust (Government Corruption)", value=0.1)
            generosity = gr.Slider(minimum=0.0, maximum=1.0, step=0.01, label="Generosity", value=0.2)
            
            inputs = [economy, family, health, freedom, trust, generosity]

        # Output displays
        with gr.Column(scale=2):
            gr.Markdown("### 📊 Results")
            with gr.Row():
                with gr.Column(scale=1, min_width=200):
                    gr.Markdown("<h3 style='text-align: center;'>Predicted Rank</h3>")
                    output_rank = gr.Textbox(
                        label="", 
                        value="78", 
                        interactive=False, 
                        elem_classes=["big-number"]
                    )
                with gr.Column(scale=1, min_width=200):
                    gr.Markdown("<h3 style='text-align: center;'>Happiness Level</h3>")
                    output_label = gr.Textbox(
                        label="", 
                        value="Medium 😐", 
                        interactive=False,
                        elem_classes=["big-number", "label-box"]
                    )
            
            output_plot = gr.BarPlot(
                x="Factor", 
                y="Value", 
                title="Input Factor Contributions",
                vertical=False,
                min_width=400,
            )

    for slider in inputs:
        slider.release(predict_happiness, inputs=inputs, outputs=[output_rank, output_label, output_plot])

demo.launch()

