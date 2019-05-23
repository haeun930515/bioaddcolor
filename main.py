import cv2
from detect_face import DetectFace
from dominant_colors import DominantColors
from tone_analysis import ToneAnalysis
from getjson import GetJson
import imutils
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

# 이성경(res/lees.jpg) dominant colors by order of histogram
# skin, hair, eye 순서
lsk_rgb = [[222.5, 201.4, 188.9], [138.6, 98.4, 55.0], [159.8, 115.8, 61.7]]
lsk_lab = []
for color in lsk_rgb:
    rgb = sRGBColor(color[0], color[1], color[2], is_upscaled=True)
    lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
    lsk_lab.append([lab.lab_l, lab.lab_a, lab.lab_b])

getJson = GetJson()
C = getJson.get_standard('res/standard.json')

tone_analysis = ToneAnalysis()

print("******************")
a = [30, 20, 10] # 가중치
spring = 0
summer = 1
fall = 2
winter = 3
print("이성경")
print("봄   : ", format(tone_analysis.probability(lsk_lab, spring, C, a),".2f"), "%")
print("여름 : ", format(tone_analysis.probability(lsk_lab, summer, C, a),".2f"), "%")
print("가을 : ", format(tone_analysis.probability(lsk_lab, fall, C, a),".2f"), "%")
print("겨울 : ", format(tone_analysis.probability(lsk_lab, winter, C, a),".2f"), "%")
print("******************")
'''
# Set paths
image = "res/lees.jpg"
predictor = "shape_predictor_68_face_landmarks.dat"

# Create an DetectFace instance
df = DetectFace(predictor, image)

# Try: Extract mouth part
mouth = df.extract_face_part(df.mouth)

# Try: Extract right eye part
r_eye = df.extract_face_part(df.right_eye)

# Try: Extract left eye part
l_eye = df.extract_face_part(df.left_eye)

# Try : Extract cheek part
l_cheek = df.cheek_img[0]
r_cheek = df.cheek_img[1]


# Create an DominantColors instance on left cheek image
clusters = 5
lc_dc = DominantColors(l_cheek, clusters)
lc_colors = lc_dc.dominantColors()
print(lc_colors)
lc_dc.plotHistogram()

# Create an DominantColors instance on left cheek image
rc_dc = DominantColors(r_cheek, clusters)
rc_colors = rc_dc.dominantColors()
print(rc_colors)
rc_dc.plotHistogram()

# Try : Dominant color on right_eye
clusters = 6
dc_re = DominantColors(r_eye, clusters)
colors = dc_re.dominantColors()
print(colors)
dc_re.plotHistogram()

# hair
hair_img = "res/lees_hair.jpg"
img = cv2.imread(hair_img)
resized_img = imutils.resize(img, width = 100)
clusters = 6
dc_re = DominantColors(resized_img, clusters)
colors = dc_re.dominantColors()
print(colors)
dc_re.plotHistogram()
'''
