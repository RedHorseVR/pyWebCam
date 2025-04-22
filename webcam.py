import cv2





#  MAIN PROGRAM AREA
ID = 0 ;
cap = cv2.VideoCapture( ID )

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280  )
cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 720 )
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
h =  cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
print( w , ' X ' , h )


cv2.namedWindow("view", cv2.WINDOW_FREERATIO)
delay = 3
key = -1
L = 1
row = 0;

while( key== -1 ):
	ret, frame  = cap.read()
	cv2.imshow( 'view', frame )
	key = cv2.waitKey(delay)
	

cap.release()
cv2.destroyAllWindows()


#  Export  Date: 02:20:46 PM - 20:Mar:2025.

