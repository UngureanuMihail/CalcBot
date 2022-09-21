from csv_logger import CsvLogger
import logging

filename = 'log.csv'
delimiter = ','
level = logging.INFO
custom_additional_levels = ['logs_a']
fmt = f'%(asctime)s{delimiter}%(message)s'
datefmt = '%Y/%m/%d %H:%M:%S'
max_size = 1024  # 1 kilobyte
max_files = 4  # 4 rotating files
header = ['date', 'User_id', 'result']

# Creat logger with csv rotating handler
csvlogger = CsvLogger(filename=filename,
                          delimiter=delimiter,
                          level=level,
                          add_level_names=custom_additional_levels,
                          add_level_nums=None,
                          fmt=fmt,
                          datefmt=datefmt,
                          max_size=max_size,
                          max_files=max_files,
                          header=header)

def log(user_id,result):
    # Log some records
    csvlogger.logs_a([user_id, result])



