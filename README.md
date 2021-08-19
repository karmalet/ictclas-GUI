# ictclas-GUI
Graphic User Interface for ICTCLAS Chinese word segmentation &amp; POS tagging tool.  
All rights belong to its owner, NLPIR-team(https://github.com/NLPIR-team).  
For personal, non-profit use only.

## **Windows 로컬에서 실행하기**
1.   컴퓨터에 Python 환경 설치
> https://www.python.org/downloads/ (기본) 설치 후 python, pip 실행을 위해 python 환경 변수 설정 필요 <br>
> https://www.anaconda.com/products/individual#Downloads (확장) 설치 후 Anaconda Prompt를 사용, 환경 변수 설정 불필요

2. [Github ictclas_GUI](https://github.com/karmalet/ictclas_GUI)에서 ICTCLAS download zip 내려받기 & 압축 해제
> (예시) d:\ictlas_GUI-master <br>

3. 의존 패키지(dependency) 설치
```
d:\ictlas_GUI-master> pip install -r requirements.txt
```

4.   Ictclas_gui.py 실행
```
d:\ictlas_GUI-master> python Ictclas_gui.py
```
> 3,4 단계에서 문제가 생길 경우 환경 변수 설정 확인

5. error 발생 시: nlpir_jun.py 파일 내 .dll 세팅 조정
```
libFile = 'NLPIR64.dll' # 64 bit python
libFile = 'NLPIR32.dll' # 32 bit python
```
