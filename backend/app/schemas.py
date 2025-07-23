from pydantic import BaseModel
from datetime import datetime

class LineUserSchema(BaseModel):
    line_id: str
    name: str
    picture: str | None
    mode: str
    added_at: datetime
    blocked_at: datetime | None

    class Config:
        from_attributes = True

class ChatMessageSchema(BaseModel):
    line_user_id: str
    message: str
    is_from_user: bool
    timestamp: datetime

    class Config:
        from_attributes = True

class DashboardStats(BaseModel):
    total_users: int
    daily_adds: int
    daily_blocks: int
    daily_renews: int