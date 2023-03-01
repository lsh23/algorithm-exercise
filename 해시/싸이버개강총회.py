import datetime
import sys

if __name__ == '__main__':

    input = sys.stdin.readline
    ans: int = 0

    S: str
    E: str
    Q: str
    S, E, Q = input().strip().split()
    start_time = datetime.time(hour=int(S.split(":")[0]), minute=int(S.split(":")[1]))
    end_time = datetime.time(hour=int(E.split(":")[0]), minute=int(E.split(":")[1]))
    streaming_end_time = datetime.time(hour=int(Q.split(":")[0]), minute=int(Q.split(":")[1]))
    attend_list: dict = {}

    while True:
        chat_info: str
        chat_info = input()
        try:
            chat_time, nickname = chat_info.split()
            chat_time: datetime.time = datetime.time(hour=int(chat_time.split(":")[0]), minute=int(chat_time.split(":")[1]))
            if chat_time <= start_time:
                attend_list[nickname] = 1
            if end_time <= chat_time <= streaming_end_time:
                if nickname in attend_list and attend_list[nickname] == 1:
                    ans += 1
                    attend_list[nickname] = 0
        except:
            break

    print(ans)
