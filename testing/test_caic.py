#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml


def get_datas():
    with open("datas/caic.ymal", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data


class TestCalc:
    # def setup(self):
    #     print("计算开始")
    #     self.calc = Calculator()
    #
    # def teardown(self):
    #     print("计算结束")

    @pt_test.mark.run(order = 2)
    @pt_test.mark.parametrize('a,b,expect', get_datas()['add']['data'], ids = get_datas()['add']['ids'])
    def test_add(self, get_calc,a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect

    @pt_test.mark.run(order = 1)
    @pt_test.mark.parametrize('a,b,expect', get_datas()['div']['data'], ids = get_datas()['div']['ids'])
    def test_div(self,get_calc,a,b,expect):
        if b == 0:
            try:
                get_calc.div(a, b)
            except ZeroDivisionError as e:
                print("除数不能为0")
        else:
            result = get_calc.div(a, b)
            assert result == expect