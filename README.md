# DeepLearning - RNN 

Installation Instructions (MAC OS)


Simple RNN Example with Tensorflow

```shell
#Clone Repo
git clone https://github.com/harsha91/DeepLearning.git

#Install/Upgrade Virtual Env
sudo pip install --upgrade virtualenv
#Enter Folder
cd DeepLearning

#Create & Activate VirtualEnv
virtualenv env
source env/bin/activate

#Install Tensorflow
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0rc0-py2-none-any.whl
pip install --upgrade $TF_BINARY_URL

#Run Program
python ptb_word_lm.py --data_path=simple-examples/data/
```
Simple Example of LSTM, using Keras

```shell

# Skip the clone and activation of the virtualenv if already done!
#Clone Repo
git clone https://github.com/harsha91/DeepLearning.git

#Install/Upgrade Virtual Env
sudo pip install --upgrade virtualenv
#Enter Folder
cd DeepLearning

#Create & Activate VirtualEnv
virtualenv env
source env/bin/activate

#Install kera
pip install keras

#by default keras uses Theno backend
#Change keras backend
sudo open ~/.keras/keras.json
#change the json file  
{"epsilon": 1e-07, "floatx": "float32", "backend": "tensorflow"}

#Run Program
python imdb_lstm.py

```


