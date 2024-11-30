# 팀 과제 6: Jenkins 활용 웹 구축

## 개요
- **팀 과제 5**를 기반으로 **jenkins**를 이용해 웹페이지를 빌드하고 배포하기 쉬운 형태로 만드는 과제입니다.
- **FrontEnd**와 **BackEnd** 파일을 구분해 각각 **frontapp**, **backapp** 컨테이너로 구동됩니다.
- 기존 **팀 과제 5**는 **Frontapp 컨테이너**에서 한꺼번에 앱을 실행했으며, 이는 **FrontEnd와 BackEnd를 구분하는 의미**를 상실한다고 생각했습니다.
- 따라서 추가적인 학습을 통해 몇 가지 수정사항을 거쳐 **FrontEnd와 BackEnd가 요청을 주고 받아** 웹페이지 하나를 구동하는 방식을 구현했습니다.

### 사용 방법

1. **저장소 복제 (특정 브랜치만)**  
   아래 명령어를 사용하여 저장소를 복제합니다. `-b` 옵션은 특정 브랜치를 지정하여 복제할 때 사용됩니다.

   ```bash
   git clone -b sub5_divided https://github.com/CSID-DGU/2024-2-OSSPrac-tOSS-06 {디렉토리_이름}

2. **docker-compose 실행**
   아래 명령어를 사용하여 frontapp, backapp 컨테이너를 동시에 백그라운드에서 실행합니다.
   - 필요한 이미지는 이미 **DockerHub에 push**되어 있어 **already exists** 메시지가 발생합니다.

   ```bash
   cd {디렉토리_이름}
   docker-compose up -d

4. **localhost:3000 접속**
   브라우저에서 localhost:3000에 접속하거나, **Docker Dashboard**에서 해당 컨테이너의 포트 부분에 나와있는 `3000:3000`을 클릭합니다.

5. **컨테이너 로그 확인**
   컨테이너의 출력이나 에러 로그를 확인하기 위해 아래 명령어를 사용합니다.

   ```bash
   docker logs {디렉토리_이름}-{frontapp 또는 backapp}-1
   ```
   또는 **Docker Dashboard**에서 해당 컨테이너를 클릭하여 **Logs**에서 로그를 확인합니다.

