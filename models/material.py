from models.material_type import MaterialType
from models.material_cards import MaterialCard
from typing import List


class Material():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cards = {}

    def set_card(self, type: MaterialType):
        print(type.id)
        print(type.mat_props)
        self.cards[type.id] = MaterialCard(type.id,type)
        # Вроде бы логично, что у карты материала тот же id, что и у соответствующего типа материала. Но это работает,
        # пока мы с одним материалом работаем только. Если брать два одинаковых типа, но разных по свойствам, нужно как-то счетчик внедрять.
        # Плюс нужна же проверка того, что добавленные карты не конфликтуют (чтобы одновременно не задать изотропный и ортотропный)
        # Вот тут, наверное, надо отдельной процедурой это описать. Но у меня класс объекта cards не объявлен, чтобы я мог ссылаться на его составляющие
        # Далее должна идти такая проверка, но мне не совсем понятно, как можно в процедуре попросить его проверить и сравнить отсутствующее содержимое
        # Поэтому далее идет сомнительной эффективности реализация такой проверки, в предположении, что у нас 4 типа материалов, которые не должны конфликтовать

#    def check_material(self):
#        j = 0
#        k = 0
#        for i in self.cards.id:
#            if j == 0:
#                k=i
#            else:
#                if abs(i-k) == 1:
#                    print('Error. Material cards incompability detected')
#            j=j+1









