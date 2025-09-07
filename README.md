# 광시야각 카메라 기반 운전자·승객 모니터링 (Driver & Passenger Monitoring)

![Project Banner](./docs/banner.png) <!-- 원하는 배너가 있으면 경로 수정 -->
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 개요
하나의 광시야각(와이드) 카메라를 통해 운전자와 조수석 승객을 동시에 모니터링하고, OpenCV 기반의 얼굴·눈·핸드 분석과 YOLO 기반 객체 감지를 결합해 졸음, 휴대폰 사용, 안전벨트 미착용, 부적절한 자세, Hands-On-Detection(HOD) 등을 실시간으로 판정하여 경고를 발생시키는 시스템입니다.

목표: 엣지(차내)에서 실시간으로 동작하며 프라이버시를 지키는(on-device) DMS(Driver Monitoring System) 프로토타입 구현.

---

## 주요 기능
- 광시야각 미러 카메라 입력(주야간 대응: IR 보조 가능)
- 영상 전처리(렌즈 보정, 노이즈 제거, 정규화)
- OpenCV 기반 얼굴/랜드마크/눈( blink / EAR ) 분석
- Head pose(머리 각도) 및 gaze(시선) 추정
- Hand / HOD (핸들 파지) 분석
- YOLO 기반 객체 감지: 스마트폰, 안전벨트(위치 기반), 기타 위험 객체
- 시계열 융합(슬라이딩 윈도우)으로 행동 분류(규칙 기반 + ML 모델)
- 경고 출력: 음성/버저/HUD/CAN 이벤트 로그
- 엣지 최적화(ONNX → TensorRT / OpenVINO 변환 추천)

---

## 사용 기술 스택
- **운영체제**: Linux  
- **라이브러리 / 프레임워크**: OpenCV, YOLO (YOLOv5/v8 계열 권장)  
- (권장) 엣지 하드웨어: NVIDIA Jetson 시리즈, Raspberry Pi + NCS2(성능 한계 주의)

---

## 구조(간단)
