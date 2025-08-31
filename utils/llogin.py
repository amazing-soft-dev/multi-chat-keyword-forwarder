import sqlite3
import os


def convert_sqlite_to_string():
    """Конвертирует SQLite сессию в строковую"""

    session_file = '../config/secure_session.session'

    if not os.path.exists(session_file):
        print(f'❌ Файл сессии {session_file} не найден!')
        print('Убедитесь, что файл находится в той же директории')
        return

    try:
        conn = sqlite3.connect(session_file)
        cursor = conn.cursor()

        cursor.execute('SELECT dc_id, server_address, port, auth_key FROM sessions')
        session_data = cursor.fetchone()

        if session_data:
            dc_id, server_address, port, auth_key_blob = session_data

            try:
                from telethon.sessions import StringSession
                try:
                    from telethon.crypto import AuthKey
                except ImportError:
                    from telethon.tl.types import AuthKey

                string_session = StringSession()

                string_session.set_dc(dc_id, server_address, port)

                string_session.auth_key = AuthKey(auth_key_blob)

                session_string = string_session.save()
                print('=' * 50)
                print('✅ Сессия успешно сконвертирована!')
                print('=' * 50)
                print('SESSION_STRING:', session_string)
                print('=' * 50)
                print('\n📋 Скопируйте строку выше для использования')

            except ImportError as e:
                print(f'❌ Ошибка импорта: {e}')
                print('Убедитесь, что установлен telethon: pip install telethon')

        else:
            print('❌ Не найдены данные сессии в файле')

    except sqlite3.Error as e:
        print(f'❌ Ошибка базы данных: {e}')
    except Exception as e:
        print(f'❌ Ошибка: {e}')
    finally:
        if 'conn' in locals():
            conn.close()


if __name__ == '__main__':
    convert_sqlite_to_string()
