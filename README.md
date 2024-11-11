# Serverless Vehicular Edge Computing for the Internet of Vehicles

# Summary
We setup the project in 3 major sections
- Section 1(Sumo suimulation)
   - Using sumo tool we fed an openstreet view map and were able to generate some routes.xml
   - This was populated with car positions along with their speeds replicating a practical simulation
- Section 2(Mininet Simulation)
   - We configured the APs and cars on mininet-wifi cli.
   - Using this we were able to configure and test connectivity between cars
   - This also ensured a practical demonstration of the network
- Section 3(Integration)
   - Set Up a Dynamic Cluster for Vehicles Using Minikube and OpenFaaS:
     - Use Minikube to manage containers for edge computation, where each vehicle acts as a Docker container that can join or leave the network dynamically.
     - Deploy OpenFaaS on the Minikube cluster, allowing vehicles to offload computational tasks to nearby roadside units (RSUs). This setup would enable serverless functions to scale as cars enter or exit an RSU's range.
   - Automate Container Creation and Removal:
     - When a vehicle comes within an RSU's range, a Python script (running on Mininet-WiFi) triggers the Minikube orchestrator to add the vehicle's container to the cluster.
     - When the vehicle moves out of range, Minikube should automatically remove it, preventing unnecessary computation on distant RSUs and conserving resources.
  

# Prerequisites
- SUMO:  Simulation of Urban MObility for traffic simulation.
- Mininet-WiFi:  Mininet extension for Wi-Fi network simulations.
- Ubuntu 20.04 or later: Recommended for compatibility with SUMO and Mininet-WiFi.
- Python 3.6+:  Required for running the simulation scripts

# Installation
## MiniKube

```bash
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube

sudo install minikube-linux-amd64 /usr/local/bin/minikube

minikube start --driver=docker

kubectl get nodes

minikube dashboard

```
## Open Faas

```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

helm version

minikube start

kubectl config use-context minikube

kubectl create namespace openfaas
kubectl create namespace openfaas-fn

helm repo add openfaas https://openfaas.github.io/faas-netes/
helm repo update

helm install openfaas openfaas/openfaas \
  --namespace openfaas \
  --set basic_auth=true \
  --set functionNamespace=openfaas-fn

kubectl get pods -n openfaas
kubectl get svc -n openfaas

kubectl port-forward svc/gateway -n openfaas 8080:8080

### Get the OpenFaaS Credentials: The default username for OpenFaaS is admin. To get the password, run the following command:

kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode

```
## SUMO

```bash
sudo apt-get install sumo sumo-tools sumo-doc

sumo --version

sudo apt-get install cmake g++ libxerces-c-dev libfox-1.6-0 libgdal-dev libproj-dev python3

git clone https://github.com/eclipse/sumo.git
cd sumo

mkdir build/cmake-build
cd build/cmake-build
cmake ../..
make -j$(nproc)
sudo make install

sumo --version
```
## Mininet-Wifi

```bash
sudo apt-get install -y git python3-setuptools python3-pip \
    python3-matplotlib build-essential gcc libssl-dev \
    libffi-dev iproute2 ethtool wireless-tools \
    python3-scapy python3-networkx

git clone https://github.com/intrig-unicamp/mininet-wifi.git
cd mininet-wifi

sudo util/install.sh -Wlnfv


```

## Running the Simulation

```bash
###this will open the mininet-CLI and GUI
sudo python3 nwtwork.py
```



# Setup
The following images explain how we are setting up the MININET CLI and with the topology to add the cars with the Access Points.


![Screenshot from 2024-11-11 18-02-48](https://github.com/user-attachments/assets/37e3a135-72e9-48ed-a014-89ee6cd2663c)

# Sumo Simulation to run the cars
![Screenshot from 2024-11-11 18-55-01](https://github.com/user-attachments/assets/c8e79d81-0148-4e2f-87f4-307d037f0e5e)

# Sumo Simulation of a Map
![Screenshot from 2024-11-11 18-52-24](https://github.com/user-attachments/assets/35fff0cc-acb7-4860-a616-645404ef183c)

# Checking for possible Links
![Screenshot from 2024-11-11 18-06-34](https://github.com/user-attachments/assets/7b3a140a-b1dd-4f63-8c05-1377c49fab9d)

# Checking Throughput
![Screenshot from 2024-11-11 18-06-19](https://github.com/user-attachments/assets/2373977a-a94b-4a94-ba38-2bb7ec78ccf1)

# Dynamic Positioning of cars 
![Screenshot from 2024-11-11 18-05-31](https://github.com/user-attachments/assets/5755bf50-145a-432f-90ac-8a16df281b04)

# Printing car IP
![Screenshot from 2024-11-11 18-04-50](https://github.com/user-attachments/assets/a763c75d-6273-4a88-b1fa-d71b548300a9)

# Pinging from cars to AP's
![Screenshot from 2024-11-11 18-04-36](https://github.com/user-attachments/assets/61dcf4c3-bcfb-4584-a6e8-977a327f87c9)
![Screenshot from 2024-11-11 18-04-15](https://github.com/user-attachments/assets/879d32c2-ed6a-4ea6-b30a-1029d25bbc03)
![Screenshot from 2024-11-11 18-04-09](https://github.com/user-attachments/assets/cf927c78-8761-474b-8a59-23793ebfa535)

# Video demonstrating setting up the Cars with AP's
- Demonstracting the Cars moving with the given AP

[Screencast from 11-11-24 06:49:32 PM IST.webm](https://github.com/user-attachments/assets/ee38122d-6713-44e3-814d-4916103ee925)



