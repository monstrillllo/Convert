import sys

import pandas as pd
import pyarrow
import pyarrow.parquet


class Convert:
    def __init__(self, args: list) -> None:
        self.args = args
        self.read_args()

    def read_args(self):
        if len(self.args) == 4:
            if self.args[1] == '--csv2parquet':
                self.csv_to_parquet(self.args[2], self.args[3])
            elif self.args[1] == '--parquet2csv':
                self.parquet_to_csv(self.args[2], self.args[3])
            else:
                print('[!]Input error! Try python3 convert.py --help')
        elif len(self.args) == 3 and self.args[1] == '--get-schema':
            self.get_schema(self.args[2])
        elif len(self.args) == 2 and self.args[1] == '--help':
            self.help_()
        else:
            print('[!]Input error! Try python3 convert.py --help')

    def csv_to_parquet(self, src_path, dst_path):
        try:
            parquet = pd.read_csv(src_path)
            parquet.to_parquet(dst_path)
        except Exception as ex:
            print(ex)

    def parquet_to_csv(self, src_path, dst_path):
        try:
            csv_ = pd.read_parquet(src_path, engine='pyarrow')
            csv_.to_csv(dst_path, index=False)
        except Exception as ex:
            print(ex)

    def get_schema(self, path):
        try:
            parquet_file = pyarrow.parquet.read_schema(path)
            print(parquet_file)
        except Exception as ex:
            print(ex)

    def help_(self):
        print('Usage: python3 convert.py [OPTIONS] PATH_TO_FILE NEW_FILE_PATH\n\n'
              'Convert csv to parquet or parquet to csv\n\n'
              'Options:\n\n'
              ' --csv2parquet\t\tconvert file.csv to new_file.parquet\n'
              ' --parquet2csv\t\tconvert file.parquet to new_file.csv\n'
              ' --get-schema\t\treturn schema of the file.parquet\n'
              ' --help\t\t\treturn this message\n')


if __name__ == '__main__':
    # print(sys.argv)
    Convert(sys.argv)
