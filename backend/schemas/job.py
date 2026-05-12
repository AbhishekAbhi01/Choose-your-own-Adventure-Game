from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class StoryJobBase(BaseModel):
    theme: str

class StoryJobResponse(StoryJobBase):
    job_id: int
    created_at: datetime
    status: str
    story_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None

    class Config:
        from_attribute = True


class StoryJobCreate(StoryJobBase):
    pass 