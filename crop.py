import cv2

# mkdir `seq 1 29`

# 77-1959
start_page = 77
end_page = 1959

for i in range(start_page, end_page + 1):
  file_name_num = i

  org_img = cv2.imread("/Users/kitamurataku/work/shikihoOCR/shikiho-2020-haru/{}.jpg".format(file_name_num))

  # 1
  crop_img = org_img[337:825, 1071:1252]
  cv2.imwrite('1/{}.jpg'.format(file_name_num), crop_img)

  # 2
  crop_img = org_img[337:823, 807:1063]
  cv2.imwrite('2/{}.jpg'.format(file_name_num), crop_img)

  # 3
  crop_img = org_img[337:827, 544:800]
  cv2.imwrite('3/{}.jpg'.format(file_name_num), crop_img)

  # 4
  crop_img = org_img[337:827, 345:538]
  cv2.imwrite('4/{}.jpg'.format(file_name_num), crop_img)

  # 5
  crop_img = org_img[335:467, 104:339]
  cv2.imwrite('5/{}.jpg'.format(file_name_num), crop_img)

  # 6
  crop_img = org_img[473:565, 102:339]
  cv2.imwrite('6/{}.jpg'.format(file_name_num), crop_img)

  # 7
  crop_img = org_img[569:654, 104:339]
  cv2.imwrite('7/{}.jpg'.format(file_name_num), crop_img)

  # 8
  crop_img = org_img[658:744, 102:337]
  cv2.imwrite('8/{}.jpg'.format(file_name_num), crop_img)

  # 9
  crop_img = org_img[746:831, 102:337]
  cv2.imwrite('9/{}.jpg'.format(file_name_num), crop_img)

  # 10
  crop_img = org_img[837:1077, 807:1256]
  cv2.imwrite('10/{}.jpg'.format(file_name_num), crop_img)

  # 11
  crop_img = org_img[837:1006, 660:801]
  cv2.imwrite('11/{}.jpg'.format(file_name_num), crop_img)

  # 12
  crop_img = org_img[1012:1077, 662:801]
  cv2.imwrite('12/{}.jpg'.format(file_name_num), crop_img)

  # 13
  crop_img = org_img[837:1077, 102:656]
  cv2.imwrite('13/{}.jpg'.format(file_name_num), crop_img)

  # 14
  crop_img = org_img[1085:1575, 1071:1252]
  cv2.imwrite('14/{}.jpg'.format(file_name_num), crop_img)

  # 15
  crop_img = org_img[1087:1575, 807:1063]
  cv2.imwrite('15/{}.jpg'.format(file_name_num), crop_img)

  # 16
  crop_img = org_img[1085:1577, 544:801]
  cv2.imwrite('16/{}.jpg'.format(file_name_num), crop_img)

  # 17
  crop_img = org_img[1085:1577, 343:538]
  cv2.imwrite('17/{}.jpg'.format(file_name_num), crop_img)

  # 18
  crop_img = org_img[1083:1217, 110:339]
  cv2.imwrite('18/{}.jpg'.format(file_name_num), crop_img)

  # 19
  crop_img = org_img[1221:1313, 102:339]
  cv2.imwrite('19/{}.jpg'.format(file_name_num), crop_img)

  # 20
  crop_img = org_img[1317:1402, 102:339]
  cv2.imwrite('20/{}.jpg'.format(file_name_num), crop_img)

  # 21
  crop_img = org_img[1406:1491, 102:337]
  cv2.imwrite('21/{}.jpg'.format(file_name_num), crop_img)

  # 22
  crop_img = org_img[1495:1579, 102:337]
  cv2.imwrite('22/{}.jpg'.format(file_name_num), crop_img)

  # 23
  crop_img = org_img[1585:1825, 807:1258]
  cv2.imwrite('23/{}.jpg'.format(file_name_num), crop_img)

  # 24
  crop_img = org_img[1585:1825, 662:803]
  cv2.imwrite('24/{}.jpg'.format(file_name_num), crop_img)

  # 25
  crop_img = org_img[1583:1825, 102:658]
  cv2.imwrite('25/{}.jpg'.format(file_name_num), crop_img)

  # 26
  crop_img = org_img[61:329, 100:516]
  cv2.imwrite('26/{}.jpg'.format(file_name_num), crop_img)

  # 27
  crop_img = org_img[68:327, 520:678]
  cv2.imwrite('27/{}.jpg'.format(file_name_num), crop_img)

  # 28
  crop_img = org_img[59:323, 677:1099]
  cv2.imwrite('28/{}.jpg'.format(file_name_num), crop_img)

  # 29
  crop_img = org_img[68:327, 1101:1260]
  cv2.imwrite('29/{}.jpg'.format(file_name_num), crop_img)
