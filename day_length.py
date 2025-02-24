import numpy as np

def f(theta, phi, n):
    a = 1
    b = np.sin(phi)
    t = np.linspace(0,np.pi,n)
    prim = 0#타원의 둘레 누적 합 변수
    for i in range(1,n):# 타원의 둘레 구하기
        x1 = a*np.cos(t[i-1])
        y1 = b*np.sin(t[i-1])
        x2 = a*np.cos(t[i])
        y2 = b*np.sin(t[i])
        prim += dis(x1,y1,x2,y2)
    # print(prim)
    return prim * np.cos(theta) * 6

def dis(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


print('input in degrees')
theta = np.radians(float(input('위도 in degree\t')))# 위도
#북반구 +
#남반구 -
phi = np.radians(float(input('축 각도 in degree\t')))# 축 각도
#여름 23.5
#겨울 -23.5
n = 10000# 분할개수 -> 타원의 둘레 구할떄 사용

a=f(theta,phi,n)
b=24-f(theta,phi,n)

#공전 보정
a *= ((24+(365*24)/(360*360))/24)
b *= ((24+(365*24)/(360*360))/24)

if phi*theta > 0:# 낮이기냐 밤이기냐 체크
    print("낮의 길이", end = ' ')
    print(max(a,b))
else:
    print("낮의 길이", end = ' ')
    print(min(a,b))

# 오차는 지구를 구형으로 가정하고 계산한 것에서 기인하는 것 같습니다.
#서울위도 37.5
#여름 축 23.5
#계산 값: 13.1
#실제 값: 14.75

#서울위도 37.5
#겨울 축 -23.5
#계산 값: 11
#실제 값: 9.5