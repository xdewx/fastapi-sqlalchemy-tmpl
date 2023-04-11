#!/usr/bin/env python3
# coding:utf-8

#
# Author: leoking
# Date: 2023-04-12 01:48:31
# LastEditTime: 2023-04-12 01:56:52
# LastEditors: leoking
# Description:
#
from fastapi import APIRouter
from fastapi_sqlalchemy import (
    db,
)
from sqlalchemy import text

from models import TestTable  # an object to provide global access to a database session

router = APIRouter()


@router.get("/ping")
async def read_root():
    return {"Hello": "World"}


@router.get("/db/write")
async def test_db():
    from models import TestTable

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
    db.session.add(TestTable(name="xxxxxx"))
    return db.session.query(TestTable).all()


@router.get("/db/read/1")
async def read(id: int):
    item = db.session.query(TestTable).get(id)
    return item


@router.get("/db/read/failed")
def read_failed(id: int):
    item = db.session.query(TestTable).get(id)
    return item


@router.get("/db/read/3")
def read_2(id: int):
    with db():
        item = db.session.query(TestTable).get(id)
    return item


@router.get("/db/read/4")
def read_3(id: int):
    item = db.session.query(TestTable).get(id)
    db.session.close()
    return item
