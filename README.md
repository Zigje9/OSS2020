![logo](https://ifh.cc/g/5ZgIzu.png)
=
****
### The project is designed for open source software development subjects.
****
Project members
-
### 1. 김기태(2017011667)
   >Github link :<https://github.com/1004gite> 
### 2. 박제구(2015038304)
  >Github link : <https://github.com/Zigje9>   
### 3. 윤찬웅(2017012279)
  >Github link :<https://github.com/qicqock>
### 4. 정충호(2017012506)
  >Github link : <https://github.com/cndgh98>
### 5. 조래준(2015038631)
  >Github link : <https://github.com/raejoonee>

프로젝트 소개
-
   > 이 프로젝트는 지도 일기를 구현하는 프로젝트로 연인간에 데이트 지도일기, 여행일기 등으로 활용이 가능하다.
   > 사용법은 사용자가 지도에 장소를 선택하고 메모를 입력하면 해당 정보가 저장이 된다. 
   > Frontend는 Vue.js, Backend는 Django 프레임워크를 사용하였고, 데이터베이스는 sqlite3(django 내장), 카카오 맵 API를 사용하여 구현 했습니다.
   > 협업 도구로는 Trello, Slack, Git을 사용했습니다.
   
   > Trello link :<https://trello.com/b/0vyzMTpX/oss-project>
   
   > Slack link :<https://oss-dev-2020.slack.com/archives/G0111F29WHZ>
   
   >Homepage link :<https://1004gite.github.io/oss2020project/>
  
기능 소개
-
#### 1. 선택한 좌표에 메모를 생성 할 수 있다. (formData : 경도, 위도 , 메모내용 , 생성시간)
#### 2. 저장된 정보를 가져와 지도에 표시해 준다. 

   
   
Required settings
-
#### 1. You need node.js, python , pip  
#### 2. set interpreter : python3.7
   >(Appdata-program-python-pythonm)
#### 3. in frontend : install npm 
    npm install
#### 4. in map_note : install django,django-webpack-loader and djangorestframework
    pip install django
    pip install django-webpack-loader
    pip install djangorestframework
#### 5. You need Kakao map API key ([Kakao Map](https://apis.map.kakao.com/web/))
##### Change map_note/frontend/App.vue in mounted()
    script.src = 'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=(Your kakao map api key)'
    
How to run
-
#### 1. in frontend 
    npm run dev
#### 2. in map_note 
    python manage.py runserver
    
    
If the webpage does not work
-
#### 1.Remove map_note/db.sqlite3. 
#### 2.And remove map_note/vuenote/migrations/0001_initial.py.
    initialize data type.
#### 3.in terminals(/map_note/) enter the command line
    python manage.py makemigrations
    python manage.py migrate

Open source used
-
django-vuejs link : <https://github.com/crescentmusyoki/django-vuejs>

