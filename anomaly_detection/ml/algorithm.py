# Copyright 2019 The OpenSDS Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class AlgorithmBase:
    def __init__(self, *args, **kwargs):
        self.algorithm_name = kwargs.get("algorithm_name")

    def create_training(self, training):
        raise NotImplemented

    def get_training_pic(self, training):
        raise NotImplemented

    def prediction(self, training, dataset):
        raise NotImplemented

    def get_prediction_pic(self, training, dataset):
        raise NotImplemented