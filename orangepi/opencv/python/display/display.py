import cv2
c = cv2.VideoCapture(1)

while(1):
  _,f = c.read()
  cv2.imshow('Camera Orange Pi',f)
  k = cv2.waitKey(5)
  if k==27:
      #Esc key to stop
      break
  elif k==-1:
      continue
  else:
      print(k)

cv2.destroyAllWindows()
