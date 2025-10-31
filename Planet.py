#Lớp node lưu trữ hành tinh
class PlanetNode:
    def __init__(self, name, diameter, mass, axis, period):
        self.name= name
        self.diameter= diameter
        self.mass=mass
        self.axis=axis
        self.period=period
        self.next= None
    def __str__(self):
        return f"{self.name}: Duong kinh={self.diameter}, khoi luong={self.mass}, truc lon={self.axis}, chu ki={self.period}"
class PlanetStack:
    def __init__(self):
        self.top= None
        
    def push(self, name, diameter, mass, axis, period):
        new_node= PlanetNode(name, diameter, mass, axis, period) #NewNode chua thong tin hanh tinh
        new_node.next= self.top #Tạo liên kết nút mới với phần thử hiện tại đang ở đỉnh ngăn xếp(Nút mới nằm ở trên, nút cũ sẽ nằm ở bên dưới)
        self.top = new_node
        
    def find_planet(self,name):
        current = self.top 
        while current:
            if current.name.lower() == name.lower():#kh phan biet chuw hoa voi chu thuong
                return current
            current = current.next
        return None
    
planet_data = [
    ("Mercury", 0.383, 0.06, 0.39, 0.24),
    ("Venus", 0.949, 0.81, 0.72, 0.62),
    ("Earth", 1.000, 1.00, 1.00, 1.00),
    ("Mars", 0.532, 0.11, 1.52, 1.88),
    ("Jupiter", 11.209, 317.83, 5.20, 11.86),
    ("Saturn", 9.449, 95.16, 9.58, 29.45),
    ("Uranus", 4.007, 14.54, 19.19, 84.02),
    ("Neptune", 3.883, 17.15, 30.07, 164.79)
]


stack= PlanetStack()
for planet in planet_data:
    stack.push(*planet)
while True:
    planet_name = input("Nhập tên hành tinh bạn muốn xem thông tin(hoặc 'exit' để thoát) : ")
    if planet_name.lower()=="exit":
        print("Đã thoát chương trình")
        break
    result = stack.find_planet(planet_name)
    if result:
        print("Thông tin hành tin:")
        print(result)
    else:
        print("không tìm thấy hành tinh trong dữ liệu ")



