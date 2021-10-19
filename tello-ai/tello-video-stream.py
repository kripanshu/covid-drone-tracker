import cv2

tello_video = cv2.VideoCapture('udp://@0.0.0.0:11111')
while True:
    try:
        ret, frame = tello_video.read()
        print("ret", ret)
        if ret:
            cv2.imshow('Tello Video', frame)
            cv2.waitKey(1)
    except Exception as err:
        print(err)

tello_video.release()
cv2.destroyAllWindows()
#
# import cv2
# import queue
# import time
# import threading
#
# q = queue.Queue()
#
#
# def Receive():
#     print("start Reveive")
#     cap = cv2.VideoCapture("https://www.rmp-streaming.com/media/big-buck-bunny-360p.mp4")
#     ret, frame = cap.read()
#     q.put(frame)
#     while ret:
#         ret, frame = cap.read()
#         q.put(frame)
#
#
# def Display():
#     print("Start Displaying")
#     while True:
#         if q.empty() != True:
#             frame = q.get()
#             cv2.imshow("frame1", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#
# if __name__ == '__main__':
#     p1 = threading.Thread(target=Receive)
#     p2 = threading.Thread(target=Display)
#     p1.start()
#     p2.start()