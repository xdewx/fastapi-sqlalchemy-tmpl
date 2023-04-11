#!/usr/bin/env python3
# coding:utf-8

#
# Author: leoking
# Date: 2023-04-08 14:24:46
# LastEditTime: 2023-04-12 01:51:09
# LastEditors: leoking
# Description:
#
from fastapi import FastAPI

from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper

from conf import DB_URL

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DB_URL, commit_on_exit=True)

from routers import test

app.include_router(test.router, prefix="/test", tags=['test'])

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", default=False)
    args = parser.parse_args()

    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=args.debug)
