
def cook_book_generate():
    cook_book = {}
    with open('recipe.txt') as source:
        for line in source:
            if len(line) == 1:
                dish_name = source.readline().lower()
                ingr_quantity = int(source.readline())
                ingridients = []
                for i in range(0, ingr_quantity):
                    one_item = {}
                    ing = source.readline().lower().strip().split(' | ')
                    one_item['ingridient_name'] = ing[0]
                    one_item['quantity'] = int(ing[1])
                    one_item['measure'] = ing[2]
                    ingridients.append(one_item)
                # print(ingridients)
            cook_book[dish_name.strip()] = ingridients
        # print(cook_book)
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=\
            new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

cook_book = cook_book_generate()

create_shop_list()
