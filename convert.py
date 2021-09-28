import argparse
import sys

import pandas as pd
import pyarrow
import pyarrow.parquet


class Convert:
    def __init__(self, args: list) -> None:
        self.args = args
        self.read_args()

    def read_args(self):
        parser = argparse.ArgumentParser('Convert csv to parquet or parquet to csv')
        parser.add_argument('--csv2parquet', help='convert csv to parquet', type=str, metavar='PATH', nargs=2)
        parser.add_argument('--parquet2csv', help='convert parquet to csv', type=str, metavar='PATH', nargs=2)
        parser.add_argument('--schema', help='return schema of the file.parquet', type=str, metavar='PATH', nargs=1)
        args = parser.parse_args()
        if args.csv2parquet:
            self.csv_to_parquet(args.csv2parquet[0], args.csv2parquet[1])
        elif args.parquet2csv:
            self.parquet_to_csv(args.parquet2csv[0], args.parquet2csv[1])
        elif args.schema:
            self.get_schema(args.schema[0])

    def csv_to_parquet(self, src_path, dst_path):
        try:
            parquet = pd.read_csv(src_path)
            parquet.to_parquet(dst_path)
            print('Done!')
        except Exception as ex:
            print(ex)

    def parquet_to_csv(self, src_path, dst_path):
        try:
            csv_ = pd.read_parquet(src_path, engine='pyarrow')
            csv_.to_csv(dst_path, index=False)
            print('Done!')
        except Exception as ex:
            print(ex)

    def get_schema(self, path):
        try:
            parquet_file = pyarrow.parquet.read_schema(path)
            print(parquet_file)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    # print(sys.argv)
    Convert(sys.argv)
