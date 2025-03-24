# JavaScript 动态渲染页面爬取

## Selenium

`pip install selenium`  [_](https://setup.scrape.center/selenium) [chromedriver](https://setup.scrape.center/chromedriver) 

- demo1 ：登录百度搜索Python

- demo2：获取网页源码

- demo3：查找节点，单、多节点

- demo4：节点交互 更多节点操作 [参考](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement) 

- demo5：动作链 更多动作链操作 [参考](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains) 

- demo6：模拟运行JS

- demo7：获取属性、文本值、id、location、tag_name、size

- demo8：切换Frame

  - **处理嵌套内容**：当页面中存在 `<iframe>`（内联框架）时，其内容与主页面是独立的 HTML 文档。直接查找 iframe 内的元素会失败，必须**先切换到目标 iframe 的上下文**，才能操作其中的元素。
  - **参数含义**：`'iframeResult'` 通常是目标 iframe 的 **`id` 或 `name` 属性值**。Selenium 通过此标识定位 iframe。
  - **切换回主页面/父级框架**

    - **返回主页面**：`browser.switch_to.default_content()`
    - **返回父级框架**（如果有多层嵌套）：`browser.switch_to.parent_frame()` 
  - 其他定位 iframe 的方式

    如果 iframe 没有 `id` 或 `name`，可以通过以下方式切换：

    1. **索引**（从 0 开始）：

       ```
    browser.switch_to.frame(0)  # 切换至第一个 iframe
       ```

    2. **通过 WebElement 定位**：
    
        ```
       iframe = browser.find_element(By.CSS_SELECTOR, "iframe.some-class")
       browser.switch_to.frame(iframe)
	
- demo9：隐式等待、显示等待。更多等待条件 [参考](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions) 

  | 等待条件                                     | 含义                                                |
  | -------------------------------------------- | --------------------------------------------------- |
  | title_is                                     | 标题是某内容                                        |
  | title_contains                               | 标题包含某内容                                      |
  | presence_of_element_located                  | 节点加载出，传入定位元组，如 (By.ID, 'p')           |
  | visibility_of_element_located                | 节点可见，传入定位元组                              |
  | visibility_of                                | 可见，传入节点对象                                  |
  | presence_of_all_elements_located             | 所有节点加载出                                      |
  | text_to_be_present_in_element                | 某个节点文本包含某文字                              |
  | text_to_be_present_in_element_value          | 某个节点值包含某文字                                |
  | frame_to_be_available_and_switch_to_it frame | 加载并切换                                          |
  | invisibility_of_element_located              | 节点不可见                                          |
  | element_to_be_clickable                      | 节点可点击                                          |
  | staleness_of                                 | 判断一个节点是否仍在 DOM，可判断页面是否已经刷新    |
  | element_to_be_selected                       | 节点可选择，传节点对象                              |
  | element_located_to_be_selected               | 节点可选择，传入定位元组                            |
  | element_selection_state_to_be                | 传入节点对象以及状态，相等返回 True，否则返回 False |
  | element_located_selection_state_to_be        | 传入定位元组以及状态，相等返回 True，否则返回 False |
  | alert_is_present                             | 是否出现 Alert                                      |

- demo10：网页前进、后退

- demo11：对cookie操作。

- demo12：选项卡管理

- demo13：处理异常。更多 [参考](https://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions) 

- demo14：禁止爬虫

- demo15：反爬。原因 `window.navigator` 包含了 `webdriver` 属性，正常浏览器该属性为 `undefined` 

- demo16：无头模式。在网站运行时不会弹出窗口。
