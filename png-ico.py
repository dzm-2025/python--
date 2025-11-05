from PIL import Image
def png_to_ico_with_sizes(png_path, ico_path, sizes=[(256, 256)]):
   img = Image.open(png_path)
   img.save(ico_path, format='ICO', sizes=sizes)
png_to_ico_with_sizes("E:\\360MoveData\\Users\\Administrator\\Pictures\\Screenshots\\log.png", "E:\\360MoveData\\Users\\Administrator\\Desktop\\上课抽号系统\\code\\log.ico", sizes=[(256, 256)])