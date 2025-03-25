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

## Splash

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;是一个JA渲染服务，含有HTTP API的轻量级浏览器，对接了Py的Twisted、QT库。用Splash同样可以爬取动态渲染的页面。Splash 的 [API](https://splash.readthedocs.io/en/stable/scripting-ref.html) 操作官方文档， 针对网页元素的 [API](https://splash.readthedocs.io/en/stable/scripting-element-object.html) 操作

安装 [官方文档](https://splash-cn-doc.readthedocs.io/zh-cn/latest/Installation.html)  [_](https://setup.scrape.center/splash)  

- demo1：传入JS脚本
- demo2：返回字典、str
- demo3：异步处理 [基础语法](https://www.runoob.com/lua/lua-basic-syntax.html) 

splash对象的属性

- demo4：args：用于获取页面加载时配置的参数
- demo5：js_enabled：JavaScript 是否开启
- demo6：resource_timeout：页面加载超时时间，`0`、`nil` 代表不设置。
- demo7：images_enabled：是否加载图片
- demo8：plugins_enabled：是否开启浏览器插件
- demo9：scroll_position：控制页面上下或作用滚动。

splash 对象的方法

- demo10：go：请求某个链接，而且它可以模拟 GET 和 POST 请求，同时支持传入请求头、表单等数据
  方法返回OK变量和reason变量的组合。ok为空，页面加载出错，reason返回错误原因。否则代表页面加载成功。

  ```lua
  ok, reason = splash:go{url, baseurl=nil, headers=nil, http_method="GET", body=nil, formdata=nil}
  ```

  - url：请求url
  - baseurl：资源加载的相对路径
  - headers：请求头
  - http_method：请求方法。默认GET，支持POST
  - body：http_methed为POST时的表单数据，使用的 `Content-type` 为 `application/json` 
  - fordata：http_methed为POST时的表单数据，使用的 `Content-type` 为 `application/x-www-form-urlencoded`  

- demo11：wait：控制页面等待时间

  ```lua
  ok, reason = splash:wait{time, cancel_on_redirect=false, cancel_on_error=true}
  ```

  - time，等待的秒数。
  - cancel_on_redirect，可选参数，默认 False，如果发生了重定向就停止等待，并返回重定向结果。
  - cancel_on_error，可选参数，默认 False，如果发生了加载错误就停止等待。

- demo12：jsfunc：直接调用 JavaScript 定义的方法，但是所调用的方法需要用双中括号包围，这相当于实现了 JavaScript 方法到 Lua 脚本的转换。关于 JavaScript 到 Lua 脚本的更多转换细节 [参考](https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-jsfunc) 

- demo13：evaljs：方法可以执行 JavaScript 代码并返回最后一条 JavaScript 语句的返回结果

- demo14：runjs：执行 JavaScript 代码，它与 evaljs 方法的功能类似，但是更偏向于执行某些动作或声明某些方法。

- demo15：autoload：可以设置每个页面访问时自动加载的对象.

  只负责加载 JavaScript 代码或库，不执行任何操作。如果要执行操作，可以调用 evaljs 或 runjs 方法。

  `ok, reason = splash:autoload{source_or_url, source=nil, url=nil}` 

  - source_or_url，JavaScript 代码或者 JavaScript 库链接。
  - source，JavaScript 代码。
  - url，JavaScript 库链接

- demo16：call_later：可以通过设置定时任务和延迟时间来实现任务延时执行，并且可以在执行前通过 cancel 方法重新执行定时任务。

- demo17：http_get：可以模拟发送 HTTP 的 GET 请求

  ```lua
  response = splash:http_get{url, headers=nil, follow_redirects=true}
  ```

  - url，请求 URL。
  - headers，可选参数，默认为空，请求的 Headers。
  - follow_redirects，可选参数，默认为 True，是否启动自动重定向。

- demo18：http_post：方法是模拟发送一个 POST 请求，不过多了一个参数 body

  ```lua
  response = splash:http_post{url, headers=nil, follow_redirects=true, body=nil}
  ```

  - url，请求 URL。
  - headers，可选参数，默认为空，请求的 Headers。
  - follow_redirects，可选参数，默认为 True，是否启动自动重定向。
  - body，可选参数，默认为空，即表单数据。

- demo19：set_content：方法可以用来设置页面的内容

- demo20：html：方法可以用来获取网页的源代码

- demo21：png：方法可以用来获取 PNG 格式的网页截图
  jpeg：方法可以用来获取 JPEG 格式的网页截图

- demo22：har：方法可以用来获取页面加载过程描述

- demo23：url：此方法可以获取当前正在访问的 URL

- demo24：get_cookies：此方法可以获取当前页面的 Cookies

- demo25：add_cookie：此方法可以为当前页面添加 Cookies

  `cookies = splash:add_cookie{name, value, path=nil, domain=nil, expires=nil, httpOnly=nil, secure=nil}` 

- demo26：clear_cookies：此方法可以清除所有的 Cookies

- demo27：get_viewport_size：此方法可以获取当前浏览器页面的大小，即宽高

- demo28：set_viewport_size：此方法可以设置当前浏览器页面的大小，即宽高

  ```lua
  splash:set_viewport_size(width, height)
  ```

- demo29：set_viewport_full：方法可以设置浏览器全屏显示

- demo30：set_user_agent：方法可以设置浏览器的 User-Agent

- demo31:set_custom_headers()：此方法可以设置请求的 Headers

- demo32：select：方法可以选中符合条件的第一个节点，如果有多个节点符合条件，则只会返回一个，其参数是 CSS 选择器

- demo33：select_all()：此方法可以选中所有的符合条件的节点，其参数是 CSS 选择器。

- demo34：mouse_click：此方法可以模拟鼠标点击操作，传入的参数为坐标值 x、y，也可以直接选中某个节点直接调用此方法。

Splash API 调用

- demo1：render.html：此接口用于获取 JavaScript 渲染的页面的 HTML 代码，接口地址就是 Splash 的运行地址加此接口名称

  如`http://localhost:8050/render.html`。

  ```shell
  curl http://localhost:8050/render.html?url=https://www.baidu.com
  ```

  给此接口传递了一个 url 参数指定渲染的 URL，返回结果即页面渲染后的源代码。

  此接口还可以指定其他参数，比如通过 wait 指定等待秒数。如果要确保页面完全加载出来，可以增加等待时间。参数[参考文档](https://splash.readthedocs.io/en/stable/api.html#render-html) 

- demo2：render.png：接口可以获取网页截图，其参数比 render.html 多了几个，比如通过 width 和 height 来控制宽高，它返回的是 PNG 格式的图片二进制数据。

  ```shell
  curl http://localhost:8050/render.png?url=https://www.taobao.com&wait=5&width=1000&height=700
  ```
  
  参数设置[文档](https://splash.readthedocs.io/en/stable/api.html#render-png) 
  
- demo3：render.jpeg：它返回的是 JPEG 格式的图片二进制数据。此接口相比 render.png 还多了一个参数 quality，可以用来设置图片质量。

- demo4：render.har：此接口用于获取页面加载的 HAR 数据

  ```shell
  curl http://localhost:8050/render.har?url=https://www.jd.com&wait=5
  ```

  返回结果非常多，是一个 Json 格式的数据，里面包含了页面加载过程中的 HAR 数据。

  

- demo5：render.json：此接口包含了前面接口的所有功能，返回结果是 Json 格式

  ```shell
  curl http://localhost:8050/render.json?url=https://httpbin.org
  ```

  这里以 JSON 形式返回了相应的请求数据

  我们可以通过传入不同参数控制其返回结果。比如，传入 html=1，返回结果即会增加源代码数据；传入 png=1，返回结果即会增加页面 PNG 截图数据；传入 har=1，则会获得页面 HAR 数据。例如：

  ```
  curl http://localhost:8050/render.json?url=https://httpbin.org&html=1&har=1
  ```

  这样返回的 Json 结果便会包含网页源代码和 HAR 数据。

  参考[文档](https://splash.readthedocs.io/en/stable/api.html#render-json) 

- demo6：execute：实现一些交互操作

  此接口才是最为强大的接口。前面说了很多 Splash Lua 脚本的操作，用此接口便可实现与 Lua 脚本的对接。

  ```
  function main(splash)
      return 'hello'
  end
  ```

  然后将此脚本转化为 URL 编码后的字符串，拼接到 execute 接口后面，示例如下：

  ```
  curl http://localhost:8050/execute?lua_source=function+main%28splash%29%0D%0A++return+%27hello%27%0D%0Aend
  ```

  运行结果：

  ```
  hello
  ```

  这里我们通过 lua_source 参数传递了转码后的 Lua 脚本，通过 execute 接口获取了最终脚本的执行结果。

### 负载均衡配置

  配置[网站](https://setup.scrape.center/splash-cluster) 

  

  



