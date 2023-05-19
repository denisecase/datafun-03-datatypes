"""
Purpose: Set up logging once and reuse it.

Author: Denise Case

This file automatically records your work so you don't have to. 
Analysts and data scientists will work hard once, to be lazy later.
"""

import logging
import pathlib
import platform
import sys
import os
import datetime

def get_source_directory_path(current_file):
    """Returns the absolute path to this source directory."""
    dir = os.path.dirname(os.path.abspath(current_file))
    return dir

def setup_logger(current_file):
    '''Setup a logger to automatically log useful information.
      @param current_file: the name of the file reqesting a logger.
      @returns: the logger object and the name of the logfile.
    '''
    logs_dir = pathlib.Path("logs")
    logs_dir.mkdir(exist_ok=True)

    module_name = pathlib.Path(current_file).stem
    log_file_name = logs_dir.joinpath(module_name + ".log")

    logging.basicConfig(filename=log_file_name, filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s')
    logger = logging.getLogger(module_name)

    divider_string = "============================================================="
    python_version_string  = platform.python_version()
    today = datetime.date.today()

    logger.info(divider_string)
    logger.info(divider_string)
    logger.info(f"Today is {today} at {datetime.datetime.now().strftime('%I:%M %p')}")
    logger.info(f"This file is running on: {os.name} {platform.system()} {platform.release()}")
    logger.info(f"The Python version is: {python_version_string}")
    logger.info(f"The active conda environment is:  {os.environ.get('CONDA_DEFAULT_ENV') }")
    logger.info(f"The active pip environment is:    {os.environ.get('PIP_DEFAULT_ENV') }")
    logger.info(f"The active environment path is:   {sys.prefix}")
    logger.info(f"The current working directory is: {os.getcwd()}")
    logger.info(f"This source file is in:           {get_source_directory_path(current_file)}")
    logger.info(divider_string)
    logger.info(divider_string)

    return logger, log_file_name

if __name__ == "__main__":
    logger, logname = setup_logger(__file__)
    logger.info(f"Starting util_datafun_logger.py")
    logger.info(f"Information is logged to: logs/{logname}")
    logger.info(f"Ending util_datafun_logger.py")

    # Use built-in open() function to read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())

    