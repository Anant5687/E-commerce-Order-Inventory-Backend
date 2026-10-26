from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserRequest(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str


class UserResponseData(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    status: int
    data: UserResponseData
    message: str

    model_config = ConfigDict(from_attributes=True)


class UserResponseAll(BaseModel):
    status: int
    data: list[UserResponseData]
    message: str

    model_config = ConfigDict(from_attributes=True)
