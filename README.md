# CSE812_Project_Group2
## Group Member
Samiul Alam, Hongzhi Wen, Jun Guo

## Project Abstract
Federated learning (FL) is a collaborative method to train models from decentralised private data. The process can be formulated as solving an optimization problem under constraint of minimizing communication overhead while ensuring robustness of model with heterogeneous data and privacy. However, in practical settings, even these constraints are an oversimplification. While most FL research work is focus on data heterogeneity, it is important to also optimize for model heterogeneity. Most FL algorithms assume all endpoint models have the exact same architectures and compute power. But in modern distributed systems, it is likely that devices will have vastly different compute powers and may even have hardware to accelerate specific kinds of neural networks. Therefore it is essential to have a more inclusive FL algorithm. We propose a FL system that would be model and data distribution agnostic and will have the potential to be deployed in real world scenarios. 

## Install Requirements
pip3 install -r requirements.txt

## Run experiments
python main.py --dataset Mnist-alpha0.1-ratio0.5 --algorithm FedGen --batch_size 32 --num_glob_iters 200 --local_epochs 20 --num_users 10 --lamda 1 --learning_rate 0.01 --model cnn --personal_learning_rate 0.01 --times 3 

## Experiment Settings
To modify the experiment settings, please edit `utils.model_config.py` file, where `'mnist_0'` and `''mnist_1''` are configs for user models.

## Acknowledgement
This source code is based on the official implementation of FedGen (https://github.com/zhuangdizhu/FedGen).
