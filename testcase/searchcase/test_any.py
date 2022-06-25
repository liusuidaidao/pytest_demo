import re

import pytest
import requests
import allure_pytest

class TestCLASS():
    sesson=requests.session()
    @pytest.mark.run(order=2)
    def test_defc(self):
        print('TestCLASS.num',TestCLASS.sesson)
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_defa(self):
        TestCLASS.num=1
    @pytest.mark.run(order=3)
    def test_defb(self):
        print('TestCLASS.num',TestCLASS.num)

    @pytest.mark.run(order=4)
    def test_get_html(self):
        url="http://47.107.116.139/phpwind/"
        rep=requests.get(url=url)
        #print(rep.text)
        csrf_token=re.search('name="csrf_token" value="(.*?)"',rep.text)
        print('csrf_token=',csrf_token)
        #print('csrf_token1=', csrf_token[1])
pytest.main()

