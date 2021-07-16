from celery import shared_task

from ..models import Site, RelatedSite


@shared_task
def writeFiles(url="https://github.com"):
    with open("mytask.txt", "w") as f:
        f.write(url)
    pass

