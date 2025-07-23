from sqlalchemy.orm import Session
from datetime import date
from .models import LineUser, ChatMessage, EventLog
from .schemas import LineUserSchema, ChatMessageSchema

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_line_user(db: Session, line_id: str, name: str, picture: str):
    user = LineUser(line_id=line_id, name=name, picture=picture)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_line_user_mode(db: Session, line_id: str, mode: str):
    user = db.query(LineUser).filter(LineUser.line_id == line_id).first()
    if user:
        user.mode = mode
        db.commit()
        db.refresh(user)
    return user

def block_line_user(db: Session, line_id: str):
    user = db.query(LineUser).filter(LineUser.line_id == line_id).first()
    if user:
        user.blocked_at = func.now()
        db.commit()
        db.refresh(user)
    return user

def renew_line_user(db: Session, line_id: str):
    user = db.query(LineUser).filter(LineUser.line_id == line_id).first()
    if user and user.blocked_at:
        user.blocked_at = None
        user.added_at = func.now()
        db.commit()
        db.refresh(user)
    return user

def create_chat_message(db: Session, line_user_id: str, message: str, is_from_user: bool):
    msg = ChatMessage(line_user_id=line_user_id, message=message, is_from_user=is_from_user)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

def get_chat_history(db: Session, line_user_id: str):
    return db.query(ChatMessage).filter(ChatMessage.line_user_id == line_user_id).all()

def create_event_log(db: Session, line_user_id: str, event_type: str):
    log = EventLog(line_user_id=line_user_id, event_type=event_type)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_dashboard_stats(db: Session):
    today = date.today()
    total_users = db.query(LineUser).count()
    daily_adds = db.query(EventLog).filter(EventLog.event_type == 'add', EventLog.timestamp >= today).count()
    daily_blocks = db.query(EventLog).filter(EventLog.event_type == 'block', EventLog.timestamp >= today).count()
    daily_renews = db.query(EventLog).filter(EventLog.event_type == 'renew', EventLog.timestamp >= today).count()
    return {
        "total_users": total_users,
        "daily_adds": daily_adds,
        "daily_blocks": daily_blocks,
        "daily_renews": daily_renews
    }

def get_all_users(db: Session):
    return db.query(LineUser).all()