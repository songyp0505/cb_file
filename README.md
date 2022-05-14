# cb_file

中国经营报电子版爬取

## 原由

 老师上课提到可以关注关注中国经营报，而官媒信息太过分散，纸质版学校也没卖的，网购报纸总感觉不太划算，幸好有电子版的

## 依赖安装：

```python
pip install -r requriements.txt
```

## Chrome版本：

 Windows：
 101.0.4951.67（正式版本）项目已经附上chromedriver了
 Linux：
 89.0.4389.23版本

## 程序入口：

start.bat （主文件是cb_file.py）

## 程序逻辑：

1.访问http://dianzibao.cb.com.cn/

2.获取每一版面的pdf文件并保存

3.合并pdf

4.生成以当前日期为文件名的pdf
