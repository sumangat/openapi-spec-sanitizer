from loader import Loader
from stateful import Stateful
from analyzer import Analyzer, State
import yaml
from yaml.loader import FullLoader
from icecream import ic
import copy


class Splitter(Stateful):
    def __init__(self, args):
        super().__init__(State.UNKNOWN)
        self.output_filename = args.output
        self.loader = Loader(args)
        self.tags = args.tags

    def split_yaml(self, file: str) -> dict:
        with open(file) as f:
            data = yaml.load(f, Loader=FullLoader)
            data_new = copy.deepcopy(data)
            for path in data['paths']:
                ic(path)
                for key in (data['paths'][path].keys()):
                    if key in ['get', 'post', 'delete', 'put']:
                        # Define what tags you want to keep in the YAML
                        if data['paths'][path][key]['tags'][0] not in self.tags:
                            ic(data['paths'][path][key]['tags'])
                            try:
                                del data_new['paths'][path]
                            except KeyError as ex:
                                ic("already removed")

        return data_new
