# Spider



## 第3章

### xpath

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
- xpath_demo12：节点轴获取子元素、兄弟元素、父元素、祖先元素等

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

| 节点轴            | 描述         |
| ----------------- | ------------ |
| ancestor          | 祖先节点     |
| attribute         | 节点属性     |
| child             | 直接孩子节点 |
| descendant        | 子孙节点     |
| following         | 之后节点     |
| following-sibling | 兄弟节点     |



