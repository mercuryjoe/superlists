'''
功能测试文档
使用unittest模块扩展功能测试
使用Edge作用测试的主要浏览器。Firefox与Chrome暂不作测试
'''

import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    # MSEdgeDriver 调用
    driver_edge = webdriver.Edge(executable_path=r"C:\MSEdgeDriver\msedgedriver.exe")

    def tearDown(self):
        self.driver_edge.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她云看了这个应用的首页
        # Edge
        # self.edgedriver_path = r"C:\MSEdgeDriver\msedgedriver.exe"
        # self.browser_edge = webdriver.Edge(executable_path=self.edgedriver_path)
        self.driver_edge.get('http://localhost:8000')

        # 她注意到网页的标题和头部包含 “To-Do”这个司
        self.assertIn('To-Do', self.driver_edge.title)
        self.fail('Finish the test!')

        # 应用邀请她输入一个待办事项

        # 她在一个文本框中输入了 “Buy peacock feathers ” (购买孔雀羽毛)
        # 伊迪丝的爱好是使用假蝇做饵钓鱼

        # 她按回画键后、页面更新了
        # 待办事项表格中显示了 “1: Buy peacock feathers”

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 她输入了“Use peacock feathers to make a fly”(使用孔雀羽毛做假蝇)
        # 伊迪丝做事很有条理

        # 页面再次更新，她的清单中显示了这两个待办事项

        # 伊迪丝想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 她访问那个URL，发现她的待办事项列表还在

        # 她很满意，去睡觉了


if __name__ == '__main__':
    unittest.main(warnings='ignore')
