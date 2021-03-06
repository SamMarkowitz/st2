# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from st2actions.runners.pythonrunner import Action
import json
import os

GITINFO_FILE = '.gitinfo'


class PackInfo(Action):
    def run(self, pack, pack_dir="/opt/stackstorm/packs"):
        gitinfo = os.path.join(pack_dir, pack, GITINFO_FILE)
        try:
            with open(gitinfo) as data_file:
                details = json.load(data_file)
                return details
        except:
            print "Unable to load git info for {}".format(pack)
