from django.shortcuts import render, HttpResponse, Http404

     name = "Леонид"
   surname = "Попов"
   email = "darkesgg285@gmail.com"
   phone = "8-988-185-14-67"

 items = [
     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
     {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
     {"id": 4, "name": "Картофель фри" ,"quantity":0},
     {"id": 5, "name": "Кепка" ,"quantity":124},


 def about(request):
     info = f""" <div>Имя: <b>{name}</b> </div>
                 Фамилия: <b>{surname}</b> <br>
                 телефон: <b>8-923-600-01-02</b> <br>
                 email: <b>{email}</b>"""
     return HttpResponse(info)
     context = {
         "name": "Леонид",
         "surname": "Попов",
         "phone": 79008001012,
         "email": [2, 5, "6", 7.6, 8]
     }
     return render(request, "about.html", context)


 def home(request):
     text = f"""<h1> "Изучаем django" </h1>
     <strong> Автор </strong>: <i> {surname} Л.А. </i>"""
     return HttpResponse(text)
     return render(request, "index.html")


 def item_page(request, id):
  for item in items:
      if item["id"] == id:
          return render(request,"item_page.html",item)

    raise Http404(f"Товар с id={id} не найден")


 def items_list(request):
     items_result = "<ol>"
     for item in items:
         items_result += "<li>" + f"<a href='/item/{item['id']}'>" + item["name"] + "</a>" + "</li>"

     items_result += "</ol>"

     return HttpResponse(items_result)
     # items_result = "<ol>"
     # for item in items:
     #     items_result += "<li>" + f"<a href='/item/{item['id']}'>" + item["name"] + "</a>" + "</li>"
     #
     # items_result += "</ol>"
     #
     # return HttpResponse(items_result)
     context = {
         "items": items
     }
     return render(request, "items.html", context)
