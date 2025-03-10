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
