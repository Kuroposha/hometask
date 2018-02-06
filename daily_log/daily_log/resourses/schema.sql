-- CREATE TABLE NOT EXISTS dailylog (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   log_manu_act TEXT NOT NULL,
-- );

CREATE TABLE IF NOT EXISTS daily_task (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  discr_of_task TEXT NOT NULL DEFAULT 'name',
  plan_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  status TINYINT NOT NULL DEFAULT 0
)