# JPWAV-AI: 



# <p align="center">Audio Sentiment Analysis Software</p>
  
This is a project aimed at setting up an application allowing the analysis of emotions of a recorded voice based on a large set of audio data.

The repo is composed of 3 main parts: **Data Science**, **API** and **Software**
Each part work independently and the union of those 3 parts is the **Software**

The progress of the part devoted to the deployment of the api in *Azure* is available on this secondary repo: https://github.com/JeanPhilippeCaetano/Audio-Sentiment-Analysis-Software-Deployment

## 🛠️ Tech Stack
- [Python](https://www.python.org/)
- [PyQt5](https://www.qt.io/qt-for-python/)
- [Azure](https://azure.microsoft.com/)
- [Jupyter Notebook](https://jupyter.org/)
- A lot of Data Science library 
    


## 🛠️ Install Dependencies
Go in the folder of the part that you want to run (between **Data**, **API** and **Software**) and install dependencies through the requirements.txt included in each parts.

### Software:
```bash
`Python3 run main.py`
```
### Run API in local:
```bash
`uvicorn main:app --reload`
```
#### ➤ API Reference: Submit form
```http
POST /predict
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `features`   | `list[list[float]]`  shape: ( ,40)   | **Required**. Melscale (MFCC) of audio file |
```http
GET /docs
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None`   | `None` | Test part providel by **FastAPI**|



Data Science:

`Open our notebooks and have fun ;)`







## 🙇 Author
#### Jean-Philippe Caetano
- Linkedin: [@jean-philippe-caetano-b30327229](https://www.linkedin.com/in/jean-philippe-caetano-b30327229/)
- Github: [@JeanPhilippeCaetano](https://github.com/JeanPhilippeCaetano)
#### Wassim Saioudi
- Linkedin: [@wassim-saioudi](https://www.linkedin.com/in/wassim-saioudi)
- Github: [@2va2s](https://github.com/2va2s)
    

## ➤ License
No license provided.

# Thank to anyone whose work has inspired us ! ❤       
