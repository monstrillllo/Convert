#How to use:

##Firstly you need to clone this repo

    git clone https://monstrillllo@bitbucket.org/coherentprojects/coherent-training-eugen-sapezhinsky.git
    
##Next go to the repo folder and install requirements

    cd coherent-training-eugen-sapezhinsky
    python3 -m pip install -r requirements.txt

##Now you can do it

    python3 convert.py [--csv2parqet | --parquet2csv <src-file-path> <new-file-path>] | [--get-schema <parquet-file-path>] | [--help]

#Usage example:

#input

    python3 convert.py --help

#output
        
    Usage: python3 convert.py [OPTIONS] PATH_TO_FILE NEW_FILE_PATH
    
    Convert csv to parquet or parquet to csv
    
    Options:
    
     --csv2parquet          convert file.csv to new_file.parquet
     --parquet2csv          convert file.parquet to new_file.csv
     --get-schema           return schema of the file.parquet
     --help                 return this message

