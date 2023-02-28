import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()


    def user_exists(self, user_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))


    def get_user_id(self, lol):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `id` = ?", (lol,))
        return result.fetchone()[0]


    def get_all_users(self, lol):
        result = self.cursor.execute(
            "SELECT * FROM `users` WHERE `id` = ?",
            (self.get_user_id(lol),))
        return result.fetchall()


    def add_user(self, user_id):
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()


    def get_all_users(self):
        temp_users = self.cursor.fetchall()
        return temp_users


    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM `users` WHERE `id` = ?", (user_id,))
        return self.conn.commit()


    def add_chat(self, chat_id):
        self.cursor.execute("INSERT INTO `chats` (`chat_id`) VALUES (?)", (chat_id,))
        return self.conn.commit()


    def delete_chat(self, chat_id):
        self.cursor.execute("DELETE FROM `chats` WHERE `id` = ?", (chat_id,))
        return self.conn.commit()


    def chat_exists(self, chat_id):
        """Проверяем, есть ли юзер в базе"""
        result = self.cursor.execute("SELECT `id` FROM `chats` WHERE `chat_id` = ?", (chat_id,))
        return bool(len(result.fetchall()))


    def set_status(self, chat_id, status):
        self.cursor.execute("UPDATE `chats` SET `status` = ? WHERE `chat_id` = ?", (status, chat_id))
        return self.conn.commit()


    def set_greeting(self, chat_id, status):
        self.cursor.execute("UPDATE `chats` SET `greeting` = ? WHERE `chat_id` = ?", (status, chat_id))
        return self.conn.commit()

print("database init")
