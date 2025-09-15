import cv2
import time

def main():
    # 웹캠 열기
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ 카메라 열기 실패")
        return

    # HOG 보행자 감지기 초기화
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # 첫 프레임 읽기
    ret, prev_frame = cap.read()
    if not ret:
        print("❌ 첫 프레임 읽기 실패")
        return

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

    MIN_AREA = 1500  # 최소 영역 픽셀 수 (작은 움직임 무시)
    last_motion_time = 0
    motion_cooldown = 1.0  # 연속 감지 제한 (초)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 흑백 + 블러
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # 프레임 차이로 모션 감지
        frame_delta = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motion_detected = False

        # 초록 박스 + 윤곽선 표시
        for contour in contours:
            if cv2.contourArea(contour) < MIN_AREA:
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 초록 박스
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)          # 윤곽선
            motion_detected = True

        # 모션 로그
        now = time.time()
        if motion_detected and (now - last_motion_time) > motion_cooldown:
            last_motion_time = now
            print(f"[{time.strftime('%H:%M:%S')}] Motion detected!")

        # 사람 탐지 (HOG 보행자)
        rects, weights = hog.detectMultiScale(frame, winStride=(8,8))
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 빨간 박스
            cv2.putText(frame, "Person", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255), 2)

        # 모션 상태 텍스트
        cv2.putText(frame, f"Motion: {'YES' if motion_detected else 'NO'}", (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 0, 255) if motion_detected else (255, 0, 0), 2)

        cv2.imshow('Motion Camera', frame)
        prev_gray = gray

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            # s 키 누르면 스냅샷 저장
            ts = int(time.time())
            filename = f"snapshot_{ts}.jpg"
            cv2.imwrite(filename, frame)
            print("Saved", filename)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
