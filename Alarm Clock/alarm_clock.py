from playsound import playsound
import datetime
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def set_alarm():
    print(CLEAR)
    while True:
        try:
            alarm_time = input("Enter the alarm time in 24-hour format (HH:MM): ")
            alarm_hours, alarm_minutes = map(int, alarm_time.split(':'))
            if not (0 <= alarm_hours < 24 and 0 <= alarm_minutes < 60):
                raise ValueError("Invalid time format")
            break
        except ValueError as e:
            print(f"{CLEAR_AND_RETURN}")
            print(e)
    return alarm_hours, alarm_minutes

def main():
    print("Welcome to the Python Alarm Clock!")
    alarm_hours, alarm_minutes = set_alarm()
    
    while True:
        now = datetime.datetime.now()
        current_hours, current_minutes = now.hour, now.minute
        if current_hours == alarm_hours and current_minutes == alarm_minutes:
            print("ALARM!")
            playsound('C:\\Users\\paras\\OneDrive\\Desktop\\python\\sync_interns\\Alarm.mp3')
            break
        time.sleep(1)  # sleep for 1 second

if __name__ == '__main__':
    main()