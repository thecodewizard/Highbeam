from sys import path
path.append("D:\\Users\\Sam\\GIT\\fadecandy\\examples\\python")
import opc

m = {}

m[3105] = [6, 13]
m[3106] = [6, 9]
m[3107] = [6, 5]
m[3112] = [5, 15]
m[3111] = [5, 11]
m[3110] = [5, 7]
m[3109] = [5, 3]
m[3113] = [4, 17]
m[3114] = [4, 13]
m[3115] = [4, 9]
m[3116] = [4, 5]
m[3117] = [4, 1]
m[3118] = [3, 3]
m[3119] = [3, 7]
m[3120] = [3, 11]
m[3121] = [3, 15]
m[3122] = [2, 17]
m[3123] = [2, 13]
m[3124] = [2, 9]
m[3125] = [2, 5]
m[3126] = [2, 1]
m[3127] = [1, 3]
m[3128] = [1, 7]
m[3129] = [1, 11]
m[3130] = [1, 15]
m[3132] = [0, 13]
m[3133] = [0, 9]
m[3134] = [0, 5]

m[3073] = [0, 35]
m[3074] = [0, 31]
m[3075] = [0, 27]
m[3077] = [1, 25]
m[3078] = [1, 29]
m[3079] = [1, 33]
m[3080] = [1, 37]
m[3081] = [2, 39]
m[3082] = [2, 35]
m[3083] = [2, 31]
m[3084] = [2, 27]
m[3085] = [2, 23]
m[3086] = [3, 25]
m[3087] = [3, 29]
m[3088] = [3, 33]
m[3089] = [3, 37]
m[3090] = [4, 39]
m[3091] = [4, 35]
m[3092] = [4, 31]
m[3093] = [4, 27]
m[3094] = [4, 23]
m[3095] = [5, 25]
m[3096] = [5, 29]
m[3097] = [5, 33]
m[3098] = [5, 37]
m[3100] = [6, 35]
m[3101] = [6, 31]
m[3102] = [6, 27]

d = open("led_test.txt").readlines()
eye_offset = 95


numLEDs = 6*64*8 + 64

client = opc.Client('raspberrypi:7890')

buff = [ (0,0,0) ] * numLEDs



for led_id in m:
	row, col = m[led_id]
	row += eye_offset
	if d[row][col]=="#":
		buff[led_id] = (128,128,128)

client.put_pixels(buff)
client.put_pixels(buff)