# Lxper_nsw
 Lxper 기술과제 git 제출자료입니다.

# How to Use
 실행을 위해선 model.zip 파일이 필요합니다.
 LXPER.ipynb 파일을 실행해 model.zip 파일을 확보해주세요.

 run server
 ```bash
 $ uvicorn app:app --reload
 ```

 request
 ```bash
 $ curl -X POST -H "Content-type: application/json" -d "{\"passage\":\"I are a boy.\"}" http://localhost:8000/generate
 ```