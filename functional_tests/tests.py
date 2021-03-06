'''
功能测试文档
使用unittest模块扩展功能测试
使用Edge作用测试的主要浏览器。
'''

import time
# import unittest

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# class NewVisitorTest(unittest.TestCase):
class NewVisitorTest(LiveServerTestCase):

    e_path = r"C:\MSEdgeDriver\msedgedriver.exe"
    driver = webdriver.Edge(executable_path=e_path)

    def tearDown(self):
        self.driver.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.driver.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她云看了这个应用的首页
        # self.driver.get('http://mydjango.com')
        self.driver.get(self.live_server_url)

        # 她注意到网页的标题和头部包含 “To-Do”这个司
        self.assertIn('To-Do', self.driver.title)
        header_text = self.driver.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请她输入一个待办事项
        inputbox = self.driver.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')
        # 她在一个文本框中输入了 “Buy peacock feathers ” (购买孔雀羽毛)
        # 伊迪丝的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车键后、页面更新了
        # 待办事项表格中显示了 “1: Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 她输入了“Use peacock feathers to make a fly”(使用孔雀羽毛做假蝇)
        # 伊迪丝做事很有条理
        inputbox = self.driver.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        # self.assertIn('2: Use peacock feathers to make a fly',
        #               [row.text for row in rows])

        # 页面再次更新，她的清单中显示了这两个待办事项
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 伊迪丝想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能
        self.fail('Finish the test!')

        # 她访问那个URL，发现她的待办事项列表还在

        # 她很满意，去睡觉了


# if __name__ == '__main__':
#    unittest.main(warnings='ignore')
