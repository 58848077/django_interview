# :notebook_with_decorative_cover: Wavenet Django Interview

## 給定之資料庫表格
```python
class Company(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name =  models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
```
## 資料庫表格資料範例
#### Company
|id |name
|----- |------ 
|1 |A-Link
|2 |Banky
|3 |CRS
|... |...

#### Customer
|id |first_name |last_name |create_time |edit_time| company
|----- |------ |----- |------ |------ |-----
|1 |Kevin  |Chang |2022-12-01 10:25:02.743289 |2022-12-29 09:33:05.163253 |1
|2 |Victor |Chang |2022-12-01 10:25:02.743289 |2022-12-29 09:33:05.163253 |1
|3 |Wendy  |Liu   |2022-12-07 10:25:02.743289 |2022-12-29 09:33:05.163253 |2
|4 |Peter  |Huang |2022-12-15 10:25:02.743289 |2022-12-29 09:33:05.163253 |2
|5 |Johnny |Wang  |2022-12-23 10:25:02.743289 |2022-12-29 09:33:05.163253 |3
|... |... |... |... |... |...


## 請寫出:
### 1. 完成interview_app中的views.py（RESTful API 的 CRUD）

### 2. 為views.py中的InterviewView建立API端點（endpoint）

### 3. 於models.py建立以下表格，並於Customer中新增ManyToMany欄位
```python
class Tag(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=30)
```
#### Tag
|id |name
|----- |------ 
|1 |Tag-1
|2 |Tag-2
|3 |Tag-3
|... |...