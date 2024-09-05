# 查看gt
# new = torch.squeeze(new_label, dim=0)
# print(f'new shape:{new.shape}')
# check_label = torch.zeros_like(new)
# check_label[new == 1] = 1
# check_label = check_label.numpy()
# cv2.imwrite('label1.png', 255 * check_label)
#
# check_label1 = torch.zeros_like(new)
# check_label1[new == 0] = 1
# check_label1 = check_label1.numpy()
# cv2.imwrite('label0.png', 255 * check_label1)
#
# check_label2 = torch.zeros_like(new)
# check_label2[new == 2] = 1
# check_label2 = check_label2.numpy()
# cv2.imwrite('label2.png', 255 * check_label2)
