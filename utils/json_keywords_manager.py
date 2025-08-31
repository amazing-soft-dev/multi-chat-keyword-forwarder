import json
import os
from typing import List
from utils.logger import get_logger

logger = get_logger(__name__)


class JSONKeywordsManager:
    def __init__(self, file_path: str = 'keywords.json'):
        self.file_path = file_path or os.path.join(os.getcwd(), 'keywords.json')
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump({"keywords": [], "ban_words": []}, f, ensure_ascii=False, indent=2)

    def _load_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_data(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def set_keywords(self, words: List[str]):
        data = self._load_data()
        data['keywords'] = [w.strip().lower() for w in words if w.strip()]
        self._save_data(data)

    def get_keywords(self) -> List[str]:
        return self._load_data()['keywords']


    def set_ban_words(self, words: List[str]):
        data = self._load_data()
        data['ban_words'] = [w.strip().lower() for w in words if w.strip()]
        self._save_data(data)

    def get_ban_words(self) -> List[str]:
        return self._load_data()['ban_words']


    def check_text(self, text: str) -> bool:
        if not text:
            return False

        text_lower = text.lower()
        data = self._load_data()


        for ban_word in data['ban_words']:
            if ban_word in text_lower:
                return False


        for keyword in data['keywords']:
            if keyword in text_lower:
                return True

        return False


keywords_manager = JSONKeywordsManager()