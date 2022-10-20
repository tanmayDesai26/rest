#!/bin/bash

# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START startup_script]
echo "inside startup script"
sudo apt-get update
sudo apt-get install -y python3 python3-pip git
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install --upgrade Pillow
sudo pip3 install numpy
sudo pip3 install requests
sudo pip3 install flask
sudo pip3 install jsonpickle
sudo pip3 install grpcio-tools
mkdir -p lab6
cd /lab6
curl http://metadata/computeMetadata/v1/instance/attributes/rest-client -H "Metadata-Flavor: Google" > rest-client.py
curl http://metadata/computeMetadata/v1/instance/attributes/rest-server -H "Metadata-Flavor: Google" > rest-server.py
curl http://metadata/computeMetadata/v1/instance/attributes/grpc-server -H "Metadata-Flavor: Google" > grpc-server.py
curl http://metadata/computeMetadata/v1/instance/attributes/grpc-client -H "Metadata-Flavor: Google" > grpc-client.py
curl http://metadata/computeMetadata/v1/instance/attributes/lab6-proto -H "Metadata-Flavor: Google" > lab6.proto
curl http://metadata/computeMetadata/v1/instance/attributes/flatirons_Winter_Sunrise_edit_2 -H "Metadata-Flavor: Google" > Flatirons_Winter_Sunrise_edit_2.jpg

sudo python3 -m grpc_tools.protoc --proto_path=. ./lab6.proto --python_out=. --grpc_python_out=.


# [END startup_script]
