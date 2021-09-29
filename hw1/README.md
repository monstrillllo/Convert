Convert.py

Convert csv file to parquet file or parquet to csv or show schema of the parquet file.

Install

    git clone https://monstrillllo@bitbucket.org/coherentprojects/coherent-training-eugen-sapezhinsky.git
    cd coherent-training-eugen-sapezhinsky
    python3 -m pip install -r requirements.txt
        

Usage
 
    python3 convert.py [OPTIONS] PATH_TO_FILE NEW_FILE_PATH
    
    Convert csv to parquet or parquet to csv
    
    Options:
    
     --csv2parquet          convert file.csv to new_file.parquet
     --parquet2csv          convert file.parquet to new_file.csv
     --get-schema           return schema of the file.parquet
     --help                 return this message

Example

    python3 convert.py --csv2parquet ./my_files/file.csv ./my_files/file.parquet

    python3 convert.py --get-schema ./my_files/file.parquet

