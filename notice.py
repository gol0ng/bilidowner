from winotify import Notification


def show_notification(title, message):
    toast = Notification(
        app_id="莫小荒",  # 应用程序名称
        title=title,
        msg=message,
        duration="short",  # 通知显示时间
    )
    toast.show()

