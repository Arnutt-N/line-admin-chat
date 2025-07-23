from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from .database import Base

class LineUser(Base):
    __tablename__ = "line_users"
    id = Column(Integer, primary_key=True, index=True)
    line_id = Column(String, unique=True, index=True)
    name = Column(String)
    picture = Column(String)
    mode = Column(String, default="bot")  # bot or manual
    added_at = Column(DateTime, default=func.now())
    blocked_at = Column(DateTime, nullable=True)

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key=True, index=True)
    line_user_id = Column(String, index=True)
    message = Column(String)
    is_from_user = Column(Boolean)
    timestamp = Column(DateTime, default=func.now())

class EventLog(Base):
    __tablename__ = "event_logs"
    id = Column(Integer, primary_key=True, index=True)
    line_user_id = Column(String, index=True)
    event_type = Column(String)  # add, block, renew
    timestamp = Column(DateTime, default=func.now())