from win10toast import ToastNotifier

toastm = ToastNotifier()

toastm.show_toast(title="Notification",msg="Work Time"
                  ,icon_path="date_utensils_and_tools_clock_alarm_timer_time_icon_256440.ico",
                  duration=10,threaded=True)