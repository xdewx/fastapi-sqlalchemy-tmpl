#!/bin/bash

###
 # @Author: leoking
 # @Date: 2023-04-08 14:23:54
 # @LastEditTime: 2023-04-08 16:03:08
 # @LastEditors: leoking
 # @Description: 
### 

ENV_NAME="fastapi"

conda create -n $ENV_NAME python=3.10 && \
    conda activate $ENV_NAME && \
    pip install fastapi "uvicorn[standard]" fastapi-sqlalchemy
