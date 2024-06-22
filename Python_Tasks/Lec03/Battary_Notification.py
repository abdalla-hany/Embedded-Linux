# program to push the pc battary percentage


from plyer import notification
import psutil


battary = psutil.sensors_battery()
percentage = battary.percent
print(percentage)

notification.notify(
        title="Battary Percentage",
        message=str(percentage),
        timeout=10  # Notification will stay for 10 seconds
    )

