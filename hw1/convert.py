import argparse
import pandas as pd
import pyarrow
import pyarrow.parquet


def read_args():
    """
    Parse command line params and depending on result call functions

    Return
    ------
    None
    """
    parser = argparse.ArgumentParser('Convert csv to parquet or parquet to csv')
    parser.add_argument('--csv2parquet', help='convert csv to parquet', type=str, metavar='PATH', nargs=2)
    parser.add_argument('--parquet2csv', help='convert parquet to csv', type=str, metavar='PATH', nargs=2)
    parser.add_argument('--schema', help='return schema of the file.parquet', type=str, metavar='PATH', nargs=1)
    args = parser.parse_args()
    if args.csv2parquet:
        convert_csv_to_parquet(args.csv2parquet[0], args.csv2parquet[1])
    elif args.parquet2csv:
        convert_parquet_to_csv(args.parquet2csv[0], args.parquet2csv[1])
    elif args.schema:
        print(get_schema(args.schema[0]))


def convert_csv_to_parquet(src_path: str, dst_path: str) -> None:
    """
    Convert source csv file to destination parquet file

    Parameters
    ----------
    src_path: str, required
        path to source file
    dst_path: str, required
        path to destination file

    Return
    ------
    None
    """

    try:
        parquet = pd.read_csv(src_path)
        parquet.to_parquet(dst_path)
        print('Done!')
    except Exception as ex:
        print(ex)


def convert_parquet_to_csv(src_path: str, dst_path: str) -> None:
    """
    Convert source parquet file to destination csv file

    Parameters
    ----------
    src_path: str, required
        path to source file
    dst_path: str, required
        path to destination file

    Return
    ------
    None
    """
    try:
        csv_ = pd.read_parquet(src_path, engine='pyarrow')
        csv_.to_csv(dst_path, index=False)
        print('Done!')
    except Exception as ex:
        print(ex)


def get_schema(path: str) -> pyarrow.Schema:
    """
    Convert source parquet file to destination csv file

    Parameters
    ----------
    path: str, required
        path to file

    Return
    ------
    None
    """
    try:
        return pyarrow.parquet.read_schema(path)
    except Exception as ex:
        print(ex)


def main():
    read_args()


if __name__ == '__main__':
    main()
