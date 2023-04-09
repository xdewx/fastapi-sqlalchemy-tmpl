#!/usr/bin/env python3
# coding:utf-8

#
# Author: leoking
# Date: 2023-04-08 15:56:29
#LastEditTime: 2023-04-10 00:49:55
#LastEditors: leoking
# Description:
#

from pathlib import Path

DIR4DATA = Path(__file__).parent.parent.joinpath("data")

DIR4DATA.mkdir(exist_ok=True, parents=True)

DB_URL = f"sqlite:///{DIR4DATA.as_posix()}/db.sqlite3"

print(DB_URL)
