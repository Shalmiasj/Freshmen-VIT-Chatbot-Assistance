
# Freshmen VIT Chatbot Assistance
A Chatbot is developed to answer queries from VIT freshmen students.Keras sequential neural network model is used to build the chatbot. To retrieve the information, the chatbot is connected to a JSON database and Google Maps for directions

## Overview
Python's Keras sequential Neural Network model is used to build the chatbot. To retrieve the information that is displayed to the user, the chatbot is connected to a Java Script Object Notation (JSON) database. It is also connected to Google Maps, which shows the user destinations that are close to where they need to be. The chatbot will help the students by providing them with amiable assistance.

## Motivation
Vellore Institute of Technology (VIT) is one of India's best universities for engineering. The desire to study at this prestigious university to improve their education is being expressed by several youngsters from all around the globe. Students are prepared to leave behind the comfort of their hometowns to move into the safe and secure living arrangements supplied by the hostels here and foster a happy community in order to acquire multiple professional opportunities. A chatbot is created to answer queries and supply the freshman students who enroll at Vellore Intitute of Technology with the information they need about the campus's amenities, including meals, club activities, classes, and others. With the aid of this chatbot, students may also discover nearby stores, paying guest houses, and fun places to visit on the weekends


## Project Structure

![Workflow](https://imgtr.ee/images/2023/06/17/YD59z.png)


## Data Collection
The data containing the details inside VIT is gathered from the official sources, website and information from senior students. In order to make it simple for the freshmen joining VIT to explore places outside the campus, many restaurants, PGs, hotels, supermarkets related details were collected from various websites and filtered in a way that the places are available near the college campus. Although this chatbot might seem to offer only a limited number of options, all the places mentioned for visiting during weekends can be reached in one to two hour duration and are carefully chosen, keeping in mind the safety and comfort of the students

## Data Description
A dataset is created on our own to train the deep learning model. The data which is required to train the sequential model, predict and respond to user queries is created in a JSON file format and named as intents.json. This intents.json file contains all the data collected in the form of “tags”, “patterns” and “responses”. The intents.json file includes certain categories of things that can happen. For example, greetings, questions on various topics, issues etc. These are some of the categories provided with tags. Tags refers to the keyword that the model extracts from the user queries. There is one specific tag for greeting for which we also specify patterns like good morning, hi, hello, hey, etc. Patterns contain the possible number of ways a sentence can be typed by the user for one specific information. 


## Files 
- `labels.pkl`,`text.pkl` : Only humans can understand the JSON, Python, pictures, and other files used to make this chatbot. Pickle encodes any input data into binary format for the system to process. The encoded files can again be converted to the respective file format with the help of this module. While the model is built, two pickle files namely text.pkl and labels.pkl are created.
- `app.py`: the model is deployed into Flask (a web framework)
- `gmap.py` : A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
- `training.py`: Collected data is preprocessed and trained using sequential model in ANN
- `intents.json`: This intents.json file contains all the data collected in the form of “tags”, “patterns” and “responses”. The intents.json file includes certain categories of things that can happen

## Algorithm Used
- sequential Model

## Packages Used
- Pandas 
- Numpy
- Matplotlib 
- Plotly 
- nltk
- Ipython
- Tensorflow
- Keras
- Pickle
- Random

## Model Building 
The term "sequential" is frequently used in several contexts. Sequential here refers to moving from the input to layer 1, then layer 2, and finally the output. So it is highly directional. Usually, a simple neural network has only a single hidden layer. In a sequential model, one can have any number of hidden layers. They are "linear stacks of layers," where one layer leads to the next layer. It is compact and easy to implement. The sequential model uses a plain stack of layers where each layer has one input and one output tensor. This is how TensorFlow got its name. Each layer functions as a tensor. The layer is a tensor of values, and each node is a tensor as well. It is used for both classification and regression models.

## Web Framework – Flask
Flask is an Open-source micro framework. It is useful for designing web based applications in python. No additional tools or libraries are required. It can import any package from python and work automatically based on the imported package and files. Flask is supported by WSGI(Web Server Gateway Interface) and jinja2 template engine.

## Results
![Screenshot of chatbot's response](https://imgtr.ee/images/2023/06/17/YDVQx.jpg)


## Conclusion

The Freshmen VIT chatbot has been found to produce satisfactory results. The accuracy of the model is 91%, and the loss is 26%. This chatbot is expected to be extremely useful, particularly for students in their first year of college. The chatbot gives precise and straightforward responses, which makes it easier for the user to understand and communicate. The API of Google Maps is very helpful in directing the students to the required destination. This chatbot can be used for various other purposes by just changing the dataset accordingly. Adding more patterns and tags to the intents.json file contributes to the sequential model's accuracy. Future work can include using a SQL database instead of JSON for easier data entry and information retrieval. This web-based chatbot can be developed into an application for usability on all mobile devices.


## Project Structure

![Workflow](https://imgtr.ee/images/2023/06/17/YD59z.png)


## Data Collection
The data containing the details inside VIT is gathered from the official sources, website and information from senior students. In order to make it simple for the freshmen joining VIT to explore places outside the campus, many restaurants, PGs, hotels, supermarkets related details were collected from various websites and filtered in a way that the places are available near the college campus. Although this chatbot might seem to offer only a limited number of options, all the places mentioned for visiting during weekends can be reached in one to two hour duration and are carefully chosen, keeping in mind the safety and comfort of the students

## Data Description
A dataset is created on our own to train the deep learning model. The data which is required to train the sequential model, predict and respond to user queries is created in a JSON file format and named as intents.json. This intents.json file contains all the data collected in the form of “tags”, “patterns” and “responses”. The intents.json file includes certain categories of things that can happen. For example, greetings, questions on various topics, issues etc. These are some of the categories provided with tags. Tags refers to the keyword that the model extracts from the user queries. There is one specific tag for greeting for which we also specify patterns like good morning, hi, hello, hey, etc. Patterns contain the possible number of ways a sentence can be typed by the user for one specific information. 


## Files 
- `labels.pkl`,`text.pkl` : Only humans can understand the JSON, Python, pictures, and other files used to make this chatbot. Pickle encodes any input data into binary format for the system to process. The encoded files can again be converted to the respective file format with the help of this module. While the model is built, two pickle files namely text.pkl and labels.pkl are created.
- `app.py`: the model is deployed into Flask (a web framework)
- `gmap.py` : A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
- `training.py`: Collected data is preprocessed and trained using sequential model in ANN
- `intents.json`: This intents.json file contains all the data collected in the form of “tags”, “patterns” and “responses”. The intents.json file includes certain categories of things that can happen

## Algorithm Used
- sequential Model

## Packages Used
- Pandas 
- Numpy
- Matplotlib 
- Plotly 
- nltk
- Ipython
- Tensorflow
- Keras
- Pickle
- Random

## Model Building 
The term "sequential" is frequently used in several contexts. Sequential here refers to moving from the input to layer 1, then layer 2, and finally the output. So it is highly directional. Usually, a simple neural network has only a single hidden layer. In a sequential model, one can have any number of hidden layers. They are "linear stacks of layers," where one layer leads to the next layer. It is compact and easy to implement. The sequential model uses a plain stack of layers where each layer has one input and one output tensor. This is how TensorFlow got its name. Each layer functions as a tensor. The layer is a tensor of values, and each node is a tensor as well. It is used for both classification and regression models.

## Web Framework – Flask
Flask is an Open-source micro framework. It is useful for designing web based applications in python. No additional tools or libraries are required. It can import any package from python and work automatically based on the imported package and files. Flask is supported by WSGI(Web Server Gateway Interface) and jinja2 template engine.

## Results
![Screenshot of chatbot's response](https://imgtr.ee/images/2023/06/17/YDVQx.jpg)


## Conclusion

The Freshmen VIT chatbot has been found to produce satisfactory results. The accuracy of the model is 91%, and the loss is 26%. This chatbot is expected to be extremely useful, particularly for students in their first year of college. The chatbot gives precise and straightforward responses, which makes it easier for the user to understand and communicate. The API of Google Maps is very helpful in directing the students to the required destination. This chatbot can be used for various other purposes by just changing the dataset accordingly. Adding more patterns and tags to the intents.json file contributes to the sequential model's accuracy. Future work can include using a SQL database instead of JSON for easier data entry and information retrieval. This web-based chatbot can be developed into an application for usability on all mobile devices.



