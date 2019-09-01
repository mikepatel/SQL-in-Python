"""
Michael Patel
September 2019

File description:
    Test script to try out ideas with SQL, Pandas, and Python

Tutorial resource:
    https://towardsdatascience.com/sql-in-python-for-beginners-b9a4f9293ecf

"""
################################################################################
# Imports
import pandas as pd
from sqlalchemy import create_engine

################################################################################
# Main
if __name__ == "__main__":
    # create SQL engine
    engine = create_engine()