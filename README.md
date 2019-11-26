# baidutranslation
百度翻译公开api
# 使用方法
## 即时翻译
```python
import translate
trans=translate.trans()
trans.main()
```
## 单个翻译
```python
import translate
trans=translate.trans()
p='Python is the best program lanugue in the word!'
result=trans.transl_entozh(p) #返回json格式数据
print(result['trans_result']['data'][0]['dst'])
```