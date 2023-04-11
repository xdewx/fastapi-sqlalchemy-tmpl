#!/usr/bin/env python3
# coding:utf-8

#
# Author: leoking
# Date: 2023-04-08 16:01:35
# LastEditTime: 2023-04-12 01:50:42
# LastEditors: leoking
# Description:
#
from typing import Optional
from pydantic import BaseModel

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class TestTable(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String(16))
