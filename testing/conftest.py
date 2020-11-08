#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from BaseFunction.caculator import Caculator

@pytest.fixture(scope ="module")
def get_calc():
    calc = Caculator()
    print("计算开始")
    yield calc
    print("计算结束")
