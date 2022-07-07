# ictclas-GUI
Graphic User Interface for ICTCLAS Chinese word segmentation &amp; POS tagging tool.  
All rights belong to its owner, NLPIR-team(https://github.com/NLPIR-team).  
For personal, non-profit use only.

## **Windows 로컬에서 실행하기**
1.   컴퓨터에 Python 환경 설치 (아래 중 택 1)
> 1.1 https://www.python.org/downloads/ (기본) 설치 후 python, pip 실행을 위해 python 환경 변수 설정 필요 <br>
> 1.2 https://www.anaconda.com/products/individual#Downloads (확장) 설치 후 Anaconda Prompt를 사용, 환경 변수 설정 불필요

2. [Github ictclas_GUI](https://github.com/karmalet/ictclas_GUI)에서 ICTCLAS download zip 내려받기 & 압축 해제
> (예시) d:\ictclas_GUI-master <br>

3. 의존 패키지(dependency) 설치
> 1.1의 경우 cmd에서, 1.2의 경우 Anaconda Prompt에서 아래 명령을 실행합니다
```
d:\ictclas_GUI-master> pip install -r requirements.txt
```
> 3 단계에서 문제가 생길 경우 환경 변수 설정 확인

4.   Ictclas_gui.py 실행
```
d:\ictclas_GUI-master> python ictclas_gui.py
```

5. error 발생 시: nlpir_jun.py 파일 편집하여 .dll 세팅 조정
```
# libFile = '/content/ictclas_GUI/libNLPIR64.so'
libFile = 'NLPIR64.dll' # 64 bit python 설치하였을 경우, 해당 행 앞의 # 표시 삭제
libFile = 'NLPIR32.dll' # 32 bit python 설치하였을 경우, 해당 행 앞의 # 표시 삭제
```
6. License 만료 시 NLPIR.user 파일 갱신<br>
[1달 라이센스 파일 다운로드](https://github.com/NLPIR-team/NLPIR/blob/master/License/license%20for%20a%20month/NLPIR-ICTCLAS%E5%88%86%E8%AF%8D%E7%B3%BB%E7%BB%9F%E6%8E%88%E6%9D%83/NLPIR.user)<br>
> `d:\ictclas_GUI-master\Data\`에 복사
<br>

## 문제 해결
실행후 생성되는 .err 파일 내용 확인
