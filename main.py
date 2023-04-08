#!/usr/bin/env python3
# coding:utf-8

#
# Author: leoking
# Date: 2023-04-08 14:24:46
# LastEditTime: 2023-04-08 16:37:26
# LastEditors: leoking
# Description:
#
from typing import Union
from fastapi import FastAPI

from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper
from fastapi_sqlalchemy import (
    db,
)
from sqlalchemy import text  # an object to provide global access to a database session

from conf import DB_URL

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DB_URL, commit_on_exit=True)


@app.get("/ping")
async def read_root():
    return {"Hello": "World"}


@app.get("/test/db")
async def test_db():
    from models import TestModel

    db.session.execute(
        text(
            """
        create table if not exists test(
            id INTEGER PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """
        )
    )
    db.session.add(TestModel(name="xxxxxx"))
    return db.session.query(TestModel).all()
