import unittest
import requests
import os, sys, time

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, parentdir)
sys.path.append("..")


class Search_CategoryList_test(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://eims.sit.datoubao.com/eims/category/queryCategoryList"

        # 获得类目接口

    def test_selectAllCategory_null(self):
        '''类目都不选点击查询'''

        payload = {'firstCategoryId': '', 'secondCategoryId': '', 'thirdCategoryId': '', 'currentPage': '',
                   'pageCount': ''}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)

    def test_onlyselectfirstCategory(self):
        '''只选择一级类目点击查询,后面二三类目默认不选,查询页码第一页，分页查询量9'''
        payload = {'firstCategoryId': '186', 'secondCategoryId': '49', 'thirdCategoryId': '208', 'currentPage': '1',
                   'pageCount': '9'}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], True)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)

    def test_onlyselectfirstCategory_wrongSecWrongThird(self):
        '''正确选择一级类目，错误的二级类目，错误的三级类目，'''
        payload = {'firstCategoryId': '186', 'secondCategoryId': '0', 'thirdCategoryId': '0', 'currentPage': '',
                   'pageCount': ''}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)

    def test_onlyselectfirstCategoryrightSecWrongThird(self):
        ''''正确的一级类目，该一级类目下的二级类目，错误的三级类目'''
        payload = {'firstCategoryId': '186', 'secondCategoryId': '49', 'thirdCategoryId': '0', 'currentPage': '',
                   'pageCount': ''}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)

    def test_onlyselectfirstCategorywrongSecWrongThird(self):
        '''正确的一级类目，不在该类目下的二级类目，错误的三级类目'''
        payload = {'firstCategoryId': '186', 'secondCategoryId': '59', 'thirdCategoryId': '#', 'currentPage': '',
                   'pageCount': ''}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)
    def test_onlyselectfirstCategorywrongSecRightThird(self):
        ''''正确的一级类目，不在该类目下的二级类目，在该一级类目下的三级类目'''
        payload = {'firstCategoryId': '186', 'secondCategoryId': '59', 'thirdCategoryId': '55', 'currentPage': '',
                   'pageCount': ''}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['result'], False)
        self.assertEqual(self.result['errorCode'], 0)
        self.assertEqual(self.result['message'], None)

        # 类目列表查询接口

    def tearDown(self):
        print(str(self.result))


if __name__ == '__main__':
    unittest.main()
