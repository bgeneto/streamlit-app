#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""Experimento do Prof. Mauro."""

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


class Experiment:
    def __init__(self, sensors: int, pps: int) -> None:
        # number of sensors
        self.sensors = sensors
        # read points per sensor
        self.pps = pps
        self.pts = self.sensors * self.pps


def initial_sidebar_config():
    # sidebar contents
    sidebar = st.sidebar
    sidebar.subheader("..:: MENU ::..")


def reshapedf(ini: int, df: pd.DataFrame) -> None:
    # crop the beginning of data
    df = df[ini:]

    # crop the end of data
    nlen = len(df) - len(df) % exp.pts
    df = df[:nlen]

    # reshape dataframe
    df = pd.DataFrame((df.values.reshape(exp.pts, -1)))

    # print all data  
    #st.write(df)

    # split data by sensors
    split_sensors(df)


def split_sensors(df: pd.DataFrame) -> None:
    # split sensors data in the middle point (not average)
    ndf = pd.DataFrame()
    pos = 10; i = 0
    while pos < len(df):
        i += 1
        sr = df.iloc[pos-1].rename(f"sensor {i}")
        ndf = pd.concat([ndf, sr], axis=1)
        pos = pos + exp.pps

    st.write(ndf)
    # plot sensors 
    fig = px.line(ndf)
    st.plotly_chart(fig, use_container_width=True)


def main():
    # record start time
    start = timer()

    # config sidebar
    #sidebar = initial_sidebar_config()

    # upload and read csv file
    st.write("## 1. Upload your CSV file")
    uploaded_file = st.file_uploader(
        "Choose a CSV file below:", 
        type=['csv'],
        accept_multiple_files=False)

    df = None
    # check if file was uploaded
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file, delimiter=',',
                             skiprows=1, usecols=[1])
            st.success(
                ":white_check_mark: File uploaded and read with success!")
        except Exception as e:
            st.exception(e)
            stop()

        # plot whole file
        fig = px.line(df)
        st.plotly_chart(fig, use_container_width=True)

        # choose the initial point
        st.write("## 2. Initial point")
        help_txt = "Tip: zoom in the graphic above to better " \
                   "choose your initial point."
        ini = 0
        ini = st.number_input('Choose the initial (index) point by inspecting the figure above', format="%d", min_value=0,
                              help=help_txt,
                              on_change=reshapedf,
                              args=(ini, df,),
                              key=ini)

        reshapedf(ini, df)

    # copyright, version and running time info
    end = timer()
    st.caption(
        f":copyright: 2022 bgeneto | Version: {__version__} | Execution: {(end-start):.2f}s")


if __name__ == '__main__':
    # always run as a streamlit app
    force_streamlit = True

    # page title/header
    title = "Experiment :pencil: Prof. Mauro"

    # experiment data
    exp = Experiment(sensors=8, pps=20)

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

