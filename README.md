# VerdictTag
tag the license, phone number and bank account in the verdict
## 安裝
pip install -U git+https://github.com/NLU-Law-Tech/VerdictTag.git
## 使用
- `input`: 
    - verdict: 判決書 ( string )
- `output`:
    - 所有找到物件的 list
### 判決書清洗
用來去除原始判決書中的換行、空白等符號，以利正則可以找到完整的物件
```python 
from VerdictTag import cleansing
verdict = cleansing(verdict)
```
### 找車牌
```python 
from VerdictTag import find_license
items = find_license(verdict)
```
回傳物件說明
- start: 號碼起始位置 ( int )
- end: 號碼結束位置 ( int )
- value: 號碼字串 ( string )
- type: "car" 表示此物件為車牌
- vehicleType: 車種 例如:普通自小客車、普通重型機車
### 找銀行帳號
```python 
from VerdictTag import find_bank
items = find_bank(verdict)
```
回傳物件說明
- start: 號碼起始位置 ( int )
- end: 號碼結束位置 ( int )
- value: 號碼字串 ( string )
- type: "bank" 表示此物件為銀行帳號
- bank_name: 銀行名稱 例如:臺灣銀行、土地銀行
- branch: 分行名稱
### 找手機
```python 
from VerdictTag import find_phone
items = find_phone(verdict)
```
回傳物件說明
- start: 號碼起始位置 ( int )
- end: 號碼結束位置 ( int )
- value: 號碼字串 ( string )
- type: "phone" 表示此物件為手機號碼
