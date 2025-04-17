import json
import os
from typing import Dict, Any, Optional

class DatabaseHandler:
    def __init__(self, db_file: str = 'channel_settings.json'):
        self.db_file = db_file
        self._ensure_db_exists()
    
    def _ensure_db_exists(self) -> None:
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump({"channels": {}}, f)
    
    def load_data(self) -> Dict[str, Any]:
        try:
            with open(self.db_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            default_data = {"channels": {}}
            self._save_data(default_data)
            return default_data
    
    def _save_data(self, data: Dict[str, Any]) -> None:
        with open(self.db_file, 'w') as f:
            json.dump(data, f, indent=4)
    
    def set_channel_model(self, channel_id: int, model_name: str) -> None:
        data = self.load_data()
        data["channels"][str(channel_id)] = {"model": model_name}
        self._save_data(data)
    
    def get_channel_model(self, channel_id: int) -> Optional[str]:
        data = self.load_data()
        channel_data = data["channels"].get(str(channel_id))
        if channel_data:
            return channel_data.get("model")
        return None
    
    def remove_channel(self, channel_id: int) -> bool:
        data = self.load_data()
        channel_id_str = str(channel_id)
        if channel_id_str in data["channels"]:
            del data["channels"][channel_id_str]
            self._save_data(data)
            return True
        return False
    
    def list_channels(self) -> Dict[str, Any]:
        data = self.load_data()
        return data["channels"]