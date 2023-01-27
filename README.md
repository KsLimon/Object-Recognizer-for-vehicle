![alt text](https://mastercourse.site/wp-content/uploads/2020/12/cropped-Mastercourseweblogo-07-1-e1615404376389-300x38.png)  

Dokkho Data Science C1: Capstone Project 2

# Object-Recognizer-for-autonomous-vehicle

## Introduction
This project, named "Object Recognizer for Autonomous Vehicles," is a machine learning model that is trained to recognize and classify various objects that can be found on the road. The model was trained using the FastAI library, and PyTorch as the deep learning framework. The model utilizes a ResNet34 architecture and was trained on a dataset of 3000 images of 15 different types of objects commonly found on the road.

The objects that the model is trained to recognize include:

1. Cars
2. Trucks
3. Traffic signals: such as stop signs, traffic lights, and road signs
4. Road markings: such as lane lines, crosswalks, and pavement markings
5. Construction zones: such as cones, barriers, and construction vehicles
6. Animals: such as wild animals, domestic animals, and farm animals
7. Road obstacles: such as fallen trees, debris, and potholes
8. Pedestrians: people walking, jogging or cycling
9. Emergency vehicles: such as ambulances, fire trucks, and police cars
10. Bicycles: individual or group of people riding bicycles
11. Motorcycles: individual or group of people riding motorcycles
12. Buses
13. Road works: construction workers, heavy machinery, excavation
14. Drones: flying drones in the vicinity of the vehicle
15. Zebra crossing

## Data
The dataset used for training the model consists of 3000 images of various sizes and aspect ratios. The images were resized to 256x256 pixels and normalized to improve model performance.

## Model
The model used for this project is a ResNet34 architecture trained using the fastai library. The model achieved an accuracy of 85.66% on the validation set.

## ResNet34 and FastAI
The ResNet34 architecture is a deep residual network that was introduced in the paper "Deep Residual Learning for Image Recognition" by He et al. It is a 34-layer deep neural network that utilizes residual connections to alleviate the vanishing gradient problem and improve the flow of information through the network.

FastAI is a library built on top of PyTorch that provides high-level APIs for training and deploying machine learning models. It is designed to make it easy for practitioners to train and deploy models in a fast and efficient way, and it is particularly well-suited for computer vision tasks.

## Deployment
The model is deployed using Hugging Face's Model Hub and can be accessed through the following links:
- App link: https://huggingface.co/spaces/KamrusSamad/object-recognizer-for-vehicle
- API link: https://kamrussamad-object-recognizer-for-vehicle.hf.space/run/predict

## How to use the model
The model can be used by sending a post request to the API link https://kamrussamad-object-recognizer-for-vehicle.hf.space/run/predict with the image file attached to the request body. The response will be in json format and will contain the object class and the probability of the image belonging to that class.

## Limitations
As with any machine learning model, the performance of this object recognizer may be affected by factors such as image resolution, lighting conditions, and the presence of occlusions. Additionally, the model's performance on new, unseen data may not match its performance on the validation set. Dataset also a mejor issue because it has no enough data.

## Contributions
I would be happy to accept any contributions to this project. If you would like to contribute, please open a pull request with a detailed explanation of your changes.

## Future Work
Future work on this project could include fine-tuning the model on a larger and more diverse dataset, experimenting with different architectures and training techniques, and incorporating additional data such as lidar or radar measurements.

## Conclusion
This project demonstrates the use of deep learning techniques for object recognition in autonomous vehicles using the fastai library and PyTorch framework. The model achieved good accuracy and can be used for various applications such as self-driving cars, drones and other autonomous systems.
