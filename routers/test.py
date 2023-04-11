#!/usr/bin/env python3
# coding:utf-8

#
# Author: leoking
# Date: 2023-04-12 01:48:31
# LastEditTime: 2023-04-12 01:49:36
# LastEditors: leoking
# Description:
#
from fastapi import APIRouter
from fastapi_sqlalchemy import (
    db,
)
from sqlalchemy import text  # an object to provide global access to a database session

router = APIRouter()


@router.get("/ping")
async def read_root():
    return {"Hello": "World"}


@router.get("/test/db")
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
