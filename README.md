# Application that takes a hand written digit and replies with the digit written. (Serverlessly)


### 1. Write App (Flask, TensorFlow)
- The code to build, train, and save the model is in the `test` folder.
- Implement the app in `main.py`
### 2. Setup Google Cloud 
- Create new project
- Activate Cloud Run API and Cloud Build API

### 3. Install and init Google Cloud SDK
- https://cloud.google.com/sdk/docs/install

### 4. Dockerfile, requirements.txt, .dockerignore
- https://cloud.google.com/run/docs/quickstarts/build-and-deploy#containerizing

### 5. Cloud build & deploy
```
gcloud builds submit --tag gcr.io/cs329s-339009/index
gcloud run deploy --image gcr.io/cs329s-339009/index --platform managed
```

### Test
- Test the code with `test/test.py`

credit : https://youtu.be/vieoHqt7pxo
