def calculatePaintCan(height,width,cover):
  area = height * width
  numberOfCan = math.ceil(area / cover)
  print(f"The number of can for painting the wall is {cover}")

askHeight = int(input("Height of the wall: "))

askWidth = int(input("Width of the wall: "))

coverage = 5

calculatePaintCan(height = askHeight, width = askWidth, cover = coverage)