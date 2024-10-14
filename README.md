<h2>back 실행 방법</h2>

1. https://my.telegram.org/auth에 접속 후 API 해시키 발급

2. .env 파일에 위에서 받은 값을 토대로 아래 정보 입력.
   <code>
   telegram_id = "APP API_ID"
   telegram_hash = "APP API_HASH"
   telegram_phone = "로그인시 사용한 번호"
   </code>

3. requirements.txt 파일 설치

4. login.py 실행을 통해 back서버에서 사용할 session 파일 생성

5. python run.py 실행

<h2>Front 실행 방법</h2>

1. npm install을 통해 필요 라이브러리 설치

2. npm start를 통해 프론트 실행
