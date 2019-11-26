# Baidutranslation
百度翻译公开api
# 使用方法
需安装[Node](https://nodejs.org/en/)
```shell
pip install -r requirements.txt
```
## 即时翻译
```python
import translate
trans=translate.Trans()
trans.main()
```
## 单个翻译
```python
import translate
trans=translate.Trans()
p='Python is the best program lanugue in the word!'
result=trans.transl_entozh(p) #返回json格式数据
print(result['trans_result']['data'][0]['dst'])
#Python是世界上最好的语言程序！
```