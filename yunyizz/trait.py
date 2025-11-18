from yunyizz.api import SetSpiderAccountOffline, MarkTaskWaiting, MarkTaskFinish, GetMissingAuthors, UploadAuthor


class YunyizzTrait(object):
    def mark_spider_account_offline(self):
        return SetSpiderAccountOffline().send()

    def mark_task_waiting(self):
        return MarkTaskWaiting().send()


    def mark_task_finish(self):
        return MarkTaskFinish().send()

    def are_authors_in_db(self, user_ids):
        return GetMissingAuthors(user_ids).send()

    def upload_authors(self, user_id, **kwargs):
        return UploadAuthor(user_id, **kwargs).send()

