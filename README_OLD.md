# Spider

## 第3章

### xpath

 安装 `pip install lxml`  [_](https://setup.scrape.center/lxml) 

| 表达式    | 描述                     |
| --------- | ------------------------ |
| nodename  | 选取此节点的所有子节点   |
| /         | 从当前节点选取直接子节点 |
| //        | 从当前节点选取子孙节点   |
| .         | 选取当前节点             |
| ..        | 选取当前节点的父节点     |
| parent::* | 选取当前节点的父节点     |
| @         | 选取属性                 |



- xpath_demo1: `etree` 构造 xpath 对象
- xpath_demo2: `etree` 读取html文件构造 xpath 对象
- xpath_demo3：获取 html 对象下的元素
- xpath_demo4：获取 html 对象的直接子节点 `(/)` 以及所有子孙节点 `(//)` 
- xpath_demo5：获取父节点元素 `/..` 或者 `/parent::*` 
- xpath_demo6：通过属性 `(@)` 取标签
- xpath_demo7：获取标签文本内容
- xpath_demo8：通过 `@` 获取属性值
- xpath_demo9：当属性含有多值时，使用contains
- xpath_demo10：多属性匹配，含有class、name等，匹配多属性可以筛除一部分标签
- xpath_demo11：按序选择想获取的标签


xpath的运算符

| 运算符 |      描述      |       实例        |                          返回值                           |
| :----: | :------------: | :---------------: | :-------------------------------------------------------: |
|   or   |       或       | age=19 or age=20  |    如果age是19，返回true。如果 age 是 21，则返回 false    |
|  and   |       与       | age>19 and age<21 |   如果 age是20，则返回 true。如果 age是18，则返回 false   |
|  mod   | 计算除法的余数 |      5 mod 2      |                             1                             |
|   \|   | 计算两个节点集 |   //book\|//cd    |             返回所有拥有book和cd元素的节点集              |
|   +    |      加法      |       6 + 4       |                            10                             |
|   -    |      减法      |       6 - 4       |                             2                             |
|   *    |      乘法      |       6 * 4       |                            24                             |
|  div   |      除法      |      8 div 4      |                             2                             |
|   =    |      等于      |      age=19       | 如果 age 是 19，则返回 true。如果 age 是 20，则返回 false |
|   !=   |     不等于     |      age!=19      | 如果 age 是 18，则返回 true。如果 age 是 19，则返回 false |
|   <    |      小于      |      age<19       | 如果 age 是 18，则返回 true。如果 age 是 19，则返回 false |
|   <=   |   小于或等于   |      age<=19      | 如果 age 是 19，则返回 true。如果 age 是 20，则返回 false |
|   >    |      大于      |      age>19       | 如果 age 是 20，则返回 true。如果 age 是 19，则返回 false |
|   >=   |   大于或等于   |      age>=19      | 如果 age 是 19，则返回 true。如果 age 是 18，则返回 false |
- xpath_demo12：节点轴获取子元素、兄弟元素、父元素、祖先元素等

| 节点轴            | 描述         |
| ----------------- | ------------ |
| ancestor          | 祖先节点     |
| attribute         | 节点属性     |
| child             | 直接孩子节点 |
| descendant        | 子孙节点     |
| following         | 之后节点     |
| following-sibling | 兄弟节点     |



### Beautiful Soup

bs解析时依赖解析器，除了py标准库中的html还支持第三方解析器

安装 `pip install bs4` [_](https://setup.scrape.center/beautifulsoup) 

| 解析器          | 使用方法                             | 优势                                                         | 劣势                   |
| --------------- | ------------------------------------ | ------------------------------------------------------------ | ---------------------- |
| Python标准库    | BeautifulSoup(markup, 'html.parser') | Python内置标准库、执行速度适中、文档容错能力强               | /                      |
| LXML HTML解析器 | BeautifulSoup(markup, 'lxml')        | 速度快、文档容错能力强                                       | 需要安装C语言库        |
| LXML XML 解析器 | BeautifulSoup(markup, 'xml')         | 速度快、唯一支持XML的解析器                                  | 需要安装C语言库        |
| html5lib        | BeautifulSoup(markup, 'html5lib')    | 提供最好的容错性、以浏览器的方式解析文档、生成HTML5格式的文档 | 速度慢、不依赖外部扩展 |

- bs_demo1：通过 `bs.标签.string` 获取标签的文本
- bs_demo2：`prettify()` 格式化输出
- bs_demo3：输出标签、标签文本、节点名称、节点属性、属性值

| 属性           | 作用                    |
| -------------- | ----------------------- |
| .string        | 获取文本                |
| .name          | 获取节点名称            |
| .attrs         | 获取节点所有属性        |
| .attrs['name'] | 获取属性为name的属性值  |
| soup.p['name'] | 获取p属性为name的属性值 |




- bs_demo4：`bs4.element.Tag.Tag` 嵌套调用

- bs_demo5：关联选择

  | 节点轴      | 描述           |
  | ----------- | -------------- |
  | contents    | 直接子节点列表 |
  | children    | 返回生成器对象 |
  | descendants | 所有子孙节点   |

- bs_demo6：关联选择

  | 节点轴            | 描述                   |
  | ----------------- | ---------------------- |
  | parent            | 直接父节点             |
  | parents           | 祖先节点，生成器       |
  | next_sibling      | 获取下一个兄弟节点     |
  | previous_sibling  | 获取前一个兄弟节点     |
  | next_siblings     | 获取后面的所有兄弟节点 |
  | previous_siblings | 获取前面的所有兄弟节点 |
  
- bs_demo7：`attrs['class']` 获取class的属性值

- bs_demo8：方法选择器、通过 `name` 查询、通过 `attrs` 查询，常用属性也可以不用attrs，直接 `find_all(class_='elements')` 查询class为 `elements` 的元素 。
  现在使用 `string` (之前使用 `text` )

  | API                                                | 描述                                                         |
  | -------------------------------------------------- | ------------------------------------------------------------ |
  | find_all(name, attrs, recursive, string, **kwargs) | 查询所有符合条件的元素                                       |
  | find(name, attrs, recursive, string, **kwargs)     | 返回第一个符合条件的元素                                     |
  | find_parents 和 find_parent                        | 前者：所有祖先节点、后者：直接父节点                         |
  | find_next_siblings 和 find_next_sibling            | 前者：后面所有兄弟节点、后者：后面第一个兄弟节点             |
  | find_previous_siblings 和 find_previous_sibling    | 前者：前面所有兄弟节点、后者：前面第一个兄弟节点             |
  | find_all_next 和 find_next                         | 前者：节点后面所有符合条件的节点、后者：后面第一个符合条件的节点 |

- bs_demo9：css选择器

  `soup.select('tag | .class | #id')`  可以选择 标签、class、id 如 `soup.select('#list-2 .element')` 选用id为list-2下class为element的标签

  直接获取属性、attrs获取属性

  获取文本值 `.select('li').get_text()`
  
### pyquery

[参考pyquery](http://pyquery.readthedocs.io)

安装 `pip install pyquery` [_](https://setup.scrape.center/pyquery) 

- pq_demo1：打印文本、爬取网站获取标签、也可以传入文件

- pq_demo2：CSS选择器

- pq_demo3：通过 `find` 查标签，当 `class="item-0 active"` 是css选择器 `('.item-0.active)'` 

  | 方法     | 描述         |
  | -------- | ------------ |
  | find     | 所有子孙节点 |
  | children | 查找子节点   |
  | parent   | 直接父节点   |
  | parents  | 祖先节点     |
  | siblings | 兄弟节点     |
  
- pq_demo4：PyQuery类型都是 `PyQuery类型` 单个节点可直接打印输出，也可以转化成str。多个节点需要调用 `items` 。通过 `.attr()` 获取属性
  
  | 方法                        | 描述                                                         |
  | --------------------------- | ------------------------------------------------------------ |
  | .items                      | 返回多节点是用该方法获取标签                                 |
  | .attr('href')    .attr.href | 获取标签的href属性值。当返回多值时，调用该方法之返回第一个，此时通过遍历在attr获取属性值 |
  | .text()                     | 忽略节点内所有html，只获取纯文字内容。想要获取其中html需要调用html。多个节点时可以直接获取，并且合成一个字符串 |
  | .html()                     | 获取该节点后层的html。多个节点时需要items遍历获取，否则只返回第一个 |
  
- pq_demo5：对节点进行动态修改
  
  | 方法                               | 描述                         |
  | ---------------------------------- | ---------------------------- |
  | remove_class()                     | 移除该节点的某个class值      |
  | add_class()                        | 给该节点添加class值          |
  | .attr('name', 'link')              | 在该节点添加name属性值为link |
  | .text('change item')               | 将该节点text转化成后面内容   |
  | .html('<span>change item</span>>') | 将该html替换该节点           |
  | .find('p').remove()                | 删除p节点                    |
  
- pq_demo6：伪类选择器

  | 选择器            | 描述                 |
  | ----------------- | -------------------- |
  | :first-child      | 第一个标签           |
  | :last-child       | 最后一个标签         |
  | :nth-child(2)     | 第二个节点           |
  | :gt(2)            | 第三个之后的节点     |
  | nth-child(2n)     | 偶数位置的标签       |
  | :contains(second) | 含有second文本的标签 |

### parsel

[参考parsel](https://parsel.readthedocs.io/en/latest/) 

安装 `pip install parsel` [_](https://setup.scrape.center/parsel) 

- parsel_demo1：css、xpath方法提取元素。遍历用xpath提取文本

  | 方法      | 描述 |
  | --------- | ---- |
  | .css()    |      |
  | .xpath()  |      |
  | .get()    |      |
  | .getall() |      |
- parsel_demo2：选取属性。css选取属性使用 `:attr()` 并传入属性名称。xpath用 `/@` 再加属性名。用 `.get()` 获取
- parsel_demo3：正则匹配