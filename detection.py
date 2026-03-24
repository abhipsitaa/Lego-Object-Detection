import cv2

# Load image
img = cv2.imread("dataset/images/train/lego.jpg")
img_h, img_w = img.shape[:2] # Get image dimensions

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur (reduces noise)
gray = cv2.GaussianBlur(gray, (5,5), 0)

#Adaptive thresholding
thresh = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    11, 2
)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

yolo_labels = []

# Process contours
for cnt in contours:
    if cv2.contourArea(cnt) > 300:
        x, y, w, h = cv2.boundingRect(cnt)

        # Convert to YOLO format
        cx = (x + w/2) / img_w
        cy = (y + h/2) / img_h
        w_norm = w / img_w
        h_norm = h / img_h

        yolo_labels.append(f"0 {cx} {cy} {w_norm} {h_norm}")

        #Draw bounding box
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

# Save detections
with open("lego.txt", "w") as f:
    for label in yolo_labels:
        f.write(label + "\n")

# Show image
cv2.imshow("Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()