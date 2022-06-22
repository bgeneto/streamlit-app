#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""main.py streamlit page"""

import itertools
import math
import os
import pickle
import sys
import uuid
from datetime import datetime, timedelta
from multiprocessing import Pool
from pathlib import Path
from timeit import default_timer as timer
from types import SimpleNamespace
from typing import Callable

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from joblib import Parallel, delayed, parallel_backend
from plotly.subplots import make_subplots
from scipy import optimize, stats
from sklearn.linear_model import LinearRegression

import streamlit as st

__author__ = "Bernhard Enders"
__maintainer__ = "Bernhard Enders"
__email__ = "b g e n e t o @ g m a i l d o t c o m"
__copyright__ = "Copyright 2022, Bernhard Enders"
__license__ = "GPL"
__version__ = "1.0.0"
__status__ = "Development"
__date__ = "20220621"


def stop(code=0):
    """Stop code execution"""
    if st._is_running_with_streamlit:
        st.stop()
    sys.exit(code)


def filename_only(fn):
    """Returns the filename without path and (the last) file extension.
    Args:
        fn: fullpath to file.
    Returns:
        The filename fn without both path and the last extension.
    """
    return os.path.splitext(os.path.basename(fn))[0]


def st_layout(title: str = "Streamlit App") -> None:
    """Configure Streamlit page layout"""

    st.set_page_config(
        page_title=title.split('-')[0],
        page_icon=":pencil:",
        layout="centered")
    st.title(title)

    
def initial_sidebar_config():
    # sidebar contents
    sidebar = st.sidebar
    sidebar.subheader("..:: MENU ::..")

    
def main():
    # record start time
    start = timer()

    # config sidebar
    sidebar = initial_sidebar_config()

    st.write("# Hello World!")

    # copyright, version and running time info
    end = timer()
    st.caption(
        f":copyright: 2022 bgeneto | Version: {__version__} | Execution: {(end-start):.2f}s")


if __name__ == '__main__':
    # always run as a streamlit app
    force_streamlit = True

    # page title/header
    title = "Page Title Here"

    # increase pandas default output precision from 6 decimal places to 7
    pd.set_option("display.precision", 7)

    # check if running as standalone python script or via streamlit
    if st._is_running_with_streamlit:
        st_layout(title)
        main()
    else:
        if force_streamlit:
            st_layout(title)
            from streamlit import cli as stcli
            sys.argv = ["streamlit", "run", sys.argv[0]]
            sys.exit(stcli.main())
        else:
            main()

