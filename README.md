# 팀 과제 5: Docker-compose 활용 / 복수 컨테이너 생성과 실행

## 개요
**팀 과제 3-1**의 파일을 기반으로 **docker-compose**를 통해 웹페이지를 구동하는 과제입니다.
**FrontEnd**와 **BackEnd** 파일을 구분해 각각 **frontapp**, **backapp** 컨테이너로 구동됩니다.

### 사용 방법

1. **저장소 복제 (특정 브랜치만)**  
   아래 명령어를 사용하여 저장소를 복제합니다. `-b` 옵션은 특정 브랜치를 지정하여 복제할 때 사용됩니다.

   ```bash
   git clone -b sub5 https://github.com/CSID-DGU/2024-2-OSSPrac-tOSS-06 {디렉토리_이름}

2. **docker-compose 실행**
   아래 명령어를 사용하여 frontapp, backapp 컨테이너를 동시에 백그라운드에서 실행합니다.

   ```bash
   cd {디렉토리_이름}
   docker-compose up -d

3. **localhost:3000 접속**
   브라우저에서 localhost:3000에 접속하거나, **Docker Dashboard**에서 해당 컨테이너의 포트 부분에 나와있는 `3000:80`을 클릭합니다.

4. **Backapp 컨테이너 로그 확인**
   컨테이너의 출력이나 에러 로그를 확인하기 위해 아래 명령어를 사용합니다.

   ```bash
   docker logs {디렉토리_이름}-backapp-1
   ```
   또는 **Docker Dashboard**에서 해당 컨테이너를 클릭하여 **Logs**에서 로그를 확인합니다.

#### 팀과제5 8번 요구사항 영상

[![동영상 보기](https://img.youtube.com/vi/1FV6s39ObU0/0.jpg)](https://youtu.be/1FV6s39ObU0)

클릭 시 **유튜브**로 이동되며, 영상 파일은 **해당 브랜치 최상위 디렉토리**에 위치합니다.

