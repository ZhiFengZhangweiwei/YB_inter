import unittest
import requests
import os, sys,time
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, parentdir)
sys.path.append("..")


class Search_ChannelBySecondId_test(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://eims.sit.datoubao.com/channel/queryChannelBySecondId"

        #获得类目接口
    def test_getsecondCategory_null(self):
        '''二级渠道正确'''

        payload = {'channelSecondId':'1'}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'],0)
        self.assertEqual(self.result['message'],None)
        self.assertEqual(self.result['result'],True )



    def test_getsecondCategory_true(self):
        '''选择二级类目获得该级类目下的三级类目，'''

        payload = {'categoryId': '48', 'queryLevel': '3'}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'],0)
        self.assertEqual(self.result['message'], None)
        self.assertEqual(self.result['result'], True)


        #类目列表查询接口



    def tearDown(self):
         print(str(self.result))




if __name__=='__main__':

    unittest.main()