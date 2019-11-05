from math import exp

input_w = [[1, 1, 2], [1, 2, 1], [2, 2, 1], [5, 5, 5]]
input_data = [4, 4, 4]


class Input_L:
    def activation(self, x):
        self.y = x * 1
        return self.y


class Image_L:
    def __init__(self, w):
        self.w = w

    def activation(self, x):
        sum = 0
        for i in range(len(self.w)):
            sum += exp(-(self.w[i] - x[i])**2/0.3**2)
        return sum


class Add_L:
    def activation(self, x):
        sum = 0
        for i in x:
            sum += i
        res = sum / len(x)
        return res


class Output_L:
    def activation(self, x):
        clas = "A"
        val = x[clas]
        for i in x.items():
            if i[1] > val:
                clas = i[0]
        return clas



input_1 = Input_L()
input_2 = Input_L()
input_3 = Input_L()

image_1 = Image_L(input_w[0])
image_2 = Image_L(input_w[1])
image_3 = Image_L(input_w[2])
image_4 = Image_L(input_w[3])

class_A = Add_L()
class_B = Add_L()

res = Output_L()

y_input = []
y_image = []
y_add = {}

y_input.append(input_1.activation(input_data[0]))
y_input.append(input_1.activation(input_data[1]))
y_input.append(input_1.activation(input_data[2]))

y_image.append([])
y_image.append([])
y_image[0].append(image_1.activation(y_input))
y_image[0].append(image_2.activation(y_input))
y_image[0].append(image_3.activation(y_input))
y_image[1].append(image_4.activation(y_input))

y_add.update({"A": class_A.activation(y_image[0])})
y_add.update({"B": class_B.activation(y_image[1])})

res = res.activation(y_add)

print("Класс",res)










