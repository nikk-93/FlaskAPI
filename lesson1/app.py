from flask import Flask
from flask import render_template
import lorem


class Product:
    def __init__(self,
                 type: str,
                 src_img: str,
                 title: str,
                 description: str,
                 price: float):
        self.type = type
        self.src_img = src_img
        self.title = title
        self.description = description
        self.price = price


app = Flask(__name__)

products = [Product(type="clothes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Куртка",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="clothes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Рубашка",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="clothes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Штаны",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="clothes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Футболка",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="clothes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Майка",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="clothes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Шапка",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="clothes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Кепка",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="shoes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Бархатные тяги",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="shoes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Сланцы",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="shoes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Мокасины",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="shoes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Монки",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="shoes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Лоферы",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="shoes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Дерби",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),
            Product(type="shoes",
                    src_img="https://lipsum.app/random/300x200",
                    title="Оксфорды",
                    description=lorem.get_sentence(
                        count=4, word_range=(10, 15)),
                    price=12.1),]


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', products=products)


@app.route('/base/')
def base_template():
    return render_template(template_name_or_list='base.html')


@app.route('/about_us/')
def about_us():
    return render_template(template_name_or_list='about_us.html')


@app.route('/contacts/')
def contacts():
    return render_template(template_name_or_list='contacts.html')


@app.route('/clothes/')
def clothes():
    return render_template(
        template_name_or_list='clothes.html',
        products=[x for x in products if x.type == 'clothes'])


@app.route('/shoes/')
def shoes():
    return render_template(
        template_name_or_list='shoes.html',
        products=[x for x in products if x.type == 'shoes'])


if __name__ == '__main__':
    app.run(debug=True)
