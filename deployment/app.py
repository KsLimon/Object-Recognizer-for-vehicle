from fastai.vision.all import *
import gradio as gr

obj_labels = (
    "Cars",
    "Trucks",
    "Traffic signals",
    "Road markings",
    "Construction zones",
    "Animals",
    "Road obstacles",
    "Pedestrians",
    "Emergency vehicles",
    "Bicycles",
    "Motorcycles",
    "Buses",
    "Road works",
    "Drones",
    "Zebra crossing"
)

model = load_learner('obj-recognizer-v2.pkl')

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return pred

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label(num_top_classes=5)
examples = [
    'TrafficSignals.jpg',
    'RoadWorks.jpg',
    'trucks.jpg',
    'Ped.png',
    'test.jpg'
    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)