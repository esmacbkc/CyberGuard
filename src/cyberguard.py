import pandas as pd
from db import init_db, insert_log, fetch_logs

# Veritabanını başlat
init_db()

# Örnek log ekleme
insert_log("192.168.1.10", "LOGIN_FAILED", "2026-09-18 16:00:00")
insert_log("192.168.1.11", "LOGIN_SUCCESS", "2026-09-18 16:05:00")
insert_log("192.168.1.10", "LOGIN_FAILED", "2026-09-18 16:10:00")

# Logları çek
logs = fetch_logs()
df = pd.DataFrame(logs, columns=["id", "ip", "action", "timestamp"])

# Basit analiz: en çok hatalı giriş yapan IP
failed_attempts = df[df["action"] == "LOGIN_FAILED"]["ip"].value_counts()
print("🚨 Şüpheli IP adresleri:")
print(failed_attempts)
