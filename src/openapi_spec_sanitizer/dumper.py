#######################################################################
# openapi-spec-sanitizer
# Copyright David Turland 2023
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
########################################################################

__all__ = ['Dumper']

import json
import os
from pathlib import Path

import yaml

from exceptions import InvalidFileException
from loader import Loader, OpenapiFormat


class Dumper:
    def __init__(self, loader, args):
        self.loader = loader

    def dump(self, filename, data):
        loader_filename = self.loader.get_filename()
        if filename is None:
            if loader_filename is None:
                raise InvalidFileException()
            root, ext = os.path.splitext(loader_filename)
            filename = f"{root}.san{ext}"
        elif loader_filename is not None:
            if loader_filename == filename:
                raise InvalidFileException(f"will not overwrite original file {filename}")
        if Path(filename).exists():
            raise InvalidFileException(f"will not overwrite existing file {filename}")

        with open(filename, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, width=1000)
