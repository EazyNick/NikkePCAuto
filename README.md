# **승리의 여신: 니케 - 자동화 프로그램** 🚀

### **프로그램 개요**
**승리의 여신: 니케 자동화 프로그램**은 반복적인 게임 테스트 및 자동화 작업을 수행하는 **QA 자동화 도구**입니다.  
이 프로그램은 **화면 캡처**, **템플릿 매칭**, **자동 클릭** 기능을 통해 효율적인 QA 테스트를 지원합니다.

---

## **주요 기능** ✨

1. **화면 캡처**  
   - 현재 게임 화면을 캡처하고 저장합니다.  

2. **템플릿 매칭**  
   - OpenCV를 활용해 템플릿 이미지와 현재 화면을 비교하여 특정 좌표를 찾아냅니다.  

3. **자동 클릭**  
   - 매칭된 좌표를 바탕으로 클릭, 마우스 이동, 드래그 등의 동작을 자동으로 수행합니다.  

4. **클릭 후 강조된 이미지 저장**  
   - 클릭한 좌표를 강조 표시한 이미지를 저장해 테스트 증적을 남깁니다.  

5. **유연한 로그 관리**  
   - 프로그램 실행 로그를 저장하고, 오래된 로그를 자동으로 정리합니다.  

---

## **설치 방법** 🛠️

### **1. 프로젝트 클론**
GitHub에서 프로젝트를 클론합니다:
```bash
git clone https://github.com/your-username/NikkePCAuto.git
cd NikkePCAuto
```

### **2. 가상환경 설정**  
Python 가상환경을 설정하고 활성화합니다:

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (Mac/Linux)
source venv/bin/activate
``

### **3. 의존성 패키지 설치**  
프로그램 실행에 필요한 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

## **사용 방법** 🚀

### **1. 로그인 화면 자동화**  
프로그램을 실행하면 로그인 화면의 템플릿 이미지를 찾아 자동으로 클릭합니다.

#### **실행 명령**
```bash
python module/click_image.py
```

#### **예상 동작**  
1. 게임 화면을 캡처합니다.  
2. 템플릿 이미지와 비교해 로그인 버튼 위치를 찾습니다.  
3. 해당 좌표를 클릭한 후, 강조된 스크린샷을 저장합니다.  

## **프로세스 요약**  
- 화면 캡처 → 템플릿 이미지 매칭 → 자동 클릭 → 강조된 이미지 저장  
- 로그 파일을 통해 실행 상태와 결과를 검토할 수 있습니다.

## **문의 및 피드백** 💬  
프로그램에 대한 질문이나 개선 사항은 [GitHub Issues](https://github.com/EazyNick/NikkePCAuto/issues)에 남겨주세요.

**승리의 여신: 니케 자동화 프로그램**은 QA 테스트의 반복 작업을 효율화하고, 정확도를 높이기 위해 설계되었습니다.  
프로그램 사용을 통해 테스트 프로세스를 더욱 **자동화**하고 **최적화**할 수 있습니다! 😊
