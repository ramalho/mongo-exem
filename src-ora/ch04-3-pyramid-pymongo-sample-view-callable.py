
import datetime
def my_view(request):
    new_page_hit = {"timestamp":datetime.datetime.utcnow(), "url":request.url}
    request.db.page_hits.insert(new_page_hit, safe=True)
    return {"project":"mongofoo"}
