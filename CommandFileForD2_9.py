from news.models import *
import random


user_1 = User.objects.create_user("Sergo")
user_2 = User.objects.create_user("Nasty")
author_1 = Author.objects.create(user=user_1)
author_2 = Author.objects.create(user=user_2)
auto_category = Category.objects.create(name="Авто")
journeys_category = Category.objects.create(name="Путешествия")
it_category = Category.objects.create(name="IT")
culture_category = Category.objects.create(name="Культура")
post_1 = Post.objects.create(author=author_1,
                             position="A",
                             heading = "Как Tesla изменит мир",
                             text = "МИФ: производство Тесла гораздо грязнее, чем производство Приуса. /nРЕАЛЬНОСТЬ: производство дорогих машин грязнее, чем дешевых, сравнивать Приус и Теслу в этом смысле все равно, что сказать, что производство Приуса грязное, потому что производства гольф-карта чище. Если сравнить сравнимое, производство Теслы настолько же грязное, как производство любого другого люксового автомобиля./nМИФ: электромобили оказывают чрезвычайно высокую нагрузку на электросети./nРЕАЛЬНОСТЬ: сеть спроектирована с расчетом на худшую секунду худшего дня худшего года — в них заложены избыточные мощности. Вы сможете заменить 70% пробега бензиновых авто пробегом электромобилей при использовании существующей сети. Этот процент еще вырастет с увеличением количества домохозяйств, имеющих солнечные батареи на своей крыше./nМИФ: Тесла содержит большое количество графита, который вносит большой вклад в ухудшение экологической ситуации в Китае./nРЕАЛЬНОСТЬ: Логика здесь такая: «В батареях Теслы используется графит; крупнейший производитель графита — Китай; в Китае — беда с экологией, поэтому Тесла частично виновата в загрязнении Китая». На самом деле Тесла использует синтетический графит, который делают в Польше и Японии, в каждом автомобиле — 100 кг графита. Эти 100 кг работают 10 лет, так что количество графита, которое используется в Модели С, примерно равно количеству графита, который вы используете, делая барбекю несколько раз в год.")
post_1.categories.set([auto_category,
                       it_category])
post_2 = Post.objects.create(author=author_2, position="N",
                             heading="Пригожин осудил лишение Украины права провести евровидение",
                             text="Руководящий совет музыкального конкурса пришел к выводу, что нынешние обстоятельства не позволяют выполнить «гарантии безопасности и эксплуатации, которые по правилам необходимы вещателю для проведения, организации и производства конкурса евровидение")
post_2.categories.set([culture_category])
post_3 = Post.objects.create(author=author_1,
                             position="A",
                             heading="Во что превратится Lada после ухода Renault?",
                             text="Полувековая история российской компании «АвтоВАЗ» волнообразна. Когда по советским дорогам поехали первые «Жигули», это были современные модели, построенные в партнерстве с итальянцами. Первый самостоятельный проект ВАЗа — внедорожник «Нива» — стал успешным не только на родине, но и в других странах по всему миру. Но ближе к 1990-м продукция завода устарела, и вплоть до начала 2010-х автомобили с ладьей на решетке радиатора оставляли желать лучшего. Никчемные «десятки» и «приоры», хотя и расходились в РФ большими тиражами, за пределами родины были никому не нужны. После выхода Granta ситуация стала улучшаться, и к концу второго десятилетия XXI века Lada расцвела, превратившись в современного производителя бюджетных машин. Опять помогли европейцы (на этот раз французы). Но день 24 февраля расколол историю российского автогиганта на до и после. Похоже, нас ждет очередная нисходящая волна в истории самой популярной марки из РФ.")
post_3.categories.set([auto_category])
comment_1 = Comment.objects.create(post=post_1,
                                   user=user_2,
                                   text="Только транспорт потребляет энергии больше, чем существующие мощности всей электрогенерации. Хотите пересесть на электромобили — да нет проблем, постройте рядом ещё столько-же электрогенерирующих и распределяющих мощностей, сколько было построено за весь 20-й век и начало 21-го. Цена вопроса не так уж и высока.")
comment_2 = Comment.objects.create(post=post_1,
                                   user=user_1,
                                   text="это МИФ, сеть спроектирована с расчетом на худшую секунду худшего дня худшего года — в них заложены избыточные мощности. Вы сможете заменить 70% пробега бензиновых авто пробегом электромобилей при использовании существующей сети. Этот процент еще вырастет с увеличением количества домохозяйств, имеющих солнечные батареи на своей крыше.")
comment_3 = Comment.objects.create(post=post_2,
                                   user=user_1,
                                   text="Европейский вещательный союз начал переговоры с Великобританией")
comment_4 = Comment.objects.create(post=post_3,
                                   user=user_2,
                                   text="Интересно, что же дальше")

for i in range(random.randint(1, 10)):
    post_1.like()
for i in range(random.randint(1, 10)):
    post_1.dislike()
for i in range(random.randint(1, 10)):
    post_2.like()
for i in range(random.randint(1, 10)):
    post_2.dislike()
for i in range(random.randint(1, 10)):
    post_3.like()
for i in range(random.randint(1, 10)):
    post_3.dislike()
for i in range(random.randint(1, 10)):
    comment_1.like()
for i in range(random.randint(1, 10)):
    comment_1.dislike()
for i in range(random.randint(1, 10)):
    comment_2.like()
for i in range(random.randint(1, 10)):
    comment_2.dislike()
for i in range(random.randint(1, 10)):
    comment_3.like()
for i in range(random.randint(1, 10)):
    comment_3.dislike()
for i in range(random.randint(1, 10)):
    comment_4.like()
for i in range(random.randint(1, 10)):
    comment_4.dislike()
author_1.update_rating()
author_2.update_rating()

Author.objects.all().order_by("-rating").values("user__username", "rating")[0]
Post.objects.all().order_by("-rating").values("date", "author__user__username", "rating", "heading")[0]
Post.objects.all().order_by("-rating")[0].preview()
Comment.objects.filter(post=Post.objects.all().order_by("-rating")[0]).values("date", "user__username", "rating", "text")